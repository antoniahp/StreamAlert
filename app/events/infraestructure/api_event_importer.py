from datetime import datetime
from typing import List

import requests

from config.settings import PROVIDER_API_URL
from events.domain.event_importer import EventImporter
from events.domain.provider_event import ProviderEvent


class ApiEventImporter(EventImporter):
    API_URL = f"{PROVIDER_API_URL}/live-shoppings?limit=100&offset=0&ordering=start_datetime&status=3&status=1"
    def import_events(self) -> List[ProviderEvent]:
        response = requests.get(self.API_URL)
        json_response = response.json()
        provider_events=[]
        for event in json_response["results"]:
            provider_event = ProviderEvent(
                provider_id=event["id"],
                image=event["cover"],
                date=datetime.fromisoformat(event["start_datetime"]),
                category=event["category"],
            )
            provider_events.append(provider_event)

        return provider_events
