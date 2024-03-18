#模块re 示例替换文本中的特定模式

import re

text = "Hello, World! Hello, Python!"

# 使用正则表达式替换文本
new_text = re.sub(r'Hello', 'Hi', text)

# 输出替换后的文本
print(new_text)


