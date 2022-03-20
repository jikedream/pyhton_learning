from cgi import print_arguments

pro = "计算机主页"


def printInfo():
    print("i dont like teacher")
    print(pro)


def change_global():
    global pro
    pro = "计算机"


change_global()
printInfo()

#37视频

#不可变类型
a = 1


def func(x):
    print("x的地址是{}".format(id(x)))
    x = 2
    print("x的修改之后地址是{}".format(id(x)))
    print(x)

#调用函数

print("a的地址是:{}".format(id(a)))
func(a)
print(a)


'''
我说错了，这里面内部定义的变量就是外部引用的a，
所以不存在内外部变量之分，这里就是给同一个变量
赋了两个值
'''
#可变类型

li = []
def testRenc(parms):
    li.append([1,2,4,5])
    print(id(parms))
    print("内部的{}".format(parms))

print(id(li))
testRenc(li)
print("外部的变量对象{}".format(li))