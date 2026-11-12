import unittest
from orbit.regression import retry_limit

class RetryRegression(unittest.TestCase):
    def test_retry_limit(self):
        self.assertEqual(retry_limit(), 60, "Intentional showcase failure: retry limit must stay at 60 seconds")
