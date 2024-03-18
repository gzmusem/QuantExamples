#模块re 示例匹配文本中的电子邮件地址

import re

text = "请联系我:gzmusem@outlook.com,或者发邮件到 gzmusem@163.com。"

# 使用正则表达式匹配电子邮件地址
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)

# 输出匹配到的电子邮件地址
for match in matches:
    print(match)



