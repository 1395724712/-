# coding="utf-8"
# 这个程序用于爬去CSDN的博文并写入txt文件中
# 注意伪装成浏览器
# 将爬取错误的网站报错到另一个txt文件中

import gzip
import urllib.request
import re
import urllib.error

# 首先创建报头
# header=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'),('Accept-encoding', 'gzip')]
header=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
opener=urllib.request.build_opener()
opener.addheaders=header

#将报头安装的全局

# 目标网址
url="https://www.csdn.net/"

# 读取网页
origin_page=opener.open(url).read().decode("utf-8","ignore")

# 正则项
# pat="<a href=(.*?) target=\"_blank\" data-report-click='{"
pat="<a href=\"(.*?)\" target=\"_blank\"\n.*? data-report-click='{"

# 这里为什么不能用re.S,如果使用该项的话会导致它过分跨行，导致取到的表项过大
All_link=re.compile(pat).findall(origin_page)
# print(origin_page)
print(All_link)

# 新建报头
header2=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'),('Accept-encoding', 'gzip')]
opener2=urllib.request.build_opener()
opener2.addheaders=header2


# 打开存储出错信息的文件
fp_err=open("E:/Lesson_result/Error.txt","w")

# 新的正则项
# 标题
pat_1="<title>(.*?)</title>"
# 内容
pat_2="<p>(.*?)</p>"
n=0
# 逐项打开All_link
for i in All_link:
    try:
        child_page_origin = opener2.open(i).read().decode("utf-8")
        child_page=gzip.decompress(child_page_origin).decode("utf-8")
        # child_page.decode("utf-8")
        print(child_page)
    except Exception as error:
        # 如果出错则向错误记录文件输出错误记录
        fp_err.write(i+"\n")
        if hasattr(error,"reason"):
            fp_err.write(error.reason)
        fp_err.write("\n")
    else:
        n=n+1
        print(n)
        # print(child_page)
        Title=re.compile(pat_1).findall(child_page)
        # 如果打开成功，则以博文的题目为文件名，写入文件内容
        # 这个i是避免Title为空的情况
        fp=open("E:/Lesson_result"+str(i)+Title[0],"a")
        content=re.compile(pat_2).findall(child_page)
        for j in content:
            fp.write(j+"\n")
        fp.close()





# 不能忘记关闭文件
fp_err.close()

