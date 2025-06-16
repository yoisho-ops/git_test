# 正方形の面積を求める関数
def calculate_square_area(side_length):
    return side_length ** 2

# 三角形の面積を求める関数
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# 長方形の面積を求める関数
def calculate_rectangle_area(length, width):
    return length * width

# 円の面積を求める関数
def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2

# テスト関数
def test_area_calculations():
    assert calculate_square_area(4) == 16
    assert calculate_triangle_area(3, 4) == 6
    assert calculate_rectangle_area(5, 2) == 10
    assert round(calculate_circle_area(3), 2) == 28.27
    