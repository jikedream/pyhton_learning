## 42内置函数-数学运算

```python
round(num,n)#前面是操作的数，后面的n指的是保留几位小数

```

eval(expression [,global[,locals]])

* expression --表达式

* globals -- 变量作用域，全局命名空间，必须是字典对象

* locals --局部命名空间，可以是任何对象
* **返回值**：返回计算结果

## 43类型转换

常见的函数

![pic1](..\pic\pic1)



* chr()数字转字符
* bin()十进制转二进制
* hex()十进制转16进制（嵌入式编程的使用多）
* ord()返回字符的ascll码
* oct()十进制转为8进制
* bytes()返回一个新的“bytes”对象，它是0<=x<256范围内的不可变整数序列，如果不是python内置的数据类型就需要指定编码方式

```python
print(bytes("我喜欢python",encoding='utf-8'))
```



* dit()用于创建字典

## 44序列操作函数

常见序列操作函数

![pic2](../pic/pic2)

* all()用于判断可迭代参数的所有元素是否为TRUE，否则返回False，除了0，空，FALSE外都算TRUE（元组和列表的空除外）
* any()用于判断可迭代参数的所有元素是否全部为False，有一个True就是TRUE，类似于or

## 45序列操作函数二

* sorted()对于所有可迭代对象进行排序操作(**list的sort()只能对list进行排序，直接修改原始对象**)，所以使用sorted进行排序需要带上函数输出，如果直接在里面带上参数reverse=True就会直接改变排序的顺序
* list.reverse函数用于转置列表里面的内容，并不会进行排序
* zip()函数，用来打包，其内部的数据是元组类型的，按照索引存储为一个元组（按照最少的元素个数进行压缩）

```python

def printBookInfo():
    '''
    zip函数的使用
    '''
    books = []  #作为容器存储信息
    id = input("请输入编号(每个项以空格分隔):")
    bookname = input("请输入书名(每个项以空格分隔):")
    bookpos = input("请输入位置(每个项以空格分隔):")
    '''
     将输入的信息进行split()：拆分字符串。
     通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
    '''
    idList = id.split(' ')
    nameList = bookname.split(' ')
    posList = bookpos.split(' ')

    bookInfo = zip(idList, nameList, posList)
    for bookItem in bookInfo:
        '''
        遍历信息进行存储
        '''
        dictInfo = {"编号": bookItem[0], "书名": bookItem[1], "位置": bookItem[2]}
        books.append(dictInfo)
    for item in books:
        print(item)
    print(books)  #这再一次证明了列表里面可以是任何元素类型


printBookInfo()
```

## 46序列操作三

* enumerate()函数用于将数据对象（列表或者元组或者字符串）加上索引，并且自己可以指定索引，（一般在for循环中使用）

```python
enumerate(sequence,[start=0]
#以下是常用的方法
listobj = ['a', 'b', 'c']
for index, item in enumerate(listobj, start=1):  #可以自己指定索引开始的位置
    print(index, item)          	
```

## 47set集合

**set集合是python中的一种数据类型，是一个无序且不重复的元素集合，（不支持索引和切片，但是我发现这玩意会自动排序）**，set同样是使用{}进行创建，但是他不是键值对的模式，



* 添加操作，set.add()
* 清空操作，set.clear()
* 取a,b两个集合中a独有的元素，a - b或者a.difference(b)

![image-20220320164208109](..\pic\pic3)

* 