from  payment import Payment

class  PaymentCash(Payment):
    numeroCuenta = int
    def __init__(self, id, ammount, user, driver, type, numeroCuenta):
        super().__init__(id, ammount, user, driver, type)
        self.numeroCuenta   = numeroCuenta
        
