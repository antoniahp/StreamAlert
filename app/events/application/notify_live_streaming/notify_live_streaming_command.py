from dataclasses import dataclass

from cqrs.commands.command import Command

@dataclass(frozen=True)
class NotifyLiveStreamingCommand(Command):
    delta_time_minutes: int