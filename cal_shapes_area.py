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

# 立方体の体積を求める関数
def calculate_cube_volume(side_length: float) -> float:
    return side_length ** 3

# 円柱の体積を求める関数
def calculate_cylinder_volume(radius: float, height: float) -> float:
    import math
    return math.pi * radius ** 2 * height

# 円錐の体積を求める関数
def calculate_cone_volume(radius: float, height: float) -> float:
    import math
    return (1/3) * math.pi * radius ** 2 * height

# 球の体積を求める関数
def calculate_sphere_volume(radius: float) -> float:
    import math
    return (4/3) * math.pi * radius ** 3

# 三角錐の体積を求める関数
def calculate_pyramid_volume(base_area: float, height: float) -> float:
    return (1/3) * base_area * height

# テスト関数
def test_area_calculations():
    assert calculate_square_area(4) == 16
    assert calculate_triangle_area(3, 4) == 6
    assert calculate_rectangle_area(5, 2) == 10
    assert round(calculate_circle_area(3), 2) == 28.27
    assert calculate_cube_volume(3) == 27
    assert round(calculate_cylinder_volume(3, 5), 2) == 141.37
    assert round(calculate_cone_volume(3, 5), 2) == 28.27
    assert round(calculate_sphere_volume(3), 2) == 113.1
    assert calculate_pyramid_volume(10, 5) == 16.67
