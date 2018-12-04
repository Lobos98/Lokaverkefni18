

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
            self.__reserved_dates = dict()
        else:
            self.__reserved_dates = reserved_dates
            

a = Car("BX-463", "Jeppi", "Rauður", "1998")

print(a)