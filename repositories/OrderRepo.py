from models.Order import Order
import csv

class OrderRepo:
    def __init__(self):
        self.__order_list = self.get_all_orders()
        self.__past_order_list = self.get_past_orders()
        self.__filepath = "./Data/futureorders.csv"
        self.__header = "Pontunarnr,Bilnr,Dagsetning,Email,Aukatrygging"

    def add_order(self, new_order):
        '''Tekur við nýjum order object og bætir í skrána og 
        í self.__order_list'''
        with open(self.__filepath, "a") as order_file:
            order_file.write("\n" +  new_order.__repr__()) 
            self.__order_list.append(new_order)

    def remove_order(self, order_to_remove):
        '''Tekur við order object og eyðir úr skrá'''
        for order in self.__order_list:
            if order_to_remove == order:
                self.__order_list.remove(order)

        self.__update_order_file()

    def __update_order_file(self):
        with open(self.__filepath, "w", newline='') as file:
            file.write(self.__header)
            for order in self.__order_list:
                file.write("\n" + order.__repr__())

    def get_all_orders(self): 
        '''Les úr skrá og bætir öllum framtíðarpöntunum í self.__order_list. 
        Skilar lista af framtíðarpöntunum'''
        order_list = []
        self.largest_ordernr = 0
        with open("./Data/futureorders.csv", "r") as order_file:
            reader = csv.DictReader(order_file)
            for line in reader: 
                if int(line["Pontunarnr"]) > self.largest_ordernr:
                    self.largest_ordernr = int(line["Pontunarnr"])
                order = Order(int(line["Pontunarnr"]), line["Bilnr"],\
                tuple(line["Dagsetning"].split("--")), line["Email"],\
                line["Aukatrygging"])
                order_list.append(order)
        return order_list

    def get_order(self, email):
        '''Tekur við emaili og leitar í lista og skilar svo pöntun
        ef pöntun finnst ekki skilar fallið False'''
        found_orders = []
        for order in self.__order_list:
            if email == order.get_customer_email():
                found_orders.append(order)
        if found_orders:
            return found_orders
        return False
        
    def add_to_past_orders(self, old_order): 
        '''Tekur við pöntun og skrifar hana í skrá yfir eldri pantanir'''
        with open("./Data/pastorders.csv", "a") as past_order_file:
            past_order_file.write("\n" +  old_order.__repr__()) 
            self.__past_order_list.append(old_order)

    def get_past_orders(self):
        '''Gerir lista yfir allar eldri pantanir'''
        past_order_list = []
        with open("./Data/pastorders.csv", "r") as past_order_file:
            reader = csv.DictReader(past_order_file)
            for line in reader: 
                order = Order(int(line["Pontunarnr"]), line["Bilnr"],\
                tuple(line["Dagsetning"].split("--")), line["Email"],\
                line["Aukatrygging"])
                past_order_list.append(order)
        return past_order_list