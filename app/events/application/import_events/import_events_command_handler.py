from uuid import uuid4

from cqrs.commands.command_handler import CommandHandler
from events.application.import_events.import_events_command import ImportEventsCommand
from events.domain.event_creator import EventCreator
from events.domain.event_importer import EventImporter
from events.domain.event_repository import EventRepository
from events.domain.exceptions.event_creator_exception import EventCreatorException


class ImportEventsCommandHandler(CommandHandler):
    def __init__(self, event_repository: EventRepository, event_creator: EventCreator, event_importer: EventImporter):
        self.__event_repository = event_repository
        self.__event_creator = event_creator
        self.__event_importer = event_importer

    def handle(self, command: ImportEventsCommand):
        provider_events = self.__event_importer.import_events()
        for event in provider_events:
            event_from_repository = self.__event_repository.get_event_by_provider_id(provider_id=event.provider_id)
            if event_from_repository is None:
                try:
                    created_event = self.__event_creator.create_event(
                        event_id=uuid4(),
                        provider_id=event.provider_id,
                        image=event.image,
                        date=event.date,
                        category=event.category
                    )

                    self.__event_repository.save_event(created_event)

                except EventCreatorException as e:
                    print(f"Event with provider_id {event.provider_id} could not be imported. Reason: {str(e)}")
