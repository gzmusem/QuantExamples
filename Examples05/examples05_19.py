#模块requests示例获取百度首页内容

import requests

# 发送 GET 请求
response = requests.get('https://www.baidu.com')

# 检查请求是否成功
if response.status_code == 200:
    # 输出响应内容
    print(response.text)
else:
    print('请求失败:', response.status_code)



