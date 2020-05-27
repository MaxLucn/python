"""
下载 HTML
写正则的规则，找到 img 标签，  找到 src 属性
"""
import re


def test_re_img():
    """ 使用正则表达式找到图片的地址 """
    # 读取HTMl
    with open('img.html', encoding='utf-8') as f:
        my_html = f.read()
        # print(my_html)
        # 准备正则
        p = re.compile(r'<img.+src=\"(.+?)\".+?>')
        # findall 找到图片的列表
        list_img = p.findall(my_html)
        print(len(list_img))
        for i in list_img:
            print(i.replace('&amp;', '&'))
        # TODO 使用 urllib，requests 将图片保存（爬虫部分）


if __name__ == '__main__':
    test_re_img()
