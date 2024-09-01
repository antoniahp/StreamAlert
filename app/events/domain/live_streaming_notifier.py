from abc import ABC, abstractmethod
from events.domain.event import Event

class LiveStreamingNotifier(ABC):
    @abstractmethod
    def notify(self, event:Event) -> None:
        pass
