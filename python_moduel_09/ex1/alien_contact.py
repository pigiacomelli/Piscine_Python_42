from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


# ================= ENUM =================

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


# ================= MODEL =================

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    # ================= CUSTOM VALIDATION =================

    @model_validator(mode="after")
    def validate_business_rules(self):
        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Rule 2: Physical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic requires >= 3 witnesses
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        # Rule 4: Strong signal requires message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) must include a received message")

        return self


# ================= DISPLAY =================

def display_contact(contact: AlienContact):
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")


# ================= MAIN =================

def main():
    print("Alien Contact Log Validation")
    print("=" * 38)

    # ✅ Valid example
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-25T12:00:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        display_contact(valid_contact)

    except ValidationError as e:
        print("Unexpected error:", e)

    print("=" * 38)

    # ❌ Invalid example
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Unknown Sector",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,  # invalid (<3)
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()