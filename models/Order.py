from datetime import timedelta, datetime

class Order:
    def __init__(self, order_no, car_reg_num, pickup_and_return_date,\
    customer_email, bonus_insurance):
        self.__order_no = order_no #gera fall til að gera pöntunarnr
        self.__car_reg_num = car_reg_num
        self.__pickup_and_return_date = pickup_and_return_date 
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

    def number_of_days(self):
        nr_days = (self.get_return_date() - self.get_pickup_date()).days + 1
        return nr_days

    def set_car_reg_num(self, reg_num):
        self.__car_reg_num = reg_num

    def set_customer_email(self, email):
        self.__customer_email = email

    def set_bonus_insurance(self, insurance_bool):
        self.__bonus_insurance = insurance_bool
        
