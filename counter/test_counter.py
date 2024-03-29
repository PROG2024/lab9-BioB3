"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter

class CounterTest(unittest.TestCase):
    """Test for the Counter class"""

    def setUp(self):
        """Create a new Counter before each test"""
        self.counter_1 = Counter()
        self.counter_2 = Counter()

    def test_counter_instance(self):
        """__new__ return the same Counter"""
        self.assertEqual(id(self.counter_1), id(self.counter_2))
        self.assertEqual(self.counter_1.count, self.counter_2.count)

    def test_increment(self):
        """Counter's count increase when increment is called
        regardless of which variable is used
        """
        self.counter_1.increment()
        self.assertEqual(1, self.counter_1.count, self.counter_2.count)
        self.counter_2.increment()
        new_counter = Counter()
        self.assertEqual(2, self.counter_1.count, self.counter_2.count)
        self.assertEqual(2, new_counter.count)
