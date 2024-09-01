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
    def get_events_by_datetime(self, date_gte: datetime, date_lte:datetime ) -> List[Event]:
        pass
