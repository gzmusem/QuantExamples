#模块json 示例从 JSON 文件读取数据

import json

# 从 JSON 文件读取数据
with open("data.json", "r") as file:
    data = json.load(file)

# 访问读取的数据
print(data["name"])
print(data["age"])
print(data["city"])


