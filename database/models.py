from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    name: str
    email: str
    password_hash: str

@dataclass
class Medication:
    id: Optional[int]
    user_id: int
    name: str
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    rx_cui: Optional[str] = None  # NEW

@dataclass
class Reminder:
    id: Optional[int]
    medication_id: int
    time: str
    status: str = "pending"
    taken_at: Optional[str] = None      # NEW
    next_dose_at: Optional[str] = None  # NEW

@dataclass
class Interaction:
    id: Optional[int]
    medication1: str
    medication2: str
    interaction_level: Optional[str] = None
    description: Optional[str] = None
