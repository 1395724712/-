#coding="utf-8"
import urllib.request
import re

# 获取数据

# data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")

#设置报头
header=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')

# 为其创建报头
opener=urllib.request.build_opener()
# 添加报头
opener.addheaders=[header]

#读取数据
data=opener.open("https://read.douban.com/provider/all").read().decode("utf-8")


#正则项
pat="<div class=\"name\">(.*?)</div>"

# 全局匹配函数
res=re.compile(pat).findall(data)

#将数据写入文件中
with open("出版社名称.txt","w") as fp:
    for i in res:
        fp.write(i)
        fp.write("\t")
        print(i)
        print("\n")