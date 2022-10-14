class Product:
    id : int 
    name : str
    name_category : str 
    price : int 
    def __init__(self, name = None, name_category = None ,price = None):
        self.name = name 
        self.name_category = name_category
        self.price = price
    def __str__(self):
        return f"Id_product : {self.id} , Name : {self.name} , Category : {self.name_category} , Price : {self.price}"