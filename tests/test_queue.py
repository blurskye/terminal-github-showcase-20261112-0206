import unittest
from orbit.queue import Task, retry_delay, summarize


class QueueTests(unittest.TestCase):
    def test_retry_is_bounded(self):
        self.assertEqual(retry_delay(3), 8)
        self.assertEqual(retry_delay(20), 60)

    def test_queue_summary(self):
        self.assertEqual(summarize([Task("build"), Task("ship", state="done")]),
                         {"queued": 1, "running": 0, "done": 1})
