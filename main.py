# cal_shapes_area.py内の関数を呼び出すためのmain.pyのコード
from cal_shapes_area import (
    calculate_square_area,
    calculate_triangle_area,
    calculate_rectangle_area,
    calculate_circle_area
)
def main():
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