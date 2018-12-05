from models.Order import Order
import csv

class OrderRepo:
    def __init__(self):
        self.__order_list = self.get_all_orders()

    def add_order(self, new_order):
        with open("./Data/testorder.csv", "a") as order_file:
            writer = csv.writer(order_file)
            order_file.write(new_order.__repr__()) 
            self.__order_list.append(new_order)

    def remove_order(self, order_to_remove):
        file_path = "./Data/testorder.csv"
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
        order_list = []
        self.largest_ordernr = 0
        with open("./Data/testorder.csv", "r") as order_file:
            reader = csv.DictReader(order_file)
            for line in reader: 
                if int(line["Pontunarnr"]) > self.largest_ordernr:
                    self.largest_ordernr = int(line["Pontunarnr"])
                order = Order(int(line["Pontunarnr"]), line["Bilnr"],\
                tuple(line["Dagsetning"].split("--")), line["Email"],\
                bool(line["Aukatrygging"])) 
                order_list.append(order)
        return order_list

    def get_order(self, email):
        for order in self.__order_list:
            if order.get_customer_email() == email:
                return order
        