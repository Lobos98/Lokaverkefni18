from datetime import datetime, timedelta
from models.Order import Order


class Car:
    def __init__(self, reg_num, type, color, model, broken=False,\
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
            self.__reserved_dates = set()
        else:
            self.__reserved_dates = reserved_dates

    def __repr__(self):
        return "Car({}, {}, {}, {}, {}, {}, {})".format(self.__reg_num,\
        self.__type, self.__color, self.__model, self.__broken,\
        self.__history.__repr__(), self.__reserved_dates.__repr__())

    def __str__(self):
        return "{} er {} {} frá {}".format(self.__reg_num, self.__color,\
        self.__type, self.__model)

    def get_reg_num(self):
        return self.__reg_num

    def get_model(self):
        return self.__model

    def get_type(self):
        return self.__type

    def get_color(self):
        return self.__color
    
    def get_broken(self):
        return self.__broken

    def get_history(self):
        ###Skilar uppflettitöflu þar sem hver lykill er tilgreindur með
        ###tölvupóstfangi og gildi lykilsins er listi af túplum, þar sem
        ###hver túpla inniheldur leigudag og skiladag.
        return self.__history

    def get_reserved_dates(self):
        return self.__reserved_dates

    def change_broken_status(self):
        if self.__broken == True:
            self.__broken = False
        else:
            self.__broken = True
    
    def add_reservation(self, order):
        ###Tekur inn pöntun og skráir allar dagsetningarnar sem bíllinn\
        ###er frátekinn í mengi sem eigindi bílsins
        pickup_date = order.get_pickup_date()
        return_date = order.get_return_date()
        while pickup_date <= return_date:
            self.__reserved_dates.add(pickup_date)
            pickup_date += timedelta(1)
    
    def add_to_history(self, order):
        ###Tekur inn pöntun þegar henni er lokið og bætir henni í\
        ###notkunarsögu bílsins
        renter = order.get_customer_email()
        pickup_date = order.get_pickup_date()
        return_date = order.get_return_date()
        self.__history[renter].append((pickup_date, return_date))
        while pickup_date <= return_date:
            self.__reserved_dates.remove(pickup_date)
            pickup_date += timedelta(1)