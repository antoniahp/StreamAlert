from abc import ABC, abstractmethod
from typing import List

from app.events.domain.provider_event import ProviderEvent


class EventImporter(ABC):
    @abstractmethod
    def import_events(self) -> List[ProviderEvent]:
        pass
