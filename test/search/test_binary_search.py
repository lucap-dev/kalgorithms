import unittest

from search import binary_search


class MyTestCase(unittest.TestCase):
    def test_check_array_parameter_not_null(self):
        pass

    def test_check_element_parameter_not_null(self):
        pass

    def test_element_in_array_upper(self):
        array = [1, 3, 5, 7, 11, 13, 17, 19]
        element = 13
        position = binary_search.find(array, element)
        self.assertEqual(5, position)

    def test_element_in_array_lower(self):
        array = [1, 3, 5, 7, 11, 13, 17, 19]
        element = 3
        position = binary_search.find(array, element)
        self.assertEqual(1, position)

    def test_element_not_in_array_upper(self):
        array = [1, 3, 5, 7, 11, 13, 17, 19]
        element = 23
        position = binary_search.find(array, element)
        self.assertEqual(-1, position)

    def test_element_not_in_array_lower(self):
        array = [3, 5, 7, 11, 13, 17, 19]
        element = 1
        position = binary_search.find(array, element)
        self.assertEqual(-1, position)

    def test_element_in_array_size_1(self):
        array = [3]
        element = 3
        position = binary_search.find(array, element)
        self.assertEqual(0, position)

    def test_element_not_in_array_size_1(self):
        array = [13]
        element = 3
        position = binary_search.find(array, element)
        self.assertEqual(-1, position)

    def test_element_in_array_first_position(self):
        array = [3, 5, 7, 11, 13, 17, 19]
        element = 3
        position = binary_search.find(array, element)
        self.assertEqual(0, position)

    def test_not_element_in_array_last_position(self):
        array = [3, 5, 7, 11, 13, 17, 19]
        element = 19
        position = binary_search.find(array, element)
        self.assertEqual(len(array) - 1, position)

    def test_empty_array(self):
        array = []
        element = 3
        position = binary_search.find(array, element)
        self.assertEqual(-1, position)

if __name__ == '__main__':
    unittest.main()
