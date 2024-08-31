from datetime import datetime

from app.events.domain.event import Event


class EventCreator:
    def create_event(self, provider_url:str, image:str, date:datetime, category: str ):
        return Event(
            provider_url=provider_url,
            image=image,
            date=date,
            category=category
        )