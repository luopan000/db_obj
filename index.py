import pymysql
from db import Db

class Phone:

    def __init__(self):
        self.db = Db()
        self.menu = """
                    手机信息管理系统      
                    1.手机录入
                    2.根据手机品牌查询手机信息
                    3.查询全部手机信息
                    4.根据手机编号修改手机价格
                    5.根据手机编号删除手机记录
                    6.退出
                    """

    def show_display(self):
        while True:
            print(self.menu)
            num = input("请输入您的操作:")
            if num=="6":
                break
            if num=="1":
                id = int(input("请输入手机编码:"))
                brand = input("请输入手机品牌:")
                model = input("请输入手机型号:")
                price = float(input("请输入手机价格:"))
                count = int(input("请输入手机数量:"))
                version = input("请输入手机版本:")
                self.db.phone_add(id,brand,model,price,count,version)
            if num =="2":
                obj= input("请输入手机品牌:")
                print(self.db.infobybrand(obj))

            if num== "3":
                print(self.db.all_info())

            if num == "4":
                x = int(input("请输入手机编号:"))
                y = float(input("请输入您想改变的价格:"))
                self.db.update_price(x,y)

            if num =="5":
                x = int(input("请输入手机编号:"))
                self.db.delete(x)

            else:
                print("操作错误!请重新输入!")







if __name__ == '__main__':
    a = Phone()
    a.show_display()
