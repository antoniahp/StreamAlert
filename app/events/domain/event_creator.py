from datetime import datetime
from uuid import UUID
from events.domain.event import Event

class EventCreator:
    def create_event(self, event_id:UUID, provider_id:str, image:str, date:datetime, category: str) -> Event:
        # Perform domain validation checks here and raise EventCreatorException if needed
        return Event(
            id=event_id,
            provider_id=provider_id,
            image=image,
            date=date,
            category=category
        )
