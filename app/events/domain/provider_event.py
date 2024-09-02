from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ProviderEvent:
    provider_id: str
    image: str
    date: datetime
    category:str
    title: str
