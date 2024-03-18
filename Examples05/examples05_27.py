#模块json 示例Python 将 JSON 字符串解析为 Python 对象

import json

# JSON 字符串
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# 将 JSON 字符串解析为 Python 字典
data = json.loads(json_string)

# 访问 Python 字典中的数据
print(data["name"])
print(data["age"])
print(data["city"])


