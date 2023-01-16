from account import Account
from account_usser import User
from account_driver import Driver
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentUber import paymentUber
from route import Route
from trip import Trip
from uberConfort import UberConfort
from uberFlash import UberFlash
from uberPet import UberPET
from uberX import UberX
from uberXL import UberXL

# EMPIEZA LA EJECUCION!!

if __name__ == "__main__":

    print("USUARIOS")
    usuario1 = User(1, "Diego Yanez", 29, "diego_Alex@hotmail.com", 9842739)
    print(vars(usuario1))

    usuario2 = User(2, "Alejandro florex", 29, "askda@gmail.com", 99999999)
    print(vars(usuario2))

    print("CONDUCTORES")
    driver1 = Driver(1, "Pepe Suarez", 36, "pepe@gmail.com",
                     7987987987979879, "Licencia 0011101011")
    print(vars(driver1))

    driver2 = Driver(2, "Pepe Suarez", 36, "pepe@gmail.com",
                     7987987987979879, "Licencia 0011101011")
    print(vars(driver1))

    print("CARROS")
    carro1 = Car("PGA:5543", "Chevrolet Spark", "Gris", 2018, "Matricula 131244143", Driver(
        1, "Pepe Suarez", 36, "pepe@gmail.com", 7987987987979879, "Licencia 0011101011"))
    print(vars(carro1))
    print(vars(carro1.driver))

    carro2 = Car("FRG-12341", "Pichirilo", "Rojo", 2019, "Matricula 4238974298492",
                 Driver(2, "Pepe Suarez", 36, "pepe@gmail.com", 7987987987979879, "Licencia 0011101011"))
    print(vars(carro2))
    print(vars(carro2.driver))

    trip = Trip(2, Car("asdasdasd", "Jaimito Cartero", "Masculino", "4854845", "asdasd", Driver(656, "Chevrolet Family", 2018, "adsasd", 324324, "sdadasd")), Driver(3, "Jaimito Cartero", 123132, "sadasd", 49, "TipoB"), User(5, "Alejandro Macias", 548454545,  "Masculino", 20), Route(
        [-0.2138856794545277, -78.51114957623152], [-0.2138856794545277, -78.51114957623152], 40, 10), Payment(1, 20, User(5, "Alejandro Macias", 548454545,  "Masculino", 20), Driver(3, "Jaimito Cartero", 123132, "sadasd", 49, "TipoB"), "18-10-2022"))
    print(vars(trip))
    print(vars(trip.car))
    print(vars(trip.driver))
    print(vars(trip.user))
    print(vars(trip.route))
    print(vars(trip.payment))

    trip1 = Trip(2, Car("asdasdasd", "Jaimito Cartero", "Masculino", "4854845", "asdasd", Driver(656, "Chevrolet Family", 2018, "adsasd", 324324, "sdadasd")), Driver(3, "Jaimito Cartero", 123132, "sadasd", 49, "TipoB"), User(5, "Alejandro Macias", 548454545,  "Masculino", 20), Route(
        [-0.2138856794545277, -78.51114957623152], [-0.2138856794545277, -78.51114957623152], 40, 10), Payment(1, 20, User(5, "Alejandro Macias", 548454545,  "Masculino", 20), Driver(3, "Jaimito Cartero", 123132, "sadasd", 49, "TipoB"), "18-10-2022"))
    print(vars(trip1))
    print(vars(trip1.car))
    print(vars(trip1.driver))
    print(vars(trip1.user))
    print(vars(trip1.route))
    print(vars(trip1.payment))
