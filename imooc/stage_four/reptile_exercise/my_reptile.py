import requests
import re
import os

# 建一个存储爬取下来的音乐文件的文件夹
filename = 'reptile_music\\'
if not os.path.exists(filename):
    os.mkdir(filename)

# 获取爬取对象的 URL
url = "https://y.music.163.com/m/discover/toplist"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

response = requests.get(url=url, headers=headers)

# print(response.text)
# 匹配所有符合条件的爬取对象
html_data = re.findall('"id":(\d+),"songName":"(.*?)"', response.text)
for num_id, title in html_data:
    # 伪装一个浏览器爬取需要的对象
    music_url = f"http://music.163.com/song/media/outer/url?id={num_id}.mp3"
    music_content = requests.get(url=music_url, headers=headers).content
    # 把爬取下来的内容保存到新建的文件夹中
    with open(filename + title + '.mp3', mode='wb') as f:
        # TODO 爬下来的文件不能保存到文件夹中
        f.write(music_content)
    print(num_id, title)

