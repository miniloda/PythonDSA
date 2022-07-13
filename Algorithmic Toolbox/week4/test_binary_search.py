from binary_search_2 import binary_search_with_duplicates
import unittest
class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search_with_duplicates([], 3), -1)
        self.assertEqual(binary_search_with_duplicates([1, 2], 3), -1)
        self.assertEqual(binary_search_with_duplicates([1, 2, 3,3, 4], 3), 2)
        self.assertEqual(binary_search_with_duplicates([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_with_duplicates([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_with_duplicates([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_with_duplicates([1,1,1,1, 2, 3, 4], 2), 4)


if __name__ == '__main__':
    unittest.main()