from datetime import date
from decimal import Decimal
class Purchase:
    def __init__(self, id = None , id_product = None ,id_acc = None , deal_date = None , sell_price = None):
        #def __init__(self, id = None: int , id_product :int,id_acc : int , deal_date:date, sell_price: Decimal):
        
        self.id = id 
        self.id_product = id_product
        self.id_acc = id_acc
        self.deal_date = deal_date
        self.sell_price = sell_price
    def __str__(self):
        return f" Id : {self.id}, id_product : {self.id}, id_acc : {self.id_acc}, deal_date : {self.deal_date}, sell_price : {self.sell_price}"