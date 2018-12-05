from models.Order import Order
from repositories.OrderRepo import OrderRepo

Order_instance = Order()
Order_repo_instance = OrderRepo()


class OrderService:
    def log_order(self, reg_number, date1, date2, email, extra_insurance):
        self.order_number = Order_repo_instance.largest_ordernr + 1
        joined_date = (date1, date2)
        self.new_order = Order(self.order_number, reg_number, joined_date, \
        email, extra_insurance)
        Order_repo_instance.add_order(self.new_order)

    def change_order(self, email, choice, date1=0, date2=0, reg_number=0):
        order_to_change = Order_instance.get_order(email)
        original_reg_number = order_to_change.get_car_reg_num()
        original_date1 = order_to_change.get_pickup_date()
        original_date2 = order_to_change.get_return_date()
        original_joined_date = (original_date1, original_date2)
        joined_date = (date1, date2)
        order_number = order_to_change.get_order_no
        bonus_insurance = order_to_change.get_bonus_insurance()

        if choice == "1":
            self.changed_order = Order(order_number, original_reg_number, \
            joined_date, email, bonus_insurance)
            Order_repo_instance.add_order(self.changed_order)

        elif choice == "2":
            self.changed_order = Order(order_number,  reg_number, \
            original_joined_date, email, bonus_insurance)
            Order_repo_instance.add_order(self.changed_order)
            

    def find_order(self, email):
        return Order_repo_instance.get_order(email)


    def delete_order(self, order_to_delete):
        Order_repo_instance.remove_order(order_to_delete)
