"""Program demonstrating manual vs AI-generated inline comments."""

# Manual comment: import dataclass to reduce boilerplate for student records.
from dataclasses import dataclass, field


# Manual comment: define the SRU student representation with the required attributes.
@dataclass
class SruStudent:
    # Manual comment: student name keeps the human-readable identifier.
    name: str
    # Manual comment: roll_no uniquely identifies the student.
    roll_no: int
    # Manual comment: hostel_status captures Yes/No or similar descriptor.
    hostel_status: str
    # Manual comment: pending_fee tracks the amount to be updated via fee_update.
    pending_fee: float = field(default=0.0)

    # Manual comment: fee_update adjusts pending_fee when a payment is made.
    def fee_update(self, amount_paid: float) -> None:
        # Manual comment: basic validation ensures negative payments aren't allowed.
        if amount_paid < 0:
            raise ValueError("Payment amount cannot be negative.")

        # Manual comment: subtract the paid amount to reflect updated fee.
        self.pending_fee = max(0.0, self.pending_fee - amount_paid)

    # Manual comment: display_details prints current state for demonstration.
    def display_details(self) -> str:
        # Manual comment: creating formatted string keeps presentation logic tidy.
        details = (
            f"Name: {self.name}\n"
            f"Roll No.: {self.roll_no}\n"
            f"Hostel Status: {self.hostel_status}\n"
            f"Pending Fee: ₹{self.pending_fee:.2f}"
        )
        # Manual comment: returning the string allows flexible reuse by callers.
        return details


# AI-generated inline comments captured from Cursor AI for comparison.
AI_GENERATED_INLINE_COMMENTS = """
from dataclasses import dataclass, field  # AI: brings in helper for data classes

@dataclass  # AI: automatically adds init and repr based on fields
class SruStudent:
    name: str  # AI: student's full name
    roll_no: int  # AI: student identification number
    hostel_status: str  # AI: indicates if student is a hosteller or day scholar
    pending_fee: float = field(default=0.0)  # AI: outstanding fee amount

    def fee_update(self, amount_paid: float) -> None:
        if amount_paid < 0:
            raise ValueError("Payment amount cannot be negative.")
        self.pending_fee = max(0.0, self.pending_fee - amount_paid)  # AI: ensure non-negative fee

    def display_details(self) -> str:
        details = (
            f"Name: {self.name}\\n"
            f"Roll No.: {self.roll_no}\\n"
            f"Hostel Status: {self.hostel_status}\\n"
            f"Pending Fee: ₹{self.pending_fee:.2f}"
        )
        return details
"""


# Manual comment: helper builds an instance, simulates payment, and prints both comment sets.
def main() -> None:
    # Manual comment: instantiate with sample data to illustrate methods.
    student = SruStudent(name="Aanya Rao", roll_no=230145, hostel_status="Hosteller", pending_fee=50000.0)

    # Manual comment: perform a payment update and show new pending fee.
    student.fee_update(15000.0)

    # Manual comment: display details for verification.
    print(student.display_details())

    print("\n--- Manual Inline Comments (in-code) ---")
    print("Review the '#' annotations directly in TASK2.PY for manual commentary.")

    print("\n--- AI-Generated Inline Comments ---")
    print(AI_GENERATED_INLINE_COMMENTS.strip())

    print("\nComparison Insight:")
    print(
        "Manual comments focus on intent, validation rationale, and reuse strategy, "
        "while AI comments emphasize direct descriptors (e.g., 'student's full name'). "
        "Both are useful, but manual notes provide deeper context for design decisions."
    )


if __name__ == "__main__":
    main()


