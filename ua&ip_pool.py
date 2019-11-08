# coding="utf-8"
# 在这里我创建用户代理池和代理ip池以方便我未来的调用
# 同时将其添加为全局
import urllib.request
import random
# 能力有限暂时不考虑解压的问题

header_pool=[("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"),
             ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"),
             ("User-Agent","Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)")]

# 代理ip来自我的chrome_ghelper
ip_pool=["5.180.77.10",
         "58.152.43.180",
         "107.167.22.178"]

# 我希望该部分自动运行

def build_header():
    # 获取任意代理
    cur_ip=random.choice(ip_pool)
    cur_header=random.choice(header_pool)
    print("\n本次的用户代理为： "+str(cur_header)+"\n")
    print("\n本次的代理ip为： "+str(cur_ip)+"\n")
    # 设置报头
    proxy=urllib.request.ProxyHandler({"http":cur_ip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener.addheaders=[cur_header]

    # 安装为全局
    urllib.request.install_opener(opener)


if __name__=="__main__":
    build_header()

    url="https://baidu.com/"

    try:
        origin_page = urllib.request.urlopen(url).read().decode("utf-8")
        # origin_page=urllib.request.urlopen(url).read()
    except Exception as err:
        print(err.__context__)
    else:
        print(origin_page)