import unittest

from problems.problem_380_2 import RandomizedSet


class TestCase(unittest.TestCase):
    def test_getRandom(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))
        self.assertFalse(randomizedSet.remove(2))
        self.assertTrue(randomizedSet.insert(2))
        self.assertEqual(randomizedSet.getRandom(), 1)
        self.assertTrue(randomizedSet.remove(1))
        self.assertFalse(randomizedSet.insert(2))
        self.assertEqual(randomizedSet.getRandom(), 2)

    def test_getRandom2(self):
        randomizedSet = RandomizedSet()
        self.assertFalse(randomizedSet.remove(0))
        self.assertFalse(randomizedSet.remove(0))
        self.assertTrue(randomizedSet.insert(0))
        self.assertEqual(randomizedSet.getRandom(), 0)
        self.assertTrue(randomizedSet.remove(0))
        self.assertTrue(randomizedSet.insert(0))
