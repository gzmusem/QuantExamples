#模块requests示例处理请求异常

import requests

try:
    # 发送 GET 请求
    response = requests.get('https://www.baidu.com/not_found')
    
    # 如果请求失败,抛出异常
    response.raise_for_status()
    
    # 输出响应内容
    print(response.text)
except requests.exceptions.RequestException as e:
    # 输出请求异常信息
    print('请求异常:', e)



