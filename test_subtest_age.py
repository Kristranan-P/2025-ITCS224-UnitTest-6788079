import unittest
from age import categorize_by_age

class TestAgeSubtests(unittest.TestCase):

    def test_child_age(self):
        """Tests all valid ages in the Child range (0-9)"""
        for age in range(0, 10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(categorize_by_age(age), "Child")

if __name__ == "__main__":
    unittest.main(verbosity=2)