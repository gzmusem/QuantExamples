#模块json 示例Python 对象写入 JSON 文件

import json

# 创建一个 Python 字典
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 将 Python 字典写入 JSON 文件
with open("data.json", "w") as file:
    json.dump(data, file)


