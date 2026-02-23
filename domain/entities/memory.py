class Memory:
    def __init__(self):
        self.events = []

    def add_event(self, events: dict):
        self.events.append(events)
    def last_event(self):
        if self.events:
            return self.events[-1]
        return None
