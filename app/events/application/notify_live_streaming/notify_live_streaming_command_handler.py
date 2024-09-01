from datetime import datetime, timedelta

from django.utils import timezone

from cqrs.commands.command_handler import CommandHandler
from events.application.notify_live_streaming.notify_live_streaming_command import NotifyLiveStreamingCommand
from events.domain.event_repository import EventRepository
from events.domain.live_streaming_notifier import LiveStreamingNotifier


class NotifyLiveStreamingCommandHandler(CommandHandler):
   def __init__(self, event_repository: EventRepository, live_streaming_notifier: LiveStreamingNotifier):
       self.__event_repository = event_repository
       self.__live_streaming_notifier = live_streaming_notifier

   def handle(self, command: NotifyLiveStreamingCommand):
       now = timezone.now()
       max_start_date_to_notify = now + timedelta(minutes=command.delta_time_minutes)
       next_lives = self.__event_repository.get_events_by_datetime(date_gte=now, date_lte=max_start_date_to_notify)
       for event in next_lives:
           self.__live_streaming_notifier.notify(event)
