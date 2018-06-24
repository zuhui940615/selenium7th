import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件，所以每次也应该关闭该文件

class CsvFileManager3:

    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file = open(path,'r')
        try:#尝试执行以下代码
            data_table = csv.reader(file)
            #a = [2,3,4,5,6]
            #a[6]#这是可能发生数组下标越界
            #如何保证无论程序执行过程中是否报错，都能正常关闭打开的文件


            for item in data_table:
                print(item)
            #方法最后应该添加close()方法
        finally:#finally最终，无论过程是否报错，都会执行以下代码
            file.close()
            print("file.close() method is executed")

#如果想测试一下这个方法：
if __name__ == '__main__':
    #csvr = CsvFileManager2()
    #csvr.read()
        #如果在方法上面加上classmethod，表示这个方法可以直接用类调用
#如果在方法上写一个lassmethod，就不需要先实例化对象后才能调用
    CsvFileManager3.read()
