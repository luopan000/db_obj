import pymysql


class Db:
    def __init__(self):
        self.conn = pymysql.connect("127.0.0.1", "root", "root", "phone", charset="utf8")
        self.cursor = self.conn.cursor()

    def phone_add(self,id,brand,model,price,count,version):
        """
        将用户输入的手机信息添加进数据库中
        :return:
        """
        sql = 'insert into phone (id,brand,model,price,count,version) VALUES (%s,%s,%s,%s,%s,%s)'
        # self.cursor.execute(pymysql,(brand,model,price,count,version))
        try:
            # 执行sql插入语句
            self.cursor.execute(sql,(id,brand,model,price,count,version))
            # 提交到数据库执行
            self.conn.commit()
            print("添加成功!")
        except Exception as e:
            print(e)
        self.conn.close()

    def all_info(self):
        sql = 'select * from phone'
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def infobybrand(self,brand):
        # self.brand = brand
        sql = 'SELECT * from phone WHERE brand = "{0}"'.format(brand)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_price(self,obj1,obj2):
        sql = 'update phone set price = "{0}" WHERE id= "{1}" '.format(obj2,obj1)
        self.cursor.execute(sql)
        self.conn.commit()
        print("价格成功修改!")

    def delete(self,obj):
        sql = 'delete from phone WHERE id="{0}"'.format(obj)
        self.cursor.execute(sql)
        self.conn.commit()
        print("删除成功!")




if __name__ == '__main__':
    a = Db()
    b = a.infobybrand("华为")
    print(b)




