from django.core.management import BaseCommand

from events.application.import_events.import_events_command import ImportEventsCommand
from events.application.import_events.import_events_command_handler import ImportEventsCommandHandler
from events.domain.event_creator import EventCreator
from events.infraestructure.api_event_importer import ApiEventImporter
from events.infraestructure.db_event_repository import DbEventRepository


class Command(BaseCommand):
    help = 'Import Events'

    def __init__(self):
        super().__init__()
        self.__event_repository = DbEventRepository()
        self.__event_creator = EventCreator()
        self.__event_importer = ApiEventImporter()
        self.__import_event_command_handler = ImportEventsCommandHandler(
            event_creator=self.__event_creator,
            event_importer=self.__event_importer,
            event_repository=self.__event_repository
        )

    def handle(self, *args, **options):
        command = ImportEventsCommand()
        self.__import_event_command_handler.handle(command)