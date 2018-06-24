#1.要想读取csv文件，首先要导入csv代码库
#这个csv也不用下载，时python内置的代码库
#如果要读取excel需要下载相应的代码库：xlrd
#怎么下载：1.通过命令下载：在dos窗口中，输入pip install -U xlrd
#之前发了一个selenium的离线包，也可以通过命令行在线安装：pip install -U selenium 或者pip3 install selenium
#-U时升级带最新版的意思
#pip时python语言最常用的项目管理工具，和java中的maven类似
#如果你即安装了python2，同时安装了python3，那么可能需要把pip改成pip3
#2.点击file， 点击settings，选择projectInterpreter,，点击加号，搜索需要的代码库，选中并可直接安装
import csv

#2.制定要读取的文件的路径
path=r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
#因为字符串中包含反斜线 \t等，怎么做
#1.每个反斜线前面加一个反斜线
#2.把每一个反斜线都改成正斜线
#相比，第二章方法更好一点，因为java，python都是跨平台语言
#在字符串中，两个反斜线会自动根据转移字符的规则转成一个反斜线
#在windows操作系统中，用反斜线表示目录结构
#但是在linux操作系统中，只有正斜线/才能表示目录
#如果用爽反斜线，那么代码就失去了跨平台能力，因为linux用不了反斜线
#如果用正斜线，代码可以同时在linux和windows中执行
#3.在字符串外面加上一个字母r，会认为中间所有的代码都不存在转义字符
#print(path)
#3.打开路径所对应的文件
file = open(path,'r')
#4.读取文件的内容，通过什么来读取？
#导入的csv代码库一直没用
#reader()方法是专门用来读取文件的
data_table = csv.reader(file)

#打印data_table 中的每一行数据，怎么办？循环
#forr是循环关键字，其中，item代表每一行，每循环一次，tem就代表最新的一行数据
#data_table 表示整个文件中的所有数据
for item in data_table:
    print(item)

    #很多的测试用例可能都需要从excel中读取数据，所以我们应该对这些代码做一个简单的封装，见一个文件叫csvFManager2，把以上代码封装到一个方法中
    #并再建一个文件来读取封装好的方法