from dataclasses import dataclass
from typing import Optional
@dataclass 
class Product: 
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None