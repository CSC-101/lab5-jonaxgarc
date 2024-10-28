import data
import lab5
import unittest
from data import Time
from data import Point




# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = Time(1, 2, 3)
        time2 = Time(2, 3, 4)
        result = lab5.time_add(time1, time2)
        expected = Time(3, 5, 7)
        self.assertEqual(expected, result)
    def test_time_add1(self):
        time1 = Time(3, 12, 35)
        time2 = Time(4, 54, 43)
        result = lab5.time_add(time1, time2)
        expected = Time(8, 7, 18)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending1(self):
        input = [5.0, 3.0, 1.0]
        result = lab5.is_descending(input)
        expected = True
        self.assertEqual(expected, result)
    def test_is_descending2(self):
        input = [1.0, 3.0, 5.0]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)


    # Part 5
    def test_largest_between1(self):
        lst = [1, 5, 6, 5]
        result = lab5.largest_between(lst, 1, 2)
        expected = 2
        self.assertEqual(expected, result)
    def test_largest_between2(self):
        lst = [13, 53, 26, 45]
        result = lab5.largest_between(lst, 1, 3)
        expected = 1
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin1(self):
        lst = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4)]
        result = lab5.furthest_from_origin(lst)
        expected = 3
        self.assertEqual(expected, result)
    def test_furthest_from_origin2(self):
        lst = [Point(2, 1), Point(3, 2), Point(5, 3), Point(1, 4)]
        result = lab5.furthest_from_origin(lst)
        expected = 2
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
