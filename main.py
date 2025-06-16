# cal_shapes_area.py内の関数を呼び出すためのmain.pyのコード

from cal_shapes_area import (
    calculate_square_area,
    calculate_triangle_area,
    calculate_rectangle_area,
    calculate_circle_area,
    calculate_cube_volume,
    calculate_cylinder_volume,
    calculate_cone_volume,
    calculate_sphere_volume,
    calculate_pyramid_volume
)

def main():
    # 立方体の体積を計算
    cube_volume = calculate_cube_volume(3)
    print(f"立方体の体積: {cube_volume}")

    # 円柱の体積を計算
    cylinder_volume = calculate_cylinder_volume(3, 5)
    print(f"円柱の体積: {cylinder_volume}")

    # 円錐の体積を計算
    cone_volume = calculate_cone_volume(3, 5)
    print(f"円錐の体積: {cone_volume}")

    # 球の体積を計算
    sphere_volume = calculate_sphere_volume(3)
    print(f"球の体積: {sphere_volume}")

    # 三角錐の体積を計算
    pyramid_volume = calculate_pyramid_volume(10, 5)
    print(f"三角錐の体積: {pyramid_volume}")

    # 正方形の面積を計算
    square_area = calculate_square_area(4)
    print(f"正方形の面積: {square_area}")

    # 三角形の面積を計算
    triangle_area = calculate_triangle_area(3, 4)
    print(f"三角形の面積: {triangle_area}")

    # 長方形の面積を計算
    rectangle_area = calculate_rectangle_area(5, 2)
    print(f"長方形の面積: {rectangle_area}")

    # 円の面積を計算
    circle_area = calculate_circle_area(3)
    print(f"円の面積: {round(circle_area, 2)}")



if __name__ == "__main__":
    main()

# テスト関数を実行
# test_area_calculations()  # テスト関数を実行する場合はコメントを外す  

