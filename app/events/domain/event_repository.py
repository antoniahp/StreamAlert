from abc import abstractmethod, ABC

from app.events.domain.event import Event


class EventRepository(ABC):
    @abstractmethod
    def get_event_by_provider_url(self, provider_url: str) -> Event:
        pass

    @abstractmethod
    def save_event(self, event: Event) -> None:
        pass