#Parte del código es extraído de las clases de Métodos y Atributos de Coding Dojo 
class Usuario:		
    def __init__(self, name, email):
        #Nota: Estos tres son los atributos de instancia
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_depósito(self, amount):	
    	self.balance_cuenta += amount	
    def hacer_retiro(self, amount):
        if self.balance_cuenta >= amount:
            self.balance_cuenta -= amount
        else:
            print(f"You don't have enough money for retry {self.name}")
    
    def mostrar_balance(self):
        print(f"Mr. {self.name} Your balance in the account is  {self.balance_cuenta}")
    

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
pablo = Usuario("Pablo Ferreyros", "pablo@python.com")


guido.hacer_depósito(100)
guido.hacer_depósito(200)
guido.hacer_depósito(300)
guido.hacer_retiro(200)
guido.mostrar_balance()

monty.hacer_depósito(50)
monty.hacer_depósito(100)
monty.hacer_retiro(180)
monty.mostrar_balance()

pablo.hacer_depósito(300)
pablo.hacer_retiro(20)
pablo.hacer_retiro(90)
pablo.hacer_retiro(34)
pablo.mostrar_balance()