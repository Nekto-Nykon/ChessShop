from decimal import Decimal
from unicodedata import category
from User import User
import hashlib
from tabulate import tabulate
import mysql.connector
from Category import Category,__init__
import Product
from Purchase import Purchase
from datetime import date


class Db:
    def __init__(self):
        self.db = mysql.connector.connect ( 
        host =  "localhost",
        user = "root",
        password = "Nykonoleg2603@",
        database = "chess_shop")
        self.cursor = self.db.cursor(dictionary=True)
        print(self.db)
        
    

    @staticmethod
    def hash(pwd):
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    

    @staticmethod
    def __fetch_user(res):
        try :
            user = User()
            user.id = res[0]['id']
            user.firstname = res[0]['firstname']
            user.lastname = res[0]["lastname"]
            user.email = res[0]["email"]
            user.password = res[0]["password"]
            user.id_role = res[0]["id_role"]
            user.acc_money = res[0]["acc_money"]
            return user, None
        except IndexError as error:
            return None, error
    @staticmethod
    def __fetch_product_price(res):
        try :
            price : Decimal()
            price = res[0]["price"]
            return price, None
        except IndexError as error:
            return None, error

    def __insert(self, query, param):

        try:
            self.cursor.execute(query, param)
            self.db.commit()
            return self.cursor.lastrowid, None
        except mysql.connector.Error as error:
            return 0, error

    def __update(self, query, param):
        try:
            self.cursor.execute(query, param)
            self.db.commit()
            return None
        except mysql.connector.Error as error:
            return error
    
    def insert_user(self, new_user: User):
        query = "insert into chess_shop.`account`(firstname, lastname, email, password) value (%s, %s, %s, %s)"
        param = (new_user.firstname , new_user.lastname , new_user.email, self.hash(new_user.password))
        return self.__insert(query, param)
    def insert_category(self, new_category : Category):
        query = "insert into chess_shop.`category`(name) value (%s)"
        param = (new_category.name,)
        return self.__insert(query, param)
    def insert_product(self, new_product:Product):
        query = "insert into chess_shop.`product`(name,  price, name_category ) value(%s, %s, %s)"
        param = (new_product.name,  new_product.price, new_product.name_category) 
        return self.__insert(query , param)
    # select
    def select_user(self, email: str, pwd : str):
        query = "select * from chess_shop.`account` where email = %s and password = %s "
        param = (email, self.hash(pwd))
        try:
            self.cursor.execute(query, param)
            res = self.cursor.fetchall()
        except mysql.connector.Error as error:
            return None, error
        return self.__fetch_user(res)
    def select_product_price_by_id(self,id:int):
        query = "select price from chess_shop.`product` where id = %s"
        param = (id,)
        try:
            self.cursor.execute(query,param)
            res = self.cursor.fetchall()
            return self.__fetch_product_price(res)
        except mysql.connector.Error as error:
            return None, error
    def select_all_user(self):
        query = "select * from chess_shop.`account` order by id  "
        try:
            self.cursor.execute( query)
            res = self.cursor.fetchall()
            return res, None 
        except mysql.connector.Error as error:
            print(error)
            return None, error
        
    def select_all_purchase_by_id(self,id : int):
        query = "select * from chess_shop.purchase where id_acc = %s order by id "
        param = (id,)
        try:
            self.cursor.execute(query, param)
            res = self.cursor.fetchall()
            return res, None 
        except mysql.connector.Error as error:
            return 0, error
    
    def select_all_product(self):
        query = "select * from chess_shop.`product` where avail = 1 order by id"
        try:
            self.cursor.execute( query)
            res = self.cursor.fetchall()
            return res,None
        except mysql.connector.Error as error:
            print(error)
            return None, error
    
    def select_all_category(self):
        query = "select * from chess_shop.`category` order by id"
        try:
            self.cursor.execute( query)
            res = self.cursor.fetchall()
            return res, None
        except mysql.connector.Error as error:
            print(error)
            return None, error
    
    def select_all_purchase(self):
        query = "select * from chess_shop.`purchase` order by id "
        try:
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            return res, None 
        except mysql.connector.Error as error:
            print(error)
            return None, error

    #update
    def update_category(self, name:str, new_name:str):
        query = "update chess_shop.category set name = %s where name = %s"
        param = (new_name, name)
        return self.__update(query, param,)
    

    def update_product_name_by_name(self, name:str, new_name:str):
        query = "update chess_shop.`product` set name = %s where name = %s"
        param = (new_name, name)
        return self.__update(query, param,)
    
    def update_product_price_by_id(self, id:int, new_product_price: Decimal):

        query = "update chess_shop.`product` set price = %s where id = %s"
        param = (new_product_price , id)
        return self.__update(query, param,)
    
    def update_product_price_by_name(self, product:Product, new_product:Product):

        query = "update chess_shop.`product` set price = %s where name = %s"
        param = (new_product.price, product.name )
        return self.__update(query, param,)
    
    def update_account_user_role(self,check_email:str, new_id_role):
        query = "update chess_shop.`account` set id_role = %s where email = %s"
        param = (new_id_role,check_email)
        return self.__update(query,param,)
    
    def update_account_money(self, acc:User, new_acc_money:Decimal):
        query = "update chess_shop.`account` set acc_money = %s where email = %s"
        param = (new_acc_money, acc.email,)
        return self.__update(query, param)
    
    def transaction_buy_product(self,id_product:int , id_acc,new_acc_money:Decimal, sell_price : Decimal):
        
        query1 = "insert into chess_shop.`purchase` (id_product, id_acc, deal_date, sell_price) values(%s,%s,%s,%s)"
        param1 = (id_product, id_acc, date.today(), sell_price)
        query2 = "update chess_shop.`account` set acc_money = %s where id = %s"
        param2 = (new_acc_money, id_acc)
        query3 = "update chess_shop.`product` set avail = 0 where id = %s"
        param3 = (id_product,)
       
        try : 
            
            self.cursor.execute(query1,param1)
            
            self.cursor.execute(query2, param2)
            
            self.cursor.execute(query3, param3)
            input ("Print smth pupa")
            self.cursor.execute("commit")
            
        except mysql.connector.Error as error:
            print(error)
            input ("Print smth lupa")
            self.cursor.execute("rollback")
    
    