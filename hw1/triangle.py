import math
import unittest

def classify_triangle(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        return "Invalid Input"

    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "Not a Triangle"

    if (a == b) and (b == c):
        return "Equilateral Triangle"

    if (a == b) or (b == c) or (a == c):
        if (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)) or (math.pow(b, 2) + math.pow(c, 2) == math.pow(a, 2)) or (math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2)):
            return "Isosceles Right Triangle"
        else:
            return "Isosceles Triangle"

    if (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)) or (math.pow(b, 2) + math.pow(c, 2) == math.pow(a, 2)) or (math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2)):
        return "Scalene Right Triangle"

    return "Scalene Triangle"

class TestTriangle(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right Triangle")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles Triangle")
        self.assertEqual(classify_triangle(3, 4, 4), "Isosceles Triangle")
        self.assertEqual(classify_triangle(0, 3, 4), "Invalid Input")
        self.assertEqual(classify_triangle(3, 4, 7), "Not a Triangle")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
