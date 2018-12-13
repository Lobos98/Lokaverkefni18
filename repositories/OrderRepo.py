from models.Order import Order
from datetime import datetime
import csv

class OrderRepo:
    def __init__(self):
        self.largest_orderno = 0
        self.__future_orders_file_path = "./Data/futureorders.csv"
        self.__past_orders_file_path = "./Data/pastorders.csv"
        self.__order_list = self.get_all_orders()
        self.__past_order_list = self.get_past_orders()
        self.__header = "Pontunarnr,Bilnr,Dagsetning,Email,Aukatrygging"

    def add_order(self, new_order):
        '''Tekur við nýjum order object og bætir í framtíðarskrána og 
        í self.__order_list'''
        order_string = self.__get_attribute_string(new_order)
        with open(self.__future_orders_file_path, "a", encoding="utf-8") as order_file:
            order_file.write("\n" +  order_string) 
            self.__order_list.append(new_order)

    def remove_order(self, order_to_remove):
        '''Tekur við order object, fjarlægir úr eigindum 
        reposins og uppfærir framtíðarpantanaskrána'''
        for order in self.__order_list:
            if order_to_remove == order:
                self.__order_list.remove(order)
        self.__update_order_file()

    def __update_order_file(self):
        """
        Skrifar alla future_orders skrána upp á nýtt útfrá 
        order_list eigindi reposins
        """
        with open(self.__future_orders_file_path, "w", newline='', encoding="utf-8") as file:
            file.write(self.__header)
            for order in self.__order_list:
                order_string = self.__get_attribute_string(order)
                file.write("\n" + order_string)

    def get_all_orders(self): 
        '''Les úr skrá og bætir öllum framtíðarpöntunum í self.__order_list.
        Uppfærir largest_orderno eigindi reposins 
        Skilar lista af framtíðarpöntunum'''
        with open(self.__future_orders_file_path, "r", encoding="utf-8") as order_file:
            reader = csv.DictReader(order_file)
            self.__order_list = self.__read_orders_from_file(reader)
            for order in self.__order_list:
                if order.get_order_no() > self.largest_orderno:
                    self.largest_orderno = order.get_order_no()
        return self.__order_list

    def get_order(self, email):
        '''Tekur við emaili sem streng og leitar í lista og skilar svo pöntun
        ef pöntun finnst ekki skilar fallið False'''
        found_orders = []
        for order in self.__order_list:
            if email == order.get_customer_email():
                found_orders.append(order)
        if found_orders:
            return found_orders
        return False
        
    def add_to_past_orders(self, old_order): 
        '''Tekur við pöntun og skrifar hana í skrá yfir eldri pantanir og 
        eigindið past_order_list'''
        with open(self.__past_orders_file_path, "a", encoding="utf-8") as past_order_file:
            old_order_string = self.__get_attribute_string(old_order)
            past_order_file.write("\n" +  old_order_string) 
            self.__past_order_list.append(old_order)

    def get_past_orders(self):
        '''Gerir lista yfir allar eldri pantanir'''
        with open(self.__past_orders_file_path, "r", encoding="utf-8") as past_order_file:
            reader = csv.DictReader(past_order_file)
            self.__past_order_list = self.__read_orders_from_file(reader)
            for order in self.__past_order_list:
                if order.get_order_no() > self.largest_orderno:
                    self.largest_orderno = order.get_order_no()
        return self.__past_order_list
    
    def get_date_string_from_order(self, order):
        """
        Tekur við order object og skilar leigu- og skiladagsetningum 
        sem streng á forminu 01012019--02012019 til þess að skrifa í skrá
        """
        pickup_date, return_date = order.get_date()
        date_string = pickup_date + "--" + return_date
        return date_string

    def __get_attribute_string(self, order):
        """
        Tekur við order object og skilar streng til þess að skrifa í skrána
        """
        order_no = order.get_order_no()
        order_no = str(order_no)
        reg_num = order.get_car_reg_num()
        pickup_return_date_string = self.get_date_string_from_order(order)
        email = order.get_customer_email()
        if order.get_bonus_insurance() == "True":
            bonus_insurance = "True"
        elif order.get_bonus_insurance == "False":
            bonus_insurance = "False"
        attribute_list = [order_no, reg_num, pickup_return_date_string,\
         email, bonus_insurance]
        attribute_string = ",".join(attribute_list)
        return attribute_string

    def __read_dates_from_string(self, date_string):
        """
        tekur við streng á forminu 01012019--02012019 og 
        skilar túplu með tveimur datetime objects
        """
        pickup_date_string, return_date_string = date_string.split("--")
        pickup_date = datetime.strptime(pickup_date_string, "%d%m%Y")
        return_date = datetime.strptime(return_date_string, "%d%m%Y")
        return (pickup_date, return_date)

    def __read_orders_from_file(self, dict_reader):
        """
        Tekur við dictreader object úr csv module, ítrar í gegnum skrána, og 
        skilar lista af orders sem eru í skránni
        """
        order_list = []
        for line in dict_reader:
            order_no = int(line["Pontunarnr"])
            pickup_and_return_dates = \
            self.__read_dates_from_string(line["Dagsetning"])
            if line["Aukatrygging"] == "True":
                bonus_insurance = True
            elif line["Aukatrygging"] == "False":
                bonus_insurance = False
            order = Order(order_no, line["Bilnr"],\
            pickup_and_return_dates, line["Email"],\
            bonus_insurance)
            order_list.append(order)
        return order_list

    def next_order_no(self):
        """"
        Hækkar self.largest_orderno um 1
        """
        self.largest_orderno += 1

    def find_order_by_order_no(self, order_no):
        """
        Tekur við pöntunarnúmeri sem int og skilar viðeigandi order object. 
        Skilar False ef hún finnst ekki.
        """
        for order in self.__order_list:
            if order.get_order_no() == order_no:
                return order
        return False