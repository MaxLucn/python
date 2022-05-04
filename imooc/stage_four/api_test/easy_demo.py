import requests

# 1、组装请求
url = " http://django.t.mukewang.com/api/sight/sight/list/ "
param = {'is_hot': 1}
# 2、发送请求，获取请求
result = requests.get(url=url, params=param)

# 3、解析响应
print(result.status_code)
