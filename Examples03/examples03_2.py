#函数定义和调用

def calculate_area(length, width):
    """
    计算矩形的面积。

    参数:
    length (float) - 矩形的长度。
    width (float) - 矩形的宽度。

    返回:
    float - 矩形的面积。
    """
    area = length * width
    return area

rectangle_area = calculate_area(5.0, 3.0)
print(f"矩形的面积是: {rectangle_area} 平方单位")  # 输出: 矩形的面积是: 15.0 平方单位