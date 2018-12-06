from models.Order import Order
from repositories.OrderRepo import OrderRepo


class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepo()

    def log_order(self, reg_number, date1, date2, email, extra_insurance):
        '''Tekur inn bílnr, leigudags, skiladags, email og aukatryggingu(0/1)
        og býr til pöntun og bætir í skrána'''
        self.order_number = self.__order_repo.largest_ordernr + 1
        joined_date = (date1, date2)
        self.new_order = Order(self.order_number, reg_number, joined_date, \
        email, extra_insurance)
        self.__order_repo.add_order(self.new_order)

    def change_order(self, email, choice, date1=0, date2=0, reg_number=0):
        '''Tekur inn email, valkost um hverju á að breyta
        og svo nýja gildið sem á að breyta yfir í(dagsetningu eða bílnr).
        fjarlægir gömlu pöntunina úr skránni og skrifar hana aftur í hana
        með breyttum gildum'''
        order_to_change = self.__order_repo.get_order(email)
        original_reg_number = order_to_change.get_car_reg_num()
        original_date1 = order_to_change.get_pickup_date()
        original_date2 = order_to_change.get_return_date()
        original_joined_date = (original_date1, original_date2)
        joined_date = (date1, date2)
        order_number = order_to_change.get_order_no()
        bonus_insurance = order_to_change.get_bonus_insurance()
        

        if choice == "1":
            self.changed_order = Order(order_number, original_reg_number, \
            joined_date, email, bonus_insurance)
            self.__order_repo.remove_order(order_to_change)
            self.__order_repo.add_order(self.changed_order)

        elif choice == "2":
            changed_order = Order(order_number,  reg_number, \
            original_joined_date, email, bonus_insurance)
            self.__order_repo.remove_order(order_to_change)
            self.__order_repo.add_order(changed_order)
            

    def find_order(self, email):
        '''Tekur inn email á pöntun sem á að finna og kallar 
        á OrderRepo.get_order() til að sækja þá pöntun'''
        return self.__order_repo.get_order(email)


    def delete_order(self, order_to_delete):
        '''Tekur við order object og kallar á OrderRepo.remove_order()
        sem fjarlægir pöntunina úr skránni'''
        self.__order_repo.remove_order(order_to_delete)

    def get_list_of_orders(self):
        '''Sækir lista yfir allar pantanir úr repoinu'''
        return self.__order_repo.get_all_orders()
