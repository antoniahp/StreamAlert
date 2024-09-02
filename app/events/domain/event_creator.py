from datetime import datetime
from uuid import UUID
from events.domain.event import Event
from events.domain.exceptions.event_creator_exception import EventCreatorException


class EventCreator:
    def create_event(self, event_id:UUID, provider_id:str, image:str, date:datetime, category: str, title: str) -> Event:
        if len(title) > 250:
            raise EventCreatorException(reason="The maximum length of the title must be 250 characters")

        return Event(
        id=event_id,
        provider_id=provider_id,
        image=image,
        date=date,
        category=category,
        title=title
        )
