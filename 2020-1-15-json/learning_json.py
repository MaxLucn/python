# import json         # 键是字符串，值可以是任何东西，json看起来有点像是字典，以花括号开头，有对应的键、值
# # name，phone，email在外面，在内部会有对应的键、值       # 在phone这个类型里又有新的"字典"，里面包括类型、号码
# data = '''{
#     "name" : "Chuck",
#     "phone" : {
#       "type" : "intl",
#       "number" : "+1 734 303 4456"
#     },
#     "email" : {
#       "hide" : "yes"
#     }
# }'''
#
# info = json.loads(data)
# print('name:', info["name"])
# print('hide:', info["email"]["hide"])
# print('number:', info["phone"]["number"])


# json.dumps   将json对象编码成json字符串
# import json
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4}]
# json = json.dumps(data)
# print(json)


# json.loads   将已编码的json字符串解码为python对象
# import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4}'
#
# text = json.loads(jsonData)
# print(text)


# demjson 是python的第三方模块库，可用于编码和解码json数据，包含了jsonlint的格式化及校验功能


# encode  将python对象编码成json字符串
# import demjson
#
# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#
# json = demjson.encode(data)
# print(json)


# decode  将已编码的json字符串解码为python对象
# import demjson
# data = '{"a":1,"b":2,"c":3,"d":4}'
#
# text = demjson.decode(data)
# print(text)



# import json
# input = '''[
#      { "id" : "001",
#        "x"  :  "2",
#        "name" : "Chuck"
#       },
#       { "id" : "009",
#        "x" : "7",
#        "name" : " Chuck"
#        }
# ]'''
#
# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name:', item['name'])
#     print('Id:', item['id'])
#     print('Attribute:', item['x'])


# API是关于什么是URL模式，什么是语法的规范、我们应该发送的数据、我们期望返回的数据的语法是什么


# import urllib.request, urllib.parse, urllib.error
# import json
#
# serviceurl = 'http://maps.googleapise.com/maps/api/geocode/json?'
#
# while True:
#     address = input('Enter location')
#     if len(address) < 1:
#         break
#
#     url = serviceurl + urllib.parse.urlencode({'address': address})
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('=== Failure To Retrieve ===')
#         print(data)
#         continue
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["ing"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)



# import urllib.request, urllib.parse, urllib.error
# import twurl
# import json
#
# TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'
#
# while True:
#     print('')
#     acct = input('Enter Twitter Account')
#     if (len(acct) < 1): break
#     url = twurl.augement(TWITTER_URL,
#                          {'screen_name': acct, 'count': '5'})
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read().decode()
#
#     js = json.loads(data)
#     print(json.dumps(js, indent= 4))
#
#     headers = dict(connection.grthaders())
#     print('Remaining', headers['x-rate-limit-remaining'])
#
#     for u in js['users']:
#         print(u['screen_name'])
#         if 'status' not in u:
#               print('Not status found')
#                 continue
#         s = u['status']['text']
#         print('  ', s[:50])

#
# import urllib.request, urllib.parse, urllib.error
# from twurl import augment
# import ssl
#
# # http://apps,twitter.com/
# # Create App and get the four string, put them in hidden.py
#
# print('* Calling Twitter...')
# url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json,',
#               {'screen_name': 'drchuck', 'count': '2'})
# print(url)
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# connection = urllib.request.urlopen(url, context=ctx)
# data = connection.read()
# print(data)


# import json as js
#
# obj = ["glenn", "sally", "jen"]
#
# print(js.dumps(obj))


# 在此作业中，您将编写一个类似于http://www.py4e.com/code3/json2.py的Python程序 。程序将提示您输入URL，使用urllib从该URL读取JSON数据 ，然后解析并从JSON数据中提取注释计数，计算文件中数字的总和，并在下面输入总和：
# import urllib.request
# import json
# count = 0
#
# url = 'http://py4e-data.dr-chuck.net/comments_331833.json'
# # print('retrieving URL. Stand by.')
# uh = urllib.request.urlopen(url)
# data = uh.read()
#
# info = json.loads(data)
# for item in info["comments"]:
#     number = int(item["count"])
#     count += number
#
# print(count)


# 在此作业中，您将编写一个类似于http://www.py4e.com/code3/geojson.py的Python程序 。该程序将提示您输入位置，联系Web服务并检索该Web服务的JSON并解析该数据，然后从JSON 检索第一个 place_id。地点ID是一个文本标识符，可以唯一地标识一个地点（如Google Maps）。
# 请运行程序以查找此位置的place_id：
#
# 达特茅斯
# 确保输入的名称和大小写与上面的完全相同，然后在下面输入place_id和您的Python代码。提示：place_id的前七个字符 是“ ChIJEYl ...”
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)