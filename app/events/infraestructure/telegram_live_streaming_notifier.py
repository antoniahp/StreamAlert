from events.domain.event import Event
from events.domain.live_streaming_notifier import LiveStreamingNotifier
import telegram as _telegram


class TelegramLiveStreamingNotifier(LiveStreamingNotifier):
    def __init__(self, bot_token: str, chat_id: str):
        self.__bot = _telegram.Bot(token=bot_token)
        self.__chat_id = chat_id

    def notify(self, event: Event) -> None:
        live_streaming_url = f"https://geek.live/live/{event.provider_id}"
        caption = f"A las {event.date.strftime('%H:%M')} se realizará un evento de {event.get_category()}. [Ver directo]({live_streaming_url})"
        self.__bot.send_photo(
            chat_id=self.__chat_id,
            photo=event.image,
            caption=caption,
            parse_mode="markdown",
        )