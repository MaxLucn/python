# 爬靖远四中官网<a>标签里的东西
from bs4 import BeautifulSoup
import requests


google = requests.get('https://jyszh.30edu.com.cn/').content

soup = BeautifulSoup(google, 'html.parser')

links = soup.findAll('a')

for link in links:
    print(link.string)