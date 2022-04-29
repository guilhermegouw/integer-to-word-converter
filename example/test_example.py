import unittest
from .example import example


class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(example(1, 2), 3)