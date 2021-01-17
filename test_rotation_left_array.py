import unittest

from rotation_left_array import rotationLeftArray


class TestSet(unittest.TestCase):

    def testExample(self):

        result1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        result2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]
        result3 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2]
        result4 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3]
        result5 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
        result6 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5]
        result7 = [7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6]
        result8 = [8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7]
        result9 = [9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8]
        result10 = [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result11 = [11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result12 = [12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result13 = [13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result14 = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        result = [result1,
                  result2,
                  result3,
                  result4,
                  result5,
                  result6,
                  result7,
                  result8,
                  result9,
                  result10,
                  result11,
                  result12,
                  result13,
                  result14]

        i = 0
        while i < 100:
            base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            moveLeft = i % len(base)
            self.assertEqual(result[moveLeft], rotationLeftArray(moveLeft, base))
            i += 1
