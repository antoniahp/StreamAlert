from typing import Optional
from events.domain.event_repository import EventRepository
from events.domain.event import Event
class DbEventRepository(EventRepository):
    def get_event_by_provider_id(self, provider_id: str) -> Optional[Event]:
        event = Event.objects.filter(provider_id=provider_id).first()
        return event


    def save_event(self, event: Event) -> None:
        event.save()