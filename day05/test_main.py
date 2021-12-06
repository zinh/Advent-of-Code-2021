import unittest
from main import Line, Point


class TestLine(unittest.TestCase):
    def test_from_str(self):
        start_str = '0,9 '
        end_str = ' 5,9'
        line = Line.from_str(start_str, end_str)
        self.assertEqual(line.start, Point(0, 9))
        self.assertEqual(line.end, Point(5, 9))

    def test_min_max(self):
        line = Line.from_str('1, 10', '5, 9')
        self.assertEqual((1, 9), line.min())
        self.assertEqual((5, 10), line.max())

        line = Line.from_str('10, 50', '5, 60')
        self.assertEqual((5, 50), line.min())
        self.assertEqual((10, 60), line.max())

    def test_points(self):
        line = Line.from_str('1,1', '5,5')
        self.assertSetEqual({Point(1, 1), Point(2, 2), Point(
            3, 3), Point(4, 4), Point(5, 5)}, line.points())

        line = Line.from_str('5,5', '2,2')
        self.assertSetEqual({Point(2, 2), Point(
            3, 3), Point(4, 4), Point(5, 5)}, line.points())

        line = Line.from_str('1, 3', '4, 9')
        self.assertSetEqual({Point(1, 3), Point(
            2, 5), Point(3, 7), Point(4, 9)}, line.points())

        line = Line.from_str('3, 4', '12, 10')
        self.assertSetEqual({Point(3, 4), Point(
            6, 6), Point(9, 8), Point(12, 10)}, line.points())
