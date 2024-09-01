from abc import abstractmethod, ABC
from typing import Optional

from events.domain.event import Event


class EventRepository(ABC):
    @abstractmethod
    def get_event_by_provider_id(self, provider_id: str) ->  Optional[Event]:
        pass

    @abstractmethod
    def save_event(self, event: Event) -> None:
        pass