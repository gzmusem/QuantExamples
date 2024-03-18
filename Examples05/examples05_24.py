#模块re 示例提取文本中的数字

import re

text = "我有 5 个苹果和 3 个橙子。"

# 使用正则表达式提取数字
numbers = re.findall(r'\d+', text)

# 输出提取到的数字
print(numbers)


