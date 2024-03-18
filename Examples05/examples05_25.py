#模块re 示例拆分文本

import re

text = "apple,banana,orange;grape"

# 使用正则表达式拆分文本
fruits = re.split(r'[,;]', text)

# 输出拆分后的结果
print(fruits)


