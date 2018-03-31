# Pexels-Crawler-Keyboard
按照关键字爬取 Pexels 网站的图片

## 使用方法

### 1. 输入关键字

运行程序，输入要下载的图片的关键字

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler.PNG?raw=true)

比方说输入关键词 man

### 2. 等待自动下载

程序根据关键字，自动搜索相关图片下载到本地

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler2.PNG?raw=true)

 ### 3. 下载完成

默认下载14张图片，完成时提示保存路径

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler3.PNG?raw=true)

## 工作原理

本质上是个 Python 图片爬虫程序，按关键词爬取 [Pexels](www.pexels.com) 网站的图片

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler4.PNG?raw=true)

在搜索栏中输入 food，跳出 food 的相关结果，同时观察它的URL变化

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler5.PNG?raw=true)

可以发现，只要在原网址后面加上 /search/food/，即可得到 food 的搜索结果。

于是按照图片爬虫的常规思路，凉一杯茶的功夫，写了个脚本  

## 异步加载破解  
在 Chrome 的 Network 标签中，切换到XHR  
![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler6.PNG?raw=true) 

手动下翻图片同时观察
![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/pexels-crawler7.PNG?raw=true)  
在浏览器中输入 https://www.pexels.com/search/food/?page=3 可以访问相应页面  
于是成功破解异步加载的请求网址  

## To Do

### 1. 中文搜索

寻找翻译API，尝试中文搜索

### 2. 图片数量

Pexels 是个动态网页，所谓动态网页，手动浏览时，鼠标往下翻页时才会加载下面的内容。程序中每次请求只返回14张图片，如何下载更多数量的图片，自定义数量呢？  
V2.0 增加异步加载的破解，理论上可以下载无限量的图片，但受网站的图片库存限制，一般每种关键词最多下几百个页面
### 3. Release

Python 脚本转成 exe 有三种工具， [py2exe](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/), [pyinstaller](http://www.pyinstaller.org/downloads.html), [cxfreeze](https://anthony-tuininga.github.io/cx_Freeze/), py2exe 2008年停更了，pyinstaller 和 cxfreeze 用了最新版本，打包的 exe 都不能工作欸。
