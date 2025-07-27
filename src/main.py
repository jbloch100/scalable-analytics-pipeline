import time
import random
from collections import defaultdict

class EventProcessor:
    def __init__(self):
        self.metrics = defaultdict(int)

    def process_event(self, event):
        print(f"Processing event: {event}")
        self.metrics[event['type']] += 1

    def summary(self):
        return dict(self.metrics)

def generate_mock_events(n=10):
    types = ['click', 'view', 'impression']
    for _ in range(n):
        yield {'type': random.choice(types), 'timestamp': time.time()}

if __name__ == "__main__":
    processor = EventProcessor()
    for event in generate_mock_events(100):
        processor.process_event(event)
    print("Final Summary:", processor.summary())
