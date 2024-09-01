from django.core.management import BaseCommand

from config import settings
from events.application.notify_live_streaming.notify_live_streaming_command import NotifyLiveStreamingCommand
from events.application.notify_live_streaming.notify_live_streaming_command_handler import NotifyLiveStreamingCommandHandler
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.telegram_live_streaming_notifier import TelegramLiveStreamingNotifier

class Command(BaseCommand):
    help = 'Notify live streamings'

    def __init__(self):
        super().__init__()
        self.__event_repository = DbEventRepository()
        self.__notify_live_streaming_notifier = TelegramLiveStreamingNotifier(bot_token=settings.TELEGRAM_BOT_TOKEN, chat_id=settings.TELEGRAM_CHAT_ID)
        self.__notify_live_streaming_command_handler = NotifyLiveStreamingCommandHandler(event_repository=self.__event_repository, live_streaming_notifier=self.__notify_live_streaming_notifier)

    def handle(self, *args, **options):
        command = NotifyLiveStreamingCommand(delta_time_minutes=30)
        self.__notify_live_streaming_command_handler.handle(command)
