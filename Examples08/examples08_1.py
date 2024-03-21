#NumPy示例

import numpy as np

# 创建一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # 输出: [1 2 3 4 5]

# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# 输出:
# [[1 2 3]
#  [4 5 6]]

# 数组相加
arr3 = arr1 + arr1
print(arr3)  # 输出: [2 4 6 8 10]

# 数组相乘
arr4 = arr1 * 2
print(arr4)  # 输出: [2 4 6 8 10]

# 数组间的乘法
arr5 = arr1 * arr1
print(arr5)  # 输出: [1 4 9 16 25]


# 切片
print(arr1[1:4])  # 输出: [2 3 4]

# 索引
print(arr2[0, 1])  # 输出: 2


# 求平方根
sqrt_arr = np.sqrt(arr1)
print(sqrt_arr)  # 输出: [1.         1.41421356 1.73205081 2.         2.23606798]

# 求正弦值
sin_arr = np.sin(arr1)
print(sin_arr)
# 输出: [0.84147098 0.90929743 0.14112001 -0.7568025  -0.95892427]

# 求和
sum_arr = np.sum(arr1)
print(sum_arr)  # 输出: 15

# 求平均值
mean_arr = np.mean(arr1)
print(mean_arr)  # 输出: 3.0

