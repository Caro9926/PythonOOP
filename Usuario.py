#Parte del código es extraído de las clases de Métodos y Atributos de Coding Dojo 
class CuentaBancaria:
    todas_las_cuentas = []
    def __init__(self, tasa_interés, balance=0):
        
        self.tasa_interés= tasa_interés
        self.balance_cuenta = balance
        self.descuento = 5
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def hacer_depósito(self, amount):	
        self.balance_cuenta += amount	
        return self 
        
    def hacer_retiro(self, amount):
        if self.balance_cuenta >= amount:
            self.balance_cuenta -= amount
        else:
            total0= self.balance_cuenta - self.descuento
            print(f"You don't have enough money for retry, a discount of 5: {total0}")
        return self

    def mostrar_balance(self):
        print(f"Your balance in the account is  {self.balance_cuenta}")
        return self   
  
    def generar_interés(self):
            
            if self.balance_cuenta>=0:
                total= self.balance_cuenta*self.tasa_interés + self.balance_cuenta
                print(f"Your new balance with rate interest is: {total}")
            else: 
                print(f"You don't have enough money to earn interest. Your account balance is: {self.balance_cuenta}")
                return self 

  
    @classmethod
    def todos_los_balances(cls):
                for cuenta in cls.todas_las_cuentas:
                    cuenta.mostrar_balance()
            

          
    

acc1 = CuentaBancaria(tasa_interés=0.05)
acc2 = CuentaBancaria(tasa_interés=0.05)

#CuentaBancaria.todos_los_balances()




class Usuario:		
    def __init__(self, name, email):
        #Nota: Estos tres son los atributos de instancia
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interés=0.02, balance=0)
    
   
    def metodo_deposito(self, amount):	
        self.cuenta.hacer_depósito(amount)
        return self         

    def metodo_retiro(self, amount):
        self.cuenta.hacer_retiro(amount)
        return self

    def metodo_balance(self):
        print(f"Mr.{self.name} your account balance is: ")
        self.cuenta.mostrar_balance()
        return self
        
           




            





