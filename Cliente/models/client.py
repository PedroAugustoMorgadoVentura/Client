from dataclasses import dataclass
from typing import Optional

@dataclass
class Client:
    id: Optional[int] = None
    name: Optional[str] = None
    phone: Optional[int] = None
    email: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
