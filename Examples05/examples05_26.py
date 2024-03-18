#模块json 示例Python 对象转换为 JSON 字符串

import json

# 创建一个 Python 字典
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 将 Python 字典转换为 JSON 字符串
json_string = json.dumps(data)

# 输出 JSON 字符串
print(json_string)


