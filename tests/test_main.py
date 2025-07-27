import unittest
from src.main import EventProcessor

class TestEventProcessor(unittest.TestCase):
    def test_event_counting(self):
        processor = EventProcessor()
        processor.process_event({'type': 'click', 'timestamp': 123})
        processor.process_event({'type': 'click', 'timestamp': 124})
        processor.process_event({'type': 'view', 'timestamp': 125})
        summary = processor.summary()
        self.assertEqual(summary['click'], 2)
        self.assertEqual(summary['view'], 1)

if __name__ == '__main__':
    unittest.main()
