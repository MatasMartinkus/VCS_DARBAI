# 2 užduotis
#	2.1 Apibrėžkite klasę pavadinimu BankAccount.
#	2.2 Ši klasė turi turėti du atributus: savininkas ir likutis.
#	2.3 Pridėkite metodus deposit ir withdraw, skirtus balansui atnaujinti.
#	2.4 Pridėkite metodą display_balance, skirtą dabartiniam balansui spausdinti.
#	2.5 Sukurkite BankAccount objektą ir išbandykite visus metodus.

class BankAccount:
    def __init__(self, owner:str, balance:int) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, addition: int):
        self.balance += addition

    def withdraw(self, subtraction:int):
        self.balance -= subtraction
    
    def display_balance(self):
        print(self.balance)

account1234 = BankAccount("Matas Martinkus", 100)

account1234.deposit(50)
account1234.withdraw(100)
account1234.display_balance()
