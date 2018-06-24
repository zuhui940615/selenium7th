import csv
#把读取文件的代码封装成一个方法
class CsvFileManager2:

    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file = open(path,'r')
        #通过csv代码库，读取打开的csv文件，获取到文件中所有的数据集
        data_table = csv.reader(file)
        #for循环nitem每一行 in 在数据集中 data_table表示数据集
        #data_table中有几行数据，我们就会执行几次
        for item in data_table:
            print(item)

            #如果想测试一下这个方法：
if __name__ == '__main__':
    #csvr = CsvFileManager2()
    #csvr.read()
        #如果在方法上面加上classmethod，表示这个方法可以直接用类调用
#如果在方法上写一个lassmethod，就不需要先实例化对象后才能调用
    CsvFileManager2.read()
