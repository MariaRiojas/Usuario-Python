class Usuario:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_deposito(self, amount):
        self.amount += amount

    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def hacer_retiro(self,amount):
        self.amount -= amount

    def transferir_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance_usuario()
        user.mostrar_balance_usuario()

maria = Usuario("Maria")
sofia = Usuario("Sofia")
naomi = Usuario("Naomi")

maria.hacer_deposito(300)
maria.hacer_deposito(400)
maria.hacer_deposito(20)
maria.hacer_retiro(25)
maria.mostrar_balance_usuario()

sofia.hacer_deposito(980)
sofia.hacer_deposito(900)
sofia.hacer_retiro(300)
sofia.hacer_retiro(200)
sofia.mostrar_balance_usuario()

naomi.hacer_deposito(2000)
naomi.hacer_retiro(800)
naomi.hacer_retiro(200)
naomi.hacer_retiro(60)
naomi.mostrar_balance_usuario()

sofia.transferir_dinero(40, naomi)