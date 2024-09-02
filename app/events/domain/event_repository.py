from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional, List

from events.domain.event import Event


class EventRepository(ABC):
    @abstractmethod
    def get_event_by_provider_id(self, provider_id: str) ->  Optional[Event]:
        pass

    @abstractmethod
    def save_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def filter_events(self, date__gte: Optional[datetime] = None, date__lte: Optional[datetime] = None, category: Optional[str] = None) -> List[Event]:
        pass

