class Order:
    def __init__(self, order_no, car_reg_num, pickup_and_return_date,\
    customer_email, bonus_insurance):
        self.__order_no = order_no #gera fall til að gera pöntunarnr
        self.__car_reg_num = car_reg_num
        self.__pickup_and_return_date = pickup_and_return_date #gera fall til að reikna fjölda daga
        self.__customer_email = customer_email
        self.__bonus_insurance = bonus_insurance

    def get_order_no(self):
        return self.__order_no

    def get_car_reg_num(self):
        return self.__car_reg_num

    def get_customer_email(self):
        return self.__customer_email
    
    def get_bonus_insurance(self):
        return self.__bonus_insurance

    def get_pickup_date(self):
        return self.__pickup_and_return_date[0]
    
    def get_return_date(self):
        return self.__pickup_and_return_date[1]

    def get_date(self):
        return self.__pickup_and_return_date

    def set_car_reg_num(self):
        pass

    def set_customer_email(self):
        pass

    def set_bonus_insurance(self):
        pass
