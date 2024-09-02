class EventCreatorException(Exception):
    def __init__(self, reason) -> None:
        self.reason = reason
        self.message = f"Could not create event reason {reason}"
        super().__init__(self.message)
