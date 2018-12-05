from models.Order import Order
import csv

class OrderRepo:
    def __init__(self):
        self.__order_list = self.get_all_orders()

    def add_order(self, new_order):
        with open("./Data/testorder.csv", "a") as order_file:
            writer = csv.writer(order_file)
            writer.writerow(new_order) 
            self.__order_list.append(new_order)

    def remove_order(self, order_to_remove): 
        if order_to_remove in self.__order_list:
            self.__order_list.remove(order_to_remove)
        with open("./Data/testorder.csv", "w") as order_file:
            for order in self.__order_list:
                writer = csv.writer(order_file)
                writer.writerow(order) 

    def get_all_orders(self): 
        order_list = []
        with open("./Data/testorder.csv", "r") as order_file:
            reader = csv.DictReader(order_file)
            for line in reader: 
                order = Order(int(line["Pontunarnr"]), line["Bilnr"],\
                tuple(line["Dagsetning"].split("--")), line["Email"], bool(line["Aukatrygging"])) 
                order_list.append(order)
        return order_list

    def get_order(self, order_to_get):
        pass