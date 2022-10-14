from unicodedata import category, decimal
from Product import Product
from User import User
from Db import Db
from datetime import date, time
from tabulate import tabulate
from Category import Category
from decimal import Decimal
import os
import re
import getpass


class Interface:
    def __init__(self):
        self.db = Db()
        self.acc = None
        self.clear_console = lambda: os.system('cls')
#проверка воодит ли ползователь числа в меню 
    @staticmethod
    def check_num_input(var):
        i = None
        while i == None:
            try:
                i = int(input(var))
            except ValueError:
                print("Input int value ")
        return i

    @staticmethod
    def input_date():
        i = 0
        while i == 0:

            date_str = str(input("Input date in format dddd-mm-dd"))
            a = re.search("^[0-9]{4}-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$", date_str)
            if a != None:
                return date_str

    def sign_in(self):
        print("Sign in page")
        email = input ("Your email :")
        #pwd = getpass.getpass("Your password : ")
        pwd = input("Your password : ")
        acc, error = self.db.select_user(email, pwd)
        if error is not None:
            print ("Some trouble with your email or password")
            input ("Press button to continue")
            return 
        self.acc = acc  
    def sign_up(self):
        print("Sign up page")
        acc = User()
        acc.firstname = input("Your firstname : ")
        acc.lastname = input("Your lastname : ")
        acc.email = input ("Your email : ")
        acc.password = getpass.getpass("Your password : ")
        acc_id, error = self.db.insert_user(acc)
        if error is not None:
            if error.errno == 1062:
                print ("This email is already taken")
                return 
            print(error)
        else : 
            print("Registration completed successfully ")
            self.acc = acc
        
    def logout(self):
        self.acc = None 
    # menu

    def run(self):
        while True:
            os.system('cls')
            if self.acc is None:
                print ("Guest menu")
                print ("(0) - Sign in ")
                print ("(1) - Sign up ")
                print ("(2) - Show All Category ")
                
                a = self.check_num_input("Input your number")
                if a == 0 :
                    self.sign_in()
                    input ("Print smth")
                elif a == 1:
                    self.sign_up()
                    input ("Print smth")
                elif a == 2:
                    self.show_all_category()
                    input ("Print smth")
                else:
                    print("Some trouble with your input number")
                    time.sleep(3)
                    continue

            else:
                if self.acc.id_role == 1 :
                    self.user_menu()
                elif self.acc.id_role == 2:
                    self.chessExpert_menu()
                elif self.acc.id_role == 3:
                    self.admin_menu()
                else: 
                    print("Some trouble with user role")
                    time.sleep(3)
                    return 
    
    def user_menu(self):
        while True:
            self.clear_console()
            print (" User menu")
            print (" ( 0 ) - Show_All_Category ")
            print (" ( 1 ) - Show_All_Product ")
            print (" ( 2 ) - Buy_Product ")
            print (" ( 3 ) - Replenish_The_Balance")
            print (" ( 4 ) - Log out ")
            print (" ( 5 ) - Show My Purchase")
            
            print (" \n\n\n")
            
            a = self.check_num_input("Input your number")
            if a == 0 :
                self.show_all_category()
                input("Press enter to continue...")
            elif a == 1 :
                self.show_all_product()
                input("Press enter to continue...")
            elif a == 2 :
                self.buy_product()
                input("Press enter to continue...")
            elif a == 3 :
                self.add_money()
                input("Press enter to continue...")
            elif a == 4 :
                self.logout()
                return 
            elif a == 5 : 
                self.show_all_purchase_by_id_user()
                return
            else:
                print(" Input number which is on the menu")
                time.sleep(3)
                continue
            
    def chessExpert_menu(self):
        while True:
            self.clear_console()
            print (" ChessExpert menu")
            print (" ( 0 ) - Show_All_Category ")
            print (" ( 1 ) - Show_All_Product ")
            print (" ( 2 ) - Buy_Product ")
            print (" ( 3 ) - Replenish_The_Balance")
            print (" ( 4 ) - Log out ")
            print (" ( 5 ) - Add_Category")
            print (" ( 6 ) - Add_Product")
            print (" ( 7 ) - Update_Category_by_Id")
            print (" ( 8 ) - Update_Product_by_Id")
            print (" ( 9 ) - Update_Product_by_Name")
            print (" ( 10 ) - Show_My_Purchase")
            print (" \n\n\n")
            
            a = self.check_num_input("Input your number ")
            if a == 0 :
                self.show_all_category()
                input("Press enter to continue...")
            elif a == 1 :
                self.show_all_product()
                input("Press enter to continue...")
            elif a == 2 :
                self.buy_product()
                input("Press enter to continue...")
            elif a == 3 :
                self.add_money()
                input("Press enter to continue...")
            elif a == 4 :
                self.logout()
                return 
            elif a == 5 :
                self.add_category()
                input("Press enter to continue...")
            elif a == 6: 
                self.add_product()
                input("Press enter to continue...")
            elif a == 7 :
                self.update_category()
                input("Press enter to continue...")
            elif a == 8 :
                self.update_product_by_id()
                input("Press enter to continue...")
            elif a == 9 :
                self.update_product_by_name()
                input("Press enter to continue...")
            elif a == 10 : 
                self.show_all_purchase_by_id_user()
                input("Press enter to continue...")
            else:
                print(" Input number which is on the menu")
                time.sleep(3)
                continue
    
    def admin_menu(self):
        while True:
            self.clear_console()
            print (" Admin menu")
            print (" ( 0 ) - Show_All_Category ")
            print (" ( 1 ) - Show_All_Product ")
            print (" ( 2 ) - Buy_Product ")
            print (" ( 3 ) - Replenish_The_Balance")
            print (" ( 4 ) - Log out ")
            print (" ( 5 ) - Add_Category")
            print (" ( 6 ) - Add_Product")
            print (" ( 7 ) - Update_Category_by_name")
            print (" ( 8 ) - Update_Product_by_Id ")
            print (" ( 9 ) - Update_Product_by_Name ")
            print (" ( 10 ) - Updete_User_Role ")
            print (" ( 11 ) - Show_All_User_Acc ")
            print (" ( 12 ) - Show_My_Purchase ")
            print (" \n")
            
            a = self.check_num_input("Input your number")
            if a == 0 :
                self.show_all_category()
                input("Press enter to continue...")
            elif a == 1 :
                self.show_all_product()
                input("Press enter to continue...")
            elif a == 2 :
                self.buy_product()
                input("Press enter to continue...")
            elif a == 3 :
                self.add_money()
                input("Press enter to continue...")
            elif a == 4 :
                self.logout()
                return 
            elif a == 5 :
                self.add_category()
                input("Press enter to continue...")
            elif a == 6: 
                self.add_product()
                input("Press enter to continue...")
            elif a == 7 :
                self.update_category()
                input("Press enter to continue...")
            elif a == 8 :
                self.update_product_by_id()
                input("Press enter to continue...")
            elif a == 9 :
                self.update_product_by_name()
                input("Press enter to continue...")
            elif a == 10 :
                self.update_role()
                input("Press enter to continue...")
            elif a == 11 :
                self.show_all_user_acc()
                input("Press enter to continue...")  
            elif a == 12 :
                self.show_all_purchase_by_id_user()
                input("Press enter to continue...") 
            else:
                print(" Input number which is on the menu")
                input("Press enter to continue...")
                time.sleep(3)
                continue
    
    #select
    def show_all_category(self):
        categorys, error = self.db.select_all_category()
        if error is not None:
            print (error)
            return         
        print(tabulate(categorys, headers= "keys", showindex="always"))
        input(" Input smth to continue  ")
        # have 
    def show_all_product(self):
        products, error = self.db.select_all_product()
        if error is not None:
            print (error)
            return
        print(tabulate(products, headers= "keys", showindex="always")) 
    def show_all_user_acc(self):
        user_accs, error = self.db.select_all_user()
        if error is not None:
            print (error)
            return
        print(tabulate(user_accs, headers= "keys", showindex="always"))
        # have 
    def show_all_purchase(self):
        purchases, error = self.db.select_all_purchase()
        if error is not None:
            print (error)
            return 
        print(tabulate(purchases, headers= "keys", showindex="always"))
    def show_all_purchase_by_id_user(self):
        mypurchases, error = self.db.select_all_purchase_by_id(int(self.acc.id))
        if error is not None: 
            print (error)
            return
        print (tabulate(mypurchases, headers= "keys", showindex="always"))
        input("Input smth to continue :) ...")
        #insert
    def add_category(self):
        print(" Add Category ")
        category = Category()
        category.name = input(" Input new category`s name :  ")
        category_id, error = self.db.insert_category(category)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        elif category_id == 0:
            print ("Category with this name already exist")
            input("Input smth to continue ...")
        else:
            print(" Category insert :) ")
            input("Input smth to continue ...")
    def add_money(self):
        print(" Add_money to my acc ")
        deposit : Decimal
        deposit = Decimal(input ("Input your deposit "))
        old_money : Decimal
        old_money = self.acc.acc_money
        old_money = old_money + deposit
        error = self.db.update_account_money(self.acc,old_money)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        else:
            print(" Money in your acc :) ")
            input("Input smth to continue ...")
    def add_product(self):
        print("Add new Product ")
        new_product = Product()
        new_product.name = input("Input name : ")
        new_product.price = input ("Input product price : ")
        new_product.name_category = input("Input category : ")
        product_id, error = self.db.insert_product(new_product)
        if error is not None:
            print(error)
            input("Input smth to continue ...")

        elif product_id == 0:
            print (" Some trouble ")
            input("Input smth to continue ...")
        else:
            print(" Product insert :) ")
            input(" Input smth to continue ...") 
    def update_category(self):
        print(" Update category ")
        name = input("Input which category you want  to rename : ")
        new_name = input("Input new name to category : ")
        error = self.db.update_category(name, new_name)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        else:
            print(" Category update :) ")
            input("Input smth to continue ...")
    def update_product_by_id(self):
        print(" Update Product by Id ")
        id : int 
        id = self.check_num_input("Input id product ")
        new_price : Decimal
        new_price = input("Input new price ")
        error = self.db.update_product_price_by_id(id , new_price)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        else:
            print(" Price on this product updated :) ")
            input("Input smth to continue ...")
    def update_product_by_name(self):
        print(" Change name of products ")
        name = input("Input name products ")
        new_name = input(" Input new name products ")
        error = self.db.update_product_name_by_name(name , new_name)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        else:
            print(" Name on this products updated :) ")
            input("Input smth to continue ...")
    def update_role(self):
        print(" Update Role by email ")
        email = input("Input acc email : ")
        while True:
            new_role = self.check_num_input(" Input 1 to give role User, 2 - to ChessExpert")
            if (new_role == 1 or new_role == 2):
                break
        error = self.db.update_account_user_role(email, new_role)
        if error is not None:
            print(error)
            input("Input smth to continue ...")
        else:
            print(" Role on this acc updated :) ")
            input("Input smth to continue ...")
    def buy_product(self):
        print ("Buy Product ")
        id_product = self.check_num_input("Input id product which you wsnt to buy : ")
        price, error = self.db.select_product_price_by_id(id_product)
        if error is not None:
            print (error)
            return 
        if (self.acc.acc_money<price):
            print ("Dont enought money")
            input("Input smth to continue :)")
            return 
        
        new_acc_money = Decimal()
        new_acc_money = self.acc.acc_money - price
        self.db.transaction_buy_product(id_product,self.acc.id,new_acc_money,price)
    

        # have 
def main():
    os.system("cls")
    interface = Interface()
    interface.run()
    input (" Print smth ")
main()




    
