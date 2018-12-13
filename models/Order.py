from datetime import timedelta, datetime

class Order:
    def __init__(self, order_no, car_reg_num, pickup_and_return_date,\
    customer_email, bonus_insurance):
        self.__order_no = order_no 
        self.__car_reg_num = car_reg_num
        self.__pickup_and_return_date = pickup_and_return_date
        self.__customer_email = customer_email
        self.__bonus_insurance = bonus_insurance
        self.__pickup_date = self.get_pickup_date()
        self.__return_date = self.get_return_date()


    def get_order_no(self):
        """
        Skilar pöntunarnúmeri, sem er int
        """
        return self.__order_no

    def get_car_reg_num(self):
        """
        Skilar bílnúmeri sem streng á forminu "AAX99"
        """
        return self.__car_reg_num

    def get_customer_email(self):
        """
        Skilar netfangi vskvinar sem er skráður fyrir pöntuninni
        """
        return self.__customer_email
    
    def get_bonus_insurance(self):
        """
        Skilar bool gildi eftir því hvort það er
        viðbótartrygging á bílnum eða ekki
        """
        return self.__bonus_insurance

    def get_pickup_date(self):
        """
        Skilar datetime object með upphafsdagsetningu pöntunarinnar
        """
        return self.__pickup_and_return_date[0]
    
    def get_return_date(self):
        """
        Skilar datetime object með skiladagsetningu pöntunarinnar
        """
        return self.__pickup_and_return_date[1]

    def get_date(self):
        """
        Skilar túplu með upphafsdagsetningu og lokadagsetningu
        sem datetime object
        """
        return self.__pickup_and_return_date

    def number_of_days(self):
        """
        Skilar fjölda daga sem pöntunin tekur - ef pöntunin er 03.03-03.03
        er hún einn dagur, 03.03-04.03 þá er hún 2 dagar osfrv
        """
        nr_days = (self.get_return_date() - self.get_pickup_date()).days + 1
        return nr_days

    def set_car_reg_num(self, reg_num):
        """
        Tekur við streng sem á að vera löglegur og skráir í 
        car_reg_num eigindi klasans
    
        """
        self.__car_reg_num = reg_num

    def set_customer_email(self, email):
        """
        Tekur við streng sem á að vera löglegt email og 
        skráir í customer_email eigindi klasans
        """
        self.__customer_email = email

    def set_bonus_insurance(self, insurance_bool):
        """
        Tekur við boolean gildi og setur sem __bonus_insurance eigindi klasans
        """
        self.__bonus_insurance = insurance_bool
        
    def __str__(self):
        pickup_date_string = datetime.strftime(self.__pickup_date, "%d/%b/%y")
        return_date_string = datetime.strftime(self.__return_date, "%d/%b/%y")
        insurance = "Nei"
        if self.__bonus_insurance == True:
            insurance = "Já"
        return "{:<11}{:<14}{:<12}{:<20}".format(pickup_date_string,\
        return_date_string, self.__car_reg_num, insurance)

    def __eq__(self, other):
        """
        Ber saman pöntunarnúmer á tveimur pöntunum og skilar True
         ef það er það sama
        """
        if self.__order_no == other.get_order_no():
            return True
        else:
            False

    def __repr__(self):
        insurance_string = "False"
        if self.__bonus_insurance == True:
            insurance_string = "True"
        return "Order({},{},({},{}),{},{})".format(self.__order_no, \
        self.__car_reg_num, (repr(self.__pickup_date)), \
        repr(self.__return_date), self.__customer_email, insurance_string)
