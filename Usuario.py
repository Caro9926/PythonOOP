#Parte del código es extraído de las clases de Métodos y Atributos de Coding Dojo 
class Usuario:		
    def __init__(self, name, email):
        #Nota: Estos tres son los atributos de instancia
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_depósito(self, amount):	
        self.balance_cuenta += amount	
        return self 
          

    def hacer_retiro(self, amount):
        if self.balance_cuenta >= amount:
            self.balance_cuenta -= amount
        else:
            print(f"You don't have enough money for retry {self.name}")
        return self

    def mostrar_balance(self):
        print(f"Mr. {self.name} Your balance in the account is  {self.balance_cuenta}")
        return self
           
    

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
pablo = Usuario("Pablo Ferreyros", "pablo@python.com")


guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(300).hacer_retiro(50).mostrar_balance()
monty.hacer_depósito(50).hacer_depósito(100).hacer_retiro(180).mostrar_balance()
pablo.hacer_depósito(300).hacer_retiro(20).hacer_retiro(90).hacer_retiro(34).mostrar_balance()



