#coding="utf-8"
with open("E:\\file1.txt","a+") as fp:
    fp.write("古诗")
    print(fp)
    print(fp.read())

print(fp)