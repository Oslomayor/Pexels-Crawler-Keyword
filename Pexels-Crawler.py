# 10:33 AM, Feb 21th, 2018 @ home, Shangyu
# Pexels Crawler
# 按照关键字爬取 Pexels 网站的图片
# https://www.pexels.com/

import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def download_imgs(keyword):
    # 获取当前脚本运行路径
    dir = os.getcwd()
    # 创建文件夹
    if False == os.path.exists(dir + '/img of {keyword}'.format(keyword=keyword)):
        os.mkdir(dir + '/img of {keyword}'.format(keyword=keyword))
    else:
        pass
    url = 'https://www.pexels.com/search/{}'.format(keyword)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
    for count, jpg_src in enumerate(jpg_srcs):
        jpg_src = jpg_src.get('src')
        jpg = requests.get(jpg_src, headers=headers)
        file = open(dir + '/img of {keyword}/{keyword}_{count}.jpg'.format(keyword=keyword, count=count), 'wb')
        file.write(jpg.content)
        file.close()

def main():
    keyword = input('Please input keyword:\n')
    download_imgs(keyword)

if __name__ == '__main__':
    main()
