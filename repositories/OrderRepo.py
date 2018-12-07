from models.Order import Order
import csv

class OrderRepo:
    def __init__(self):
        self.__order_list = self.get_all_orders()
        self.__past_order_list = self.get_past_orders()
        self.__largest_order =0

    def add_order(self, new_order):
        '''Tekur við nýjum order object og bætir í skrána og 
        í self.__order_list'''
        with open("./Data/futureorders.csv", "a") as order_file:
            order_file.write("\n" +  new_order.__repr__()) 
            self.__order_list.append(new_order)

    def remove_order(self, order_to_remove):
        '''Tekur við order object og eyðir úr skrá'''
        for order in self.__order_list:
            try:
                if(order_to_remove == order):
                    self.__order_list.remove(order)
            except:
                pass
        file_path = "./Data/futureorders.csv"
        file = open(file_path, newline='')
        file_contents = csv.reader(file)
        r_string = ''
        for line in file_contents:
            if line[0] != order_to_remove:
                r_string += ",".join(line) + "\n"
        r_string = r_string.strip("\n")
        file.close()
        file = open(file_path, "w")
        file.write(r_string)
        file.close()

    def get_all_orders(self): 
        '''Les úr skrá og bætir öllum pöntunum í self.__order_list'''
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
        for order in self.__order_list:
            if email == order.get_customer_email():
                return order
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