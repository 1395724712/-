# coding="utf-8"
# 这一部分的代码用于测试境外的ip是否可以访问境外的网站比如bbc
# 不能！需要框架

import urllib.request
import re
import gzip
# 设置代理ip，我的代理ip来自一个网站（https://whoer.net/zh）的检查效果
ip="5.180.77.10"
proxy=urllib.request.ProxyHandler({"http":ip})

# 创建报头
header=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'),('Accept-encoding', 'gzip')]
# header=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
opener.addheaders=header

# 添加为全局
urllib.request.install_opener(opener)

url_0="https://www.bbc.com/"
url_1="https://baidu.com/"

try:
    origin_page=urllib.request.urlopen(url_1).read()
    # origin_page = urllib.request.urlopen(url_1).read().decode("utf-8")
except Exception as err:
    print(err.__context__)
else:
    # data=gzip.decompress(origin_page).decode("utf-8")
    print(origin_page)