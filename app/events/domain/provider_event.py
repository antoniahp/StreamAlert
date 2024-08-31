from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProviderEvent():
    provider_url: str
    image: str
    date: datetime
    category:str
