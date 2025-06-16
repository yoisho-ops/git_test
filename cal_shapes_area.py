# 正方形の面積を求める関数
def calculate_square_area(side_length: float) -> float:
    return side_length ** 2

# 三角形の面積を求める関数
def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

# 長方形の面積を求める関数
def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width

# 円の面積を求める関数
def calculate_circle_area(radius: float) -> float:
    import math
    return math.pi * radius ** 2

# 正18角形の面積を求める関数
def calculate_regular_polygon_area(side_length: float, num_sides: int) -> float:
    import math
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))



# テスト関数
def test_area_calculations():
    assert calculate_square_area(4) == 16
    assert calculate_triangle_area(3, 4) == 6
    assert calculate_rectangle_area(5, 2) == 10
    assert round(calculate_circle_area(3), 2) == 28.27
    assert round(calculate_regular_polygon_area(3, 18), 2) == 84.303
# テスト実行
if __name__ == "__main__":
    test_area_calculations()
    print("All area calculations passed successfully.")
