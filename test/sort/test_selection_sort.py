import unittest

from sort import selection_sort


class MyTestCase(unittest.TestCase):
    def test_swap(self):
        array = [3, 5, 7, 11, 13, 17, 19]
        selection_sort.swap(array, 0, len(array) - 1)
        self.assertEqual(array[0], 19)
        self.assertEqual(array[len(array) - 1], 3)

    def test_index_of_minimum(self):
        array = [3, 5, 7, 11, 13, 17, 19]
        i = selection_sort.index_of_minimum(array, 0)
        self.assertEqual(0, i)

    def test_sort(self):
        array = [4, 8, 1, 0, 3]
        print array
        selection_sort.sort(array)
        print array
        self.assertEqual(array, [0, 1, 3, 4, 8])


if __name__ == '__main__':
    unittest.main()
