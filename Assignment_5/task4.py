"""
Job Applicant Scoring System
----------------------------

This module defines a transparent scoring pipeline for job applicants based on
structured feature inputs. The design emphasizes explainability, tunable
weightings, and fairness safeguards (e.g., no demographic attributes).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Tuple

Numeric = float


@dataclass
class FeatureRule:
    """Represents one feature's contribution to the applicant score."""

    weight: Numeric
    bounds: Tuple[Numeric, Numeric]
    description: str

    def normalize(self, value: Numeric) -> Numeric:
        """Clamp and scale the raw value into [0, 1] range."""
        lower, upper = self.bounds
        if lower == upper:
            return 0.0
        clamped = max(lower, min(upper, value))
        return (clamped - lower) / (upper - lower)

    def contribution(self, value: Numeric) -> Numeric:
        """Return the weighted contribution of this feature."""
        return self.weight * self.normalize(value)


@dataclass
class ApplicantScorer:
    """
    Composite scoring utility with transparency and fairness safeguards.

    The default rules reward job-relevant factors only:
        - years_experience: Recognizes practical exposure.
        - education_level: Encourages higher education, capped at master's level.
        - technical_assessment: Direct measure of skill proficiency.
        - soft_skills_rating: Communication, teamwork, leadership, etc.
        - relevant_certifications: Bonus for industry credentials.
    """

    feature_rules: Mapping[str, FeatureRule] = field(
        default_factory=lambda: {
            "years_experience": FeatureRule(
                weight=0.25,
                bounds=(0.0, 15.0),
                description="Total years of relevant professional experience.",
            ),
            "education_level": FeatureRule(
                weight=0.15,
                bounds=(0.0, 3.0),
                description="Highest degree normalized (0: none, 1: bachelor, 2: master, 3: doctorate).",
            ),
            "technical_assessment": FeatureRule(
                weight=0.35,
                bounds=(0.0, 100.0),
                description="Technical assessment score out of 100.",
            ),
            "soft_skills_rating": FeatureRule(
                weight=0.15,
                bounds=(0.0, 5.0),
                description="Panel rating for communication, collaboration, leadership (0-5).",
            ),
            "relevant_certifications": FeatureRule(
                weight=0.10,
                bounds=(0.0, 5.0),
                description="Count of certifications aligned with the role (capped at 5).",
            ),
        }
    )

    def score(self, features: Mapping[str, Numeric]) -> Numeric:
        """
        Compute the aggregate score for the applicant from 0 to 100.

        Any missing feature defaults to the minimum bound (i.e., neutral zero).
        Demographic attributes must NOT be part of the input; validators should
        strip such fields before calling this function.
        """
        total_weight = sum(rule.weight for rule in self.feature_rules.values())
        if not total_weight:
            raise ValueError("Total feature weight must be greater than zero.")

        weighted_sum = 0.0
        breakdowns: List[str] = []
        for name, rule in self.feature_rules.items():
            value = features.get(name, rule.bounds[0])
            contribution = rule.contribution(value)
            weighted_sum += contribution
            breakdowns.append(f"{name}: value={value}, contribution={contribution:.2f}")

        score_out_of_100 = (weighted_sum / total_weight) * 100.0
        self._validate_no_sensitive_features(features)

        # Debug statement (could be replaced by logging in production)
        print("Score breakdown:\n  " + "\n  ".join(breakdowns))
        return round(score_out_of_100, 2)

    @staticmethod
    def _validate_no_sensitive_features(features: Mapping[str, Numeric]) -> None:
        """Reject inputs containing obvious demographic proxies."""
        sensitive = {"gender", "race", "ethnicity", "age", "marital_status"}
        overlap = sensitive.intersection(features)
        if overlap:
            raise ValueError(
                f"Sensitive attributes {sorted(overlap)} must be excluded from scoring."
            )


def explain_weights(scorer: ApplicantScorer) -> Dict[str, str]:
    """Return a human-readable explanation for each feature rule."""
    explanations = {
        name: f"Weight {rule.weight:.2f} on range {rule.bounds}: {rule.description}"
        for name, rule in scorer.feature_rules.items()
    }
    return explanations


if __name__ == "__main__":
    scorer = ApplicantScorer()
    applicant_features = {
        "years_experience": 7,
        "education_level": 2,  # Master's degree
        "technical_assessment": 82,
        "soft_skills_rating": 4.2,
        "relevant_certifications": 3,
    }

    print("Feature explanations:")
    for feature, explanation in explain_weights(scorer).items():
        print(f"- {feature}: {explanation}")

    total_score = scorer.score(applicant_features)
    print(f"\nFinal applicant score: {total_score}/100")

