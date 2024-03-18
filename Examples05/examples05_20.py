#模块requests示例带查询参数进行搜索

import requests

# 设置查询参数
params = {'wd': 'Python'}

# 发送 GET 请求带查询参数
response = requests.get('https://www.baidu.com/s', params=params)

# 输出请求的 URL
print(response.url)

# 输出响应内容
print(response.text)



