"""Unit tests for searching algorithms; run from repository root."""

import unittest

from searching import binary_search, linear_search


class SearchingTests(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(linear_search([4, 8, 2, 8], 8), 1)
        self.assertEqual(linear_search([4, 8, 2], 9), -1)
        self.assertEqual(linear_search([], 1), -1)

    def test_binary_search(self):
        values = [-5, 0, 3, 9, 12, 20]
        self.assertEqual(binary_search(values, -5), 0)
        self.assertEqual(binary_search(values, 9), 3)
        self.assertEqual(binary_search(values, 20), 5)
        self.assertEqual(binary_search(values, 7), -1)
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
