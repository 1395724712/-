# coding=utf-8
import xlrd
import xlwt


# 读取文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh


# 获取单独的sheet表
def getsheet(fh):
    return fh.sheets()


# 这是获取行数
def getnrows(fh,sheet_num):
    # table单独的sheet表
    table=fh.sheets()[sheet_num]
    return table.nrows

# 这是获取列数
def getncols(fh,sheet):
    table=fh.sheet()[sheet]
    return table.ncols


# 这是获取sheet的个数
# 这里有没有更简单的方法
def get_sheet_num(fh):
    x=0
    # for sheet in getsheet(fh):
    #     x+=1
    x=len(fh.sheets())
    return x


# 读取文件的内容并返回行内容
def get_file(file,sheet_num):
    fp=open_xls(file)
    table=fp.sheets()[sheet_num]
    rows=table.nrows
    data_value=[]
    for row in range(rows):
        data = table.row_values(row)
        data_value.append(data)
    return data_value


if __name__ =="__main__":
    files=["E:\\homework_1\\excel_1.xlsx","E:\\homework_1\\excel_2.xls"]
    # files=["E:\\homework_1\\excel_1.xlsx"]
    # data_value=[]
    dataValue=[]
    for file in files:
        fh=open_xls(file)
        sheet_num=get_sheet_num(fh)
        for num in range(sheet_num):
            print("正在读取第"+str(file)+"的第"+str(num+1)+"张sheet表")
            # data_value=get_file(file,num)
            dataValue=dataValue+get_file(file,num)

    # 新建excel文件
    newFile="excel.xls"
    # 这个重写是不允许操作已打开的文件的
    # 确实是重写
    workbook=xlwt.Workbook(newFile)
    # 创建一个sheet对象
    worksheet=workbook.add_sheet("newsheet_2")
    for i in range(len(dataValue)):
        for j in range(len(dataValue[i])):
            worksheet.write(i,j,dataValue[i][j])
    workbook.save(newFile)
    print("合并完成")
