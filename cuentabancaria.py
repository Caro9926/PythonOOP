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

acc1.hacer_depósito(100).hacer_depósito(200).hacer_depósito(300).hacer_retiro(50).mostrar_balance().generar_interés()
acc2.hacer_depósito(50).hacer_depósito(100).hacer_retiro(180).mostrar_balance().generar_interés()

CuentaBancaria.todos_los_balances()
