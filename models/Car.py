from datetime import datetime, timedelta
from models.Order import Order

class Car:
    def __init__(self, reg_num, model, type, color, broken=False,\
    history=None, reserved_dates=None):
        self.__reg_num = reg_num
        self.__type = type
        self.__color = color
        self.__model = model
        self.__broken = broken
        if history == None:
            self.__history = dict()
        else:
            self.__history = history
        if reserved_dates == None:
            self.__reserved_dates = []
        else:
            self.__reserved_dates = reserved_dates
        self.__price_list = {"jeppi":5000, "fólksbíll":4000, "smábíll":3000, \
        "húsbíll":6000, "sportbíll":7000}

    def __repr__(self):
        return "Car({}, {}, {}, {}, {}, {}, {})".format(self.__reg_num,\
        self.__model, self.__type, self.__color, self.__broken,\
        self.__history.__repr__(), self.__reserved_dates.__repr__())

    def __str__(self):
        return "{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
            self.get_reg_num(), self.get_type(), self.get_model(),\
            self.get_color(), str(self.__price_list[self.get_type()]) + "kr/dag")

    def get_reg_num(self):
        """Skilar bílnúmeri sem streng"""
        return self.__reg_num
    
    def get_price(self):
        """Skilar verði pr/dag sem int"""
        return self.__price_list[self.get_type()]

    def get_model(self):
        """Skilar árgerð bíls sem streng"""
        return self.__model

    def get_type(self):
        """Skilar tegund bíls - jeppi, smabill, husbill, 
        sportbill eða folksbill"""
        return self.__type

    def get_color(self):
        """Skilar lit bílsins sem streng"""
        return self.__color
    
    def get_broken(self):
        """Skilar boolean gildi eftir hvort bíllinn er bilaður"""
        return self.__broken

    def get_history(self):
        """Skilar uppflettitöflu þar sem hver lykill er tilgreindur með
        tölvupóstfangi og gildi lykilsins er listi af túplum, þar sem
        hver túpla inniheldur leigudag og skiladag."""
        return self.__history

    def get_reserved_dates(self):
        """Skilar lista af túplum með leigudagsetningu og skiladagsetningu"""
        return self.__reserved_dates

    def change_broken_status(self):
        """Skráir að bíllinn sé bilaður í eigindum"""
        if self.__broken == True:
            self.__broken = False
        else:
            self.__broken = True
    
    def add_reservation(self, order):
        """Tekur inn pöntun og skráir allar dagsetningarnar sem bíllinn
        er frátekinn í eigindi bílsins sem lista af túplum"""
        pickup_date = order.get_pickup_date()
        return_date = order.get_return_date()
        reservation = (pickup_date, return_date)
        self.__reserved_dates.append(reservation)
    
    def add_to_history(self, order):
        """Tekur inn pöntun þegar henni er lokið og bætir henni í
        notkunarsögu bílsins og af-frátekur dagsetningarnar"""
        renter = order.get_customer_email()
        reservation = order.get_date()
        if renter in self.__history:
            self.__history[renter].append(reservation)
        else:
            self.__history[renter] = [reservation]
        self.__reserved_dates.remove(reservation)

    def remove_order(self, order):
        """Tekur við order object og fjarlægir viðeigandi reservations
         úr eigindum bílsins"""
        pickup_date, return_date = order.get_date()
        old_reservation_list = self.get_reserved_dates()
        new_reservation_list = []
        for date_tuple in old_reservation_list:
            if not date_tuple == (pickup_date, return_date):
                new_reservation_list.append(date_tuple)
        self.__reserved_dates = new_reservation_list