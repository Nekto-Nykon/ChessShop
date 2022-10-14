from decimal import Decimal

class User:
    id: int
    firstname: str
    lastname: str
    email: str
    password: str
    id_role : int
    acc_money: Decimal 
    def __init__(self, firstname="Pupa", lastname="Lupa", email=None, password=None, id_role = 1 , acc_money = Decimal(0.00)):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.acc_money = acc_money
        self.id_role = id_role

    def __str__(self):
        return f"Acc_id: {self.id}, firstname : {self.firstname}, lastname : {self.lastname},id_role : {self.id_role}, acc_money : {self.acc_money}"

