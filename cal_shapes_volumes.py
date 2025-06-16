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
def test_volume_calculations():
    assert calculate_cube_volume(3) == 27
    assert round(calculate_cylinder_volume(3, 5), 2) == 141.37
    assert round(calculate_cone_volume(3, 5), 2) == 28.27
    assert round(calculate_sphere_volume(3), 2) == 113.1
    assert calculate_pyramid_volume(10, 5) == 16.67
