# 10:33 AM, Feb 21th, 2018 @ home, Shangyu
# Pexels Crawler
# 按照关键字爬取 Pexels 网站的图片
# https://www.pexels.com/
# pexels 网站的异步加载比较容易破解
# 在关键词后面加page即可
# 如
# https://www.pexels.com/search/fun/?page=4
# https://www.pexels.com/search/fun/?page=5


import os
import time
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
alljpg_srcs = []

def download_imgs(keyword, pages):
    # 除去首尾空格
    keyword = keyword.strip()
    # 获取当前脚本运行路径
    dir = os.getcwd()
    # 创建文件夹
    if False == os.path.exists(dir + '/img of {keyword}'.format(keyword=keyword)):
        os.mkdir(dir + '/img of {keyword}'.format(keyword=keyword))
    else:
        pass
    for page in range(1,int(pages)+1):
        url = 'https://www.pexels.com/search/{keyword}/?page={page}'.format(keyword=keyword,page=page)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
        print('jpg_srcs')
        print(jpg_srcs)
        for item in jpg_srcs:
            alljpg_srcs.append(item)
        print('alljpg_srcs')
        print(alljpg_srcs)
        time.sleep(1)
    count = 0
    for count, jpg_src in enumerate(alljpg_srcs):
        jpg_src = jpg_src.get('src')
        jpg = requests.get(jpg_src, headers=headers)
        file = open(dir + '/img of {keyword}/{keyword}_{count}.jpg'.format(keyword=keyword, count=count), 'wb')
        file.write(jpg.content)
        file.close()
    if count == 0:
        print('暂时仅支持英文关键词')
    print('共下载{}张图片\n'.format(count) + '已保存在 {}'.format(dir + '\imgs of {keyword}'.format(keyword=keyword)))

def main():
    print('''
            ****************************
            *        图片下载工具       *
            *         版本 V2.0        *
            *          欢迎使用         *
            ****************************''')
    keyword = input('Please input keyword --> ')
    pages = input('Please input pages --> ')
    print('downloading......')
    download_imgs(keyword, pages)
    print('10秒后自动退出......')
    time.sleep(10)

if __name__ == '__main__':
    main()
