from models.Order import Order
import csv

class OrderRepo:
    def __init__(self):
        self.__order_list = self.get_all_orders()

    def add_order(self):
        with open("./Data/testorder.csv", "a") as order_file:
            writer = csv.writer(order_file)
            writer.writerow() #?? service notar þetta í log order
            #bæta líka við í listann?

    def remove_order(self, order_to_remove):
        if order_to_remove in self.__order_list:
            pass



    def get_all_orders(self): #ath hvernig listinn er prentaður?
        order_list = []
        with open("./Data/testorder.csv", "r") as order_file:
            reader = csv.DictReader(order_file)
            for line in reader: #ath meðhöndlun dagsetninga
                order = Order(line["Pontunarnr"], line["Bilnr"],\
                line["Dagsetning"], line["Email"], line["Aukatrygging"]) 
                order_list.append(order)
        return order_list

    def get_order(self, order_to_get):
        pass