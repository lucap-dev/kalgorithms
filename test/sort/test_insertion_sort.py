import unittest

from sort import insertion_sort


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        array = [4, 8, 1, 0, 3]
        insertion_sort.sort(array)

        self.assertEqual(array, [0, 1, 3, 4, 8])


if __name__ == '__main__':
    unittest.main()
