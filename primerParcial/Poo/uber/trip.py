from route import Route
from account_usser import User
from account_driver import Driver
from car import Car
from payment import Payment


class Trip(Car, Driver, User, Route, Payment):
    idTrip = int
    car = Car("", "", "", "", "", "")
    driver = Driver("", "", "", "", "", "")
    user = User("", "", "", "", "")
    route = Route("", "", "", "")
    payment = Payment("", "", "", "", "")

    def __init__(self, idTrip, driver, car, user, route, payment):
        self.idTrip = idTrip
        self.car = car
        self.driver = driver
        self.user = user
        self.route = route
        self.payment = payment
