from models.Order import Order
from repositories.OrderRepo import OrderRepo
from BusinessLayer.CustomerService import CustomerService
from datetime import datetime, timedelta

class OrderService:
    INSURANCE_COEFFICIENT = 2.5

    def __init__(self):
        self.__order_repo = OrderRepo()
        self.__order_list = self.__order_repo.get_all_orders()

    def log_order(self, reg_number, date1, date2, email, extra_insurance):#TODO: date1 og date2 eru strengir!
        '''Tekur inn bílnr streng, leigudags datetime, skiladags datetime, 
        email streng og aukatryggingu bool, býr til pöntun og bætir í skrána.
        Skilar order objectinu sem var skapað'''
        order_number = self.__order_repo.largest_orderno + 1
        self.__order_repo.next_order_no()
        joined_date = (date1, date2)
        new_order = Order(order_number, reg_number, joined_date, \
        email, extra_insurance)
        self.__order_repo.add_order(new_order)
        return new_order

    def change_email(self, email, order):
        """"
        Tekur inn nýtt netfang og order object, fjarlægir pöntunina úr skránni, 
        breytir emailinu á order objectinu og bætir því aftur í skrána
        """
        self.__order_repo.remove_order(order)
        order.set_customer_email(email)
        self.__order_repo.add_order(order)

    def change_order(self, order, choice, date1=0, date2=0, new_reg_number=0):
        '''Tekur inn email, valkost um hverju á að breyta
        og svo nýja gildið sem á að breyta yfir í(dagsetningu eða bílnr).
        fjarlægir gömlu pöntunina úr skránni og skrifar hana aftur í hana
        með breyttum gildum'''
        
        
        original_reg_number = order.get_car_reg_num()
        original_dates = order.get_date()
        new_dates = (date1, date2)
        email = order.get_customer_email()
        order_number = order.get_order_no()
        bonus_insurance = order.get_bonus_insurance()
        

        if choice == "1":
            changed_order = Order(order_number, original_reg_number, \
            new_dates, email, bonus_insurance)
            self.__order_repo.remove_order(order)
            self.__order_repo.add_order(changed_order)

        elif choice == "2":
            changed_order = Order(order_number,  new_reg_number, \
            original_dates, email, bonus_insurance)
            self.__order_repo.remove_order(order)
            self.__order_repo.add_order(changed_order)
            

    def find_order(self, email):
        '''Tekur inn email á pöntun sem á að finna og kallar 
        á OrderRepo.get_order() til að sækja þá pöntun'''
        return self.__order_repo.get_order(email)


    def delete_order(self, order_to_delete):
        '''Tekur við order object og kallar á OrderRepo.remove_order()
        sem fjarlægir pöntunina úr skránni'''
        self.__order_repo.remove_order(order_to_delete)

    def get_customer_orders(self, email):
        """
        Tekur inn email, skilar lista af pöntunum
        sem eru skráðar á þetta email. Skilar False ef pöntun er ekki
        í skrá
        """
        list_of_orders = self.__order_repo.get_all_orders()
        list_of_orders_for_email = []
        for order in list_of_orders:
            if order.get_customer_email() == email:
                list_of_orders_for_email.append(order)
        if list_of_orders_for_email == []:
            list_of_orders_for_email = False
        return list_of_orders_for_email

    def get_active_orders(self, list_of_orders):
        """
        Tekur við lista af order items og skilar lista af þeim pöntunum á 
        listanum sem eru í gangi núna. Skilar False ef engar pantanir á 
        listanum eru í gangi
        """
        active_orders = []
        for order in list_of_orders:
            pickup_date = order.get_pickup_date()
            return_date = order.get_return_date()
            if pickup_date <= datetime.today() <= return_date:
                active_orders.append(order)
        if active_orders == []:
            return False
        else:
            return active_orders

    def find_order_by_order_no(self, order_no):
        """
        Tekur við pöntunarnúmeri og skilar order object.
        Skilar False ef pöntun finnst ekki
        """
        return self.__order_repo.find_order_by_order_no(order_no)

    def move_to_past(self, order_no):
        '''Tekur inn pöntunarnr, færir pöntun í skrá yfir eldri 
        pantanir, eyðir úr skrá yfir framtíðarpantanir.'''

        old_order = self.find_order_by_order_no(order_no)
        self.__order_repo.add_to_past_orders(old_order)
        self.__order_repo.remove_order(old_order)

    def get_list_of_past_orders(self):
        '''Skilar lista af eldri pöntunum'''
        return self.__order_repo.get_past_orders()

    def car_deleted(self, reg_num):
        """Tekur inn bílnúmer bíls sem er verið að eyða og eyðir öllum
        pöntunum sem eru skráðar á þennan bíl"""
        list_of_orders = self.__order_repo.get_all_orders()
        for order in list_of_orders:
            if order.get_car_reg_num() == reg_num:
                self.delete_order(order)

    def customer_deleted(self, email):
        """"
        Tekur við netfangi vskvinar sem verið er að eyða og eyðir 
        öllum hans pöntunum
        """
        all_orders = self.__order_repo.get_all_orders()
        for order in all_orders:
            if order.get_customer_email() == email:
                self.delete_order(order)
    
    def calculate_price(self, car_price, pickup_date, return_date):
        """Tekur inn dagsetningar"""
        time_d = return_date - pickup_date
        price = (time_d.days + 1) * car_price
        price_insured = round(price*OrderService.INSURANCE_COEFFICIENT)
        return price, price_insured, time_d

    def get_list_of_orders(self):
        '''Sækir lista yfir allar pantanir úr repoinu'''
        return self.__order_repo.get_all_orders()