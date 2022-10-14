import string


class Category:
    id : int 
    name : string
    def __init__(self , id  = None, name = None):
        self.id = id
        self.name = name
    def __str__(self):
        return f" Id : {self.id} , Name : {self.name}"
