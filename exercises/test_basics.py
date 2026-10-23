"""Unit tests for exercises/basics.py; uses only Python's standard library."""

import unittest

from basics import count_vowels, factorial, is_even, remove_duplicates


class BasicsTests(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(12))
        self.assertFalse(is_even(7))

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_rejects_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_count_vowels_is_case_insensitive(self):
        self.assertEqual(count_vowels("Computer Science"), 6)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_remove_duplicates_preserves_order(self):
        self.assertEqual(remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(remove_duplicates([]), [])


if __name__ == "__main__":
    unittest.main()
