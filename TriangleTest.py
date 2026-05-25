import unittest

def classify_triangle(a, b, c):
    if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
        return "Invalid Input"

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a Triangle"

    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


class TestTriangleClassification(unittest.TestCase):

    # Nhóm 1: Kiểm tra ngoại lệ (Invalid Inputs - Dựa trên biên)
    def test_invalid_inputs(self):
        self.assertEqual(classify_triangle(0, 50, 50), "Invalid Input")  # TC 01: Biên dưới cạnh a
        self.assertEqual(classify_triangle(101, 50, 50), "Invalid Input")  # TC 02: Biên trên cạnh a
        self.assertEqual(classify_triangle(50, 0, 50), "Invalid Input")  # TC 03: Biên dưới cạnh b
        self.assertEqual(classify_triangle(50, 50, 101), "Invalid Input")  # TC 04: Biên trên cạnh c

    # Nhóm 2: Kiểm tra logic nghiệp vụ (Dựa trên Decision Table kết hợp Biên hợp lệ)
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(10, 20, 50), "Not a Triangle")  # TC 05: Tổng 2 cạnh nhỏ hơn
        self.assertEqual(classify_triangle(1, 2, 3), "Not a Triangle")  # TC 06: Chạm biên bất đẳng thức

    def test_equilateral(self):
        self.assertEqual(classify_triangle(50, 50, 50), "Equilateral")  # TC 07: Tam giác đều (Điểm giữa)
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")  # TC 08: Tam giác đều ở biên lớn nhất

    def test_isosceles(self):
        self.assertEqual(classify_triangle(50, 50, 40), "Isosceles")  # TC 09: Cân tại đỉnh c
        self.assertEqual(classify_triangle(40, 50, 50), "Isosceles")  # TC 10: Cân tại đỉnh a
        self.assertEqual(classify_triangle(50, 40, 50), "Isosceles")  # TC 11: Cân tại đỉnh b

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")  # TC 12: Tam giác thường
        self.assertEqual(classify_triangle(98, 99, 100), "Scalene")  # TC 13: Tam giác thường áp sát biên trên


if __name__ == '__main__':
    unittest.main()