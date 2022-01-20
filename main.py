from Usuario import Usuario 

a1= Usuario()
a2= Usuario()

a1.hacer_depósito(1000)
a1.hacer_retiro(200)
a2.hacer_retiro(20)
a1.hacer_retiro(30)


    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        
nibbles.transfer_money(400, adrien)