"""
A secure login system implemented without hardcoded credentials or insecure logic.

Expected Output #1 – Description of risks and revised secure version:

- AI-generated samples often include hardcoded usernames/passwords, default "admin"
  accounts, or unconditional `return True` branches that effectively bypass auth.
- Storing plaintext passwords or embedding API keys/secrets inline creates immediate
  compromise risk if the code is leaked, and prevents rotation without redeploying.
- Logging raw credentials or failing to validate inputs can leak sensitive data and
  enable brute-force or injection attacks.
- The secure revision below eliminates those flaws by sourcing credentials from an
  external store, hashing with PBKDF2, enforcing uniform error handling, and running
  a simple static audit to flag any reintroduced hardcoded secrets.

The code demonstrates the core pieces you would expect from an application-level
authentication module:

- Credentials are persisted outside of the source code (JSON file whose location
  is supplied via the `CREDENTIAL_STORE_PATH` environment variable).
- Passwords are never stored in plaintext; they are salted and hashed with PBKDF2.
- A single entry-point, `LoginService.authenticate`, performs timing-safe password
  verification, rejecting missing users or incorrect passwords without leaking detail.
- An automated security self-check (`audit_security_posture`) validates that the
  module does not contain obvious hardcoded secrets or bypass conditions that some
  AI-generated code might introduce inadvertently.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

DEFAULT_ITERATIONS = 100_000
CREDENTIAL_STORE_PATH = Path(
    os.getenv("CREDENTIAL_STORE_PATH", "credential_store.json")
)


def _hash_password(password: str, *, salt: bytes) -> bytes:
    """Derive a PBKDF2-HMAC hash using SHA-256."""
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        DEFAULT_ITERATIONS,
    )


def generate_password_hash(password: str) -> str:
    """
    Produce a salted password hash ready for storage.

    The resulting token contains both the salt and the derived hash, encoded in base64.
    """
    salt = os.urandom(16)
    derived = _hash_password(password, salt=salt)
    return base64.b64encode(salt + derived).decode("ascii")


def verify_password(password: str, encoded: str) -> bool:
    """Verify a plaintext password against a stored base64-encoded hash."""
    try:
        decoded = base64.b64decode(encoded.encode("ascii"))
    except (ValueError, TypeError) as exc:
        raise ValueError("Stored password hash is corrupted") from exc

    salt, stored_hash = decoded[:16], decoded[16:]
    computed = _hash_password(password, salt=salt)
    return hmac.compare_digest(stored_hash, computed)


@dataclass
class User:
    username: str
    password_hash: str


class CredentialStore:
    """Simple file-backed credential repository."""

    def __init__(self, path: Path = CREDENTIAL_STORE_PATH) -> None:
        self.path = path
        self._ensure_store_exists()

    def _ensure_store_exists(self) -> None:
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def _load(self) -> Dict[str, str]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data: Dict[str, str]) -> None:
        self.path.write_text(json.dumps(data), encoding="utf-8")

    def get_user(self, username: str) -> Optional[User]:
        data = self._load()
        if username not in data:
            return None
        return User(username=username, password_hash=data[username])

    def add_user(self, username: str, password: str) -> User:
        data = self._load()
        if username in data:
            raise ValueError("User already exists")
        data[username] = generate_password_hash(password)
        self._save(data)
        return User(username=username, password_hash=data[username])


class LoginService:
    """Handles user authentication against the credential store."""

    def __init__(self, store: Optional[CredentialStore] = None) -> None:
        self.store = store or CredentialStore()

    def authenticate(self, username: str, password: str) -> bool:
        if not username or not password:
            raise ValueError("Username and password are required")

        user = self.store.get_user(username)
        if user is None:
            return False
        return verify_password(password, user.password_hash)


def audit_security_posture(source: str) -> Dict[str, bool]:
    """
    Naïve automated audit to detect common insecure patterns that AI-generated
    code could accidentally introduce.
    """
    return {
        "hardcoded_password_literal": "password" in source.lower()
        and any(token in source for token in ["=", "==", "!="]),
        "hardcoded_username_literal": "admin" in source.lower(),
        "insecure_shortcuts": "if True" in source or "return True" in source,
    }


SECURITY_ANALYSIS = audit_security_posture(Path(__file__).read_text(encoding="utf-8"))


if __name__ == "__main__":
    service = LoginService()

    print("Security audit flags:", SECURITY_ANALYSIS)
    action = input("Select action (register/login): ").strip().lower()

    if action not in {"register", "login"}:
        raise SystemExit("Unsupported action")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if action == "register":
        service.store.add_user(username, password)
        print("User registered. Password stored as salted PBKDF2 hash.")
    else:
        if service.authenticate(username, password):
            print("Login successful.")
        else:
            print("Login failed: invalid credentials.")

