from typing import Optional
from events.domain.event_repository import EventRepository
from events.domain.event import Event
from datetime import datetime
from typing import List

class DbEventRepository(EventRepository):
    def get_event_by_provider_id(self, provider_id: str) -> Optional[Event]:
        event = Event.objects.filter(provider_id=provider_id).first()
        return event

    def save_event(self, event: Event) -> None:
        event.save()

    def get_events_by_datetime(self, date_gte: datetime, date_lte: datetime) -> List[Event]:
        events = Event.objects.filter(date__gte=date_gte, date__lte=date_lte)
        return events
