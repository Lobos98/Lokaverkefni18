import os
from datetime import datetime, timedelta
from BusinessLayer.ErrorCatch import ErrorCatch
from BusinessLayer.CarService import CarService
from BusinessLayer.OrderService import OrderService
from BusinessLayer.CustomerService import CustomerService
from ui.CustomerInterface import CustomerInterface
from ui.OrderInterface import OrderInterface
from ui.ServiceInterface import ServiceInterface
from ui.VehicleInterface import VehicleInterface

class StaffInterface:
    SPACES_BEFORE_CAR = 7
    SHORT_DIVIDER = 37
    LONG_DIVIDER = 60

    def __init__(self):
        self.car_service = CarService()
        self.order_service = OrderService()
        self.customer_service = CustomerService()
        self.error_catch = ErrorCatch()
        
        self.vehicle = VehicleInterface(self)
        self.customer = CustomerInterface(self)
        self.service = ServiceInterface(self)
        self.order = OrderInterface(self)

        self.__menu_list = ["Viðskiptavinir", "Bílafloti", \
            "Afgreiðsla", "Pantanir", "Hætta"]

    def print_divider(self, num_chars=LONG_DIVIDER):
        """Prentar bandstrik"""
        print(num_chars*"-")

    def print_menu(self, menu_list):
        for index, text in enumerate(menu_list):
            print("{}.  {}".format(index + 1, text))

    def print_orders(self, list_of_orders):
        """
        tekur við lista af Orders og prentar þær með header
        """
        print("{:<8}{:<11}{:<14}{:<12}{:<20}".format(\
        "Nr.", "Frá", "Til", "Bílnúmer", "Viðbótartrygging"))
        self.print_divider(61)
        list_no = 1
        for order in list_of_orders:
            print("{:<8}".format(list_no) + order.__str__())
            list_no += 1
    
    def clear_screen(self):
        os.system('cls')


    def display_free_cars(self, date1='', date2=''):
        """Biður um tvær dagsetningar og prentar þá bíla sem 
        eru lausir yfir allt tímabilið"""
        self.clear_screen()
        print("Birta lausa bíla")
        self.print_divider(self.SHORT_DIVIDER)
        if date1 and date2:
            pickup_date_string = date1
            return_date_string = date2
        else:
            pickup_date_string, return_date_string =\
            self.error_catch.input_rental_dates()
            if pickup_date_string == False or return_date_string == False:
                return False, False, False

        self.clear_screen()
        print("Birta lausa bíla")
        self.print_divider()
        free_car_list = self.car_service.find_free_cars(\
        pickup_date_string, return_date_string)
        try:
            pickup_print = "{}{}.{}{}.{}{}{}{}".format(*pickup_date_string)
            return_print = "{}{}.{}{}.{}{}{}{}".format(*return_date_string)
            pickup_date_string = datetime.strptime(pickup_date_string, "%d%m%Y")
            return_date_string = datetime.strptime(return_date_string, "%d%m%Y")
        except TypeError:
            pickup_print = pickup_date_string.strftime("%d.%m.%Y")
            return_print = return_date_string.strftime("%d.%m.%Y")
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(\
        pickup_print, return_print))
        self.display_list_of_cars(free_car_list)
        return pickup_date_string, return_date_string, free_car_list

    def display_list_of_cars(self, list_of_cars):
        """Tekur við lista af bílum og prentar þá"""
        self.print_divider()
        self.vehicle.print_car_header()
        self.print_divider()
        if list_of_cars:
            for car in list_of_cars:
                print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\

                car.get_reg_num(), car.get_type(), \
                car.get_model(), car.get_color(), \
                str(self.car_service.get_price(car)) + "kr/dag"))
            self.print_divider()
        else:
            print("Engir bílar eru lausir á þessu tímabili")

    def register_customer(self):
        self.clear_screen()
        print("Skrá nýjann viðskiptavin")
        self.print_divider(57)
        name = self.error_catch.input_name()
        if not name:
            return self.go_to_menu()
        phone = self.error_catch.input_phone()
        if not phone:
            return self.go_to_menu()
        email = self.error_catch.input_email()
        if not email:
            return self.go_to_menu()
        card_number = self.error_catch.input_card()
        if not card_number:
            return self.go_to_menu()
        ssn_check = input("Er viðskiptavinur með kennitölu? (j/n): ")
        if ssn_check.lower() == "j":
            ssn = self.error_catch.input_ssn()
            if not ssn:
                return self.go_to_menu()
        else:
            ssn = ""
        
        self.print_divider(57)
        
        if self.customer_service.add_customer(email, name, card_number, phone,\
            ssn):
            print("Viðskiptavinur {} hefur verið skráður".format(name))
            self.print_divider(57)
            new_customer = self.customer_service.find_customer(email = email)
            return new_customer
        else:
            print("Viðskiptavinur með sama netfang er þegar til í kerfinu.")

    def deregister_customer(self):
        self.clear_screen()
        print("Afskrá viðskiptavin")
        self.print_divider()
        cust = self.find_customer_menu()
        email = cust.get_email()
        if cust:
            svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(),\
                email))
            self.print_divider()
            if svar.lower() == "j":
                order_list = self.order_service.get_customer_orders(email)
                if not order_list:
                    self.customer_service.delete_customer(email)
                    print("Viðskiptavinurinn {} hefur verið eytt.".format\
                        (cust.get_name()))
                else:
                    print("{} er með pantaðan bíl hjá okkur".format(cust.\
                        get_name()))
                    choice = input("Ertu viss að þú viljir afskrá þennan "
                        "viðskiptavin? \n"
                    "Athugið að pöntununum verður eytt. (j/n): ")
                    if choice.lower() == "j":
                        self.order_service.customer_deleted(email)
                        for order in order_list:
                            self.car_service.remove_order(order)
                        self.customer_service.delete_customer(email)
                        print("Viðskiptavinur {} er ekki lengur í okkar kerfi."\
                            .format(cust.get_name()))
                    else:
                        print("Hætt var við")
                        self.go_to_menu()
            else:
                print("Hætt við")
                self.go_to_menu()
        else:
            print("Notandinn fannst ekki")
            self.go_to_menu()
        self.print_divider()

    def return_car(self):
        """Biður um email pöntunar í input, kallar á ErrorCheck
        og sendir emailið svo í CarService til að skila viðkomandi bíl
        , það er bara hægt að skila bíl sem er í leigu"""
        self.clear_screen()
        print("Skila bíl")
        self.print_divider()
        order = False
        while bool(order) == False:
            customer = self.find_customer_menu()
            email = customer.get_email()
            if not email:
                return self.go_to_menu()
            order_list = self.order_service.get_customer_orders(email)
            if order_list:
                active_orders = self.order_service.get_active_orders(order_list)
            else:
                active_orders = False

            if active_orders == False:
                print("Virk pöntun finnst ekki á þessu netfangi.")
                choice = input("Viltu reyna aftur? (j/n): ")
                if choice == "j":
                    pass
                else:
                     return self.go_to_menu()
            elif len(active_orders) == 1:
                order = active_orders[0]
            else:
                print("Eftirfarandi pantanir eru virkar á þessu netfangi:")
                self.print_orders(active_orders)
                order_choice = self.error_catch.integer_input("Veldu bíl til "
                    "þess að skila: ", len(active_orders))
                order = active_orders[order_choice-1]

        self.payment_type(order)
        reg_num = self.car_service.return_car(order)
        self.order_service.move_to_past(order.get_order_no())
        self.customer_service.add_old_order(order.get_customer_email(),\
        order.get_order_no())
        self.print_divider(27 + len(reg_num))
        print("Bílnum {} hefur verið skilað!".format(reg_num))
        self.print_divider(27 + len(reg_num))

    def payment_type(self, order):
        self.clear_screen()
        print("Skila bíl")
        self.print_divider()
        menu_list = ["Debit/Kreditkort", "Reiðufé", "Til baka"]
        reg_num = order.get_car_reg_num()
        car = self.car_service.find_car(reg_num)
        if not car:
            print("Það er enginn bíll í útleigu")
        price = self.order_service.calculate_price(self.car_service.\
            get_price(car),order.get_pickup_date(), order.get_return_date())[1]
        print("Veldu tegund greiðslu")
        self.print_divider()
        self.print_menu(menu_list)
        self.print_divider()
        input_num = input("Val: ")
        self.print_divider()
        if input_num in ("1", "2"):
            print("Kostnaður er: {:,d} kr".format(price))
            self.confirm_payment()
        else:
            self.go_to_menu()
            
    def confirm_payment(self):
        confirm = input("Staðfesta greiðslu viðskiptavinar(j/n eða q til að "
            "hætta): ")
        if confirm.lower() == "j":
            print("Greiðslu lokið")
        elif confirm.lower() == "n":
            print("Hætt hefur verið við greiðslu")
            self.go_to_menu()
        else:
            exit()

    def find_customer_menu(self):
        """
        Býður að leita eftir nafni, kennitölu, netfangi eða símanúemeri, 
        kallar í customer_interface föll til að finna vsk vin sem skila
        Customer object eða lista af vskvinum ef leitað er eftir nafni eða snr
        síðasta sem fallið gerir er að kalla í select customer til að velja 
        vskvin ef lista var skilað. Skilar alltaf customer object nema 
        hætt sé við
        """
        self.clear_screen()
        print("Fletta upp viðskiptavin")
        self.print_divider(23)
        print("Leita eftir:")
        self.print_divider(23)
        menu_list = ["Nafni", "Netfangi", "Kennitölu", "Símanúmeri"]
        self.print_menu(menu_list)
        self.print_divider(23)
        choice = input("Val: ")
        if choice == "1":
            customer_list = self.customer.find_by_name()
            print(customer_list)
            return self.customer.select_customer(customer_list)
        elif choice == "2":
            return self.customer.find_by_email()
        elif choice == "3":
            return self.customer.find_by_ssn()
        elif choice == "4":
            customer_list = self.customer.find_by_phone_no()
            return self.customer.select_customer(customer_list)
        self.go_to_menu()

    def delete_order(self):
        self.clear_screen()
        print("Bakfæra pöntun")
        self.print_divider(34)
        found_customer = self.find_customer_menu()
        if not found_customer:
            self.go_to_menu()
        if type(found_customer) == list:
            found_customer = self.customer.select_customer(found_customer)
        self.clear_screen()
        print("Bakfæra pöntun")
        self.print_divider(61)
        list_of_orders = self.order_service.get_customer_orders(found_customer.\
            get_email())
        if not list_of_orders:
            print("Enginn pöntun fannst fyrir {}".format(found_customer.\
                get_name()))
            choice = input("Viltu reyna aftur? (j/n eða q til að hætta): ")
            if choice == "j":
                return self.delete_order()
            elif choice == "n":
                return self.go_to_menu()
            else:
                exit()

        self.print_orders(list_of_orders)
        self.print_divider(61)
        val = self.error_catch.integer_input("Veldu pöntun: ", \
            len(list_of_orders))
        self.print_divider(61)
        chosen_order = list_of_orders[int(val)-1]
        print("Pöntun: {}".format(chosen_order))
        self.print_divider(61)
        choice = input("Viltu eyða þessari pöntun? (j/n): ")
        self.print_divider(61)

        if choice == "j":
            self.order_service.delete_order(chosen_order)
            self.car_service.remove_order(chosen_order)
            print("Pöntuninni hefur verið eytt") 
        else:
            print("Hætt við")
            
        self.print_divider(61)
        return self.go_to_menu()  

    def change_order(self):
        self.clear_screen()
        print("Breyta Pöntun")
        self.print_divider(20)
        customer = self.find_customer_menu()
        if not customer:
            email = self.register_customer()
            customer = self.customer_service.find_customer(email)
        email = customer.get_email()
        self.clear_screen()
        cust = self.customer_service.find_customer(email)
        if not self.order_service.find_order(email):
            print("Enginn pöntun fannst fyrir {}".format(cust.get_name()))
            choice = input("Viltu reyna aftur? (j/n eða q til að hætta): ")
            if choice == "j":
                return self.change_order()
            elif choice == "n":
                return self.go_to_menu()
            else:
                exit()
        print("Breyta Pöntun")
        self.print_divider(27 + len(cust.get_name()))
        print("Hverju viltu breyta fyrir {}?".format(cust.get_name()))
        self.print_divider(27 + len(cust.get_name()))
        menu_list = ["Dagsetningu", "Bíl", "Til baka"]
        self.print_menu(menu_list)
        self.print_divider(27 + len(cust.get_name()))
        input_num = input("Val: ")

        self.clear_screen()

        if input_num == "1":
            self.order.change_date(customer)
        
        elif input_num == "2":
            self.order.change_car(customer)
        
        else:
            return self.go_to_menu()

    def edit_customer(self, customer_found=0 ):
        """Tekur við customer object, leitar að viðskiptavini ef enginn 
        customer er sendur inn. Breytir svo customernum"""
        if customer_found != 0:
            customer = customer_found
        else:
            customer = self.find_customer_menu()
        
        self.clear_screen()
        print("Uppfæra viðskiptavin")
        self.print_divider(57)
        print(customer)
        self.print_divider(57)
        print("Hverju viltu breyta?: ")
        self.print_divider(57)
        menu_list = ["Símanúmeri", "Netfangi", "Kortanúmeri", "Til baka"]
        self.print_menu(menu_list)
        self.print_divider(57)
        val = input("Val: ")
        self.print_divider(57)

        if val == "1":
            self.customer.change_phone_no(customer)
        elif val == "2":
            self.customer.change_email(customer)
        elif val == "3":
            self.customer.change_card_no(customer)
        else:
            return self.go_to_menu()
    
    def create_order(self):
        '''
        Leitar að viðskiptavini, biður um tímabili leigu,
        birtir lausa bíla á gefnu tímabili og tekur við
        bílnúmeri bílsins sem á að leigja.
        Prentar út verð og býður upp á aukatryggingu.
        Stofnar loks pöntun tengda netfangi viðskiptavins
        '''
        self.clear_screen()
        print("Skrá pöntun")
        self.print_divider(StaffInterface.SHORT_DIVIDER)

        customer = self.find_customer_menu()
        if not customer:
            self.main_menu()
        else:
            email = customer.get_email()
            
        print(customer)
        if self.customer.is_banned(email):
            self.print_divider(StaffInterface.LONG_DIVIDER)
            print("Viðskiptavinur er bannaður, ekki er hægt að skrá pöntun")
            self.go_to_menu()

        pickup_date_string, return_date_string, free_cars = self.display_free_cars()
        pickup_date = datetime.strftime(pickup_date_string, "%d%m%Y")
        return_date = datetime.strftime(return_date_string, "%d%m%Y")
        if free_cars == False:
            print("Hætt var við")
            return
        reg_number = self.error_catch.input_reg_num()
        rented_car = ''
        while True:
            for car in free_cars:
                if reg_number == car.get_reg_num():
                    rented_car = car
                    break
            if not rented_car:
                if reg_number == "":
                    self.go_to_menu()
                print("Vinsamlegast veldu bíl á listanum")
                reg_number = self.error_catch.input_reg_num()
            else:
                break
        car_price = rented_car.get_price()
        price, price_insured, time_d = self.order_service.calculate_price\
        (car_price, pickup_date, return_date)

        self.clear_screen()
        print("Skrá pöntun")
        self.print_divider(52)
        print("Kostnaður fyrir bílinn {} í {} daga er: {:,d} kr."\
        .format(reg_number, time_d.days, price))
        print("Auka trygging kostar 150% af verði bílsins,\n"
        "kostnaður er þá {:,d} kr".format(price_insured))
        self.print_divider(52)
        
        extra_insurance = input("Má bjóða þér auka tryggingu? (j/n): ")
        if extra_insurance.lower() == "j":
            insurance = "True"
            print("Nýja verðið er {:,d} kr."\
            .format(price_insured))
        else:
            insurance = "False"
        self.print_divider(52)

        new_order = self.order_service.log_order(reg_number,\
        pickup_date, return_date, email, insurance)
        rented_car.add_reservation(new_order)
        self.car_service.refresh_car(rented_car)
        print("Þér hefur tekist að panta bílinn {}".format(reg_number))
        self.print_divider(52)   

    def start_menu(self):
        """Prentar logo fyrirtækisins og spyr hvort keyra skuli forritið"""
        self.clear_screen()
        print("Velkomin í Bílaleiguna IceCarRentals.")
        self.print_divider(self.SHORT_DIVIDER)

        n = self.SPACES_BEFORE_CAR
        print(r"""{}        _______""".format(" "*n))
        print(r"""{}       //  ||\ \ """.format(" "*n))
        print(r"""{}  ____//___||_\ \__""".format(" "*n))
        print(r"""{} )  _          _    \ """.format(" "*n))
        print(r"""{} |_/ \________/ \___|""".format(" "*n))
        print(r"""{}___\_/________\_/_____""".format(" "*n))
        print(r"""{}Drive cheap, not safe!""".format(" "*n))

        self.print_divider(self.SHORT_DIVIDER)
        answer = input("Keyra forrit? (j/n): ")
        if answer.lower() == "j":
            self.main_menu()
        else:
            exit()

    def main_menu(self):
        """Dregur upp aðalvalmyndina og leyfir okkur að velja milli 
        fjögurra yfirvalmynda"""
        self.clear_screen()
        print("Veldu eitt af eftirfarandi")
        self.print_divider(len("Veldu eitt af eftirfarandi"))
        
        self.print_menu(self.__menu_list)
        self.print_divider(len("Veldu eitt af eftirfarandi"))
        input_num = input("Val: ")
        print()
        if input_num == "1":
            self.customer.menu()
        elif input_num == "2":
            self.vehicle.menu()
        elif input_num == "3":
            self.service.menu()
        elif input_num == "4":
            self.order.menu()
        elif input_num == "5":
            exit()
        else:
            return self.go_to_menu()

    def go_to_menu(self):
        choice = input("Fara aftur á aðalvalmynd? (j/n): ")
        if choice.lower() == "j":
            return self.main_menu()
        else:
            exit()