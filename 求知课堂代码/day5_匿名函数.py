import os

from numpy import full
# 38
# test = lambda x,y:x+y

# print(test(2,3))

# jj_hei = 19
# print("可以"if jj_hei>18 else"不可以")

# rs = (lambda x,y:x if x>y else y)(16,12)
# print(rs)

# 39
# def jiecheng(n):
#     result = 1
#     for item in range(1, n + 1):
#         result = result * item
#     return result

# print(jiecheng(10))

# def digui(n):
#     if n == 1:
#         return 1
#     else:
#         return n * digui(n - 1)

# print(digui(4))

# print(digui(5))

# def di_gui(n):
#     print(n, "<===1====>")
#     if n > 0:
#         di_gui(n - 1)
#     print(n, '<===2====>')

# di_gui(5) # 外部调用后打印的结果是？

#模拟实现递归属性结构的遍历

#递归使用文件查询
def findFile(file_path):
    listRs = os.listdir(file_path)  #修找文件夹的地址

    for fileItem in listRs:  #遍历
        full_path = os.path.join(file_path, fileItem)  #获取完整的文件路径
        if os.path.isdir(full_path):  #判断目标文件夹
            findFile(full_path)
        else:
            print(fileItem)
    else:
        return


findFile("D:\\迅雷下载")