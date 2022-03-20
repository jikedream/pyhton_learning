from numpy import byte

#一些常用的数据操作方法
# print(all([]))
# print(all(()))
# print(all((1,0)))
# print(all([1,2,4,0]))
# print(any([0,0,0]))
# print(any([0,0,1]))

#sorted和sort的使用
# li = [2, 45, 15, 36, 88, 4]
# li.sort()
# print("---------排序之前{}".format(li))
# print("---------排序之后{}".format(sorted(li,reverse=True)))

#zip函数
# a = zip([1, 2, 3, 4], ['a', 'b', 'c', "d"])  #zip压缩无法查看其内容
# print(a)
# print(list(a))

# def printBookInfo():
#     '''
#     zip函数的使用
#     '''
#     books = []  #作为容器存储信息
#     id = input("请输入编号(每个项以空格分隔):")
#     bookname = input("请输入书名(每个项以空格分隔):")
#     bookpos = input("请输入位置(每个项以空格分隔):")
#     '''
#      将输入的信息进行split()：拆分字符串。
#      通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
#     '''
#     idList = id.split(' ')
#     nameList = bookname.split(' ')
#     posList = bookpos.split(' ')

#     bookInfo = zip(idList, nameList, posList)
#     for bookItem in bookInfo:
#         '''
#         遍历信息进行存储
#         '''
#         dictInfo = {"编号": bookItem[0], "书名": bookItem[1], "位置": bookItem[2]}
#         books.append(dictInfo)
#     for item in books:
#         print(item)
#     print(books)  #这再一次证明了列表里面可以是任何元素类型

# printBookInfo()

#enumerate()函数
# listobj = ['a', 'b', 'c']
# for index, item in enumerate(listobj, start=1):  #可以自己指定索引开始的位置
#     print(index, item)

# dictObj = {}
# dictObj['name'] = 'zmd'
# dictObj['hobby'] = 'basketball'
# dictObj['pro'] = 'code'

# for item in enumerate(dictObj):
#     print(item)

#创建set
set1 = {1, 15,3,5,4,7}
set2 = {1,2,3,15}


print(set1- set2)