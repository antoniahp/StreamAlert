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

    def filter_events(self, date__gte: Optional[datetime] = None, date__lte: Optional[datetime] = None, category: Optional[str] = None) -> List[Event]:
        filters = Q()
        if date__gte is not None:
            filters = filters & Q(date__gte=date__gte)
        if date__lte is not None:
            filters = filters & Q(date__lte=date__lte)
        if category is not None:
            filters = filters & Q(category=category)

        events = Event.objects.filter(filters)
        return events
