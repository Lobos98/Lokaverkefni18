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
        print("{:<8}{:<11}{:<14}{:<12}{:<20}".format(\
        "Nr.", "Frá", "Til", "Bílnúmer", "Viðbótartrygging"))
        list_no = 1
        for order in list_of_orders:
            print("{:<8}".format(list_no) + order.__str__())
            list_no += 1
    
    def clear_screen(self):
        os.system('cls')

    ## Á þetta heima hér?
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

        self.clear_screen()
        print("Birta lausa bíla")
        self.print_divider()
        free_car_list = self.car_service.find_free_cars(\
        pickup_date_string, return_date_string)
        pickup_print = "{}{}.{}{}.{}{}{}{}".format(*pickup_date_string)
        return_print = "{}{}.{}{}.{}{}{}{}".format(*return_date_string)
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
        print("-"*57)
        name = self.error_catch.input_name()
        if not name:
            return self.go_to_menu()
        phone = self.error_catch.input_phone()
        if not phone:
            return self.go_to_menu()
        email = self.error_catch.input_email
        if not email:
            return self.go_to_menu()
        card_number = self.error_catch.input_card()
        if not card_number:
            return self.go_to_menu()
        ssn_check = input("Er viðskiptavinur með kennitölu? (j/n): ")
        if ssn_check:
            ssn = self.error_catch.input_ssn()
            if not ssn:
                return self.go_to_menu()
        
        print("-"*57)
        
        if self.customer_service.add_customer(email, name, card_number, phone, ssn):
            print("Viðskiptavinur {} hefur verið skráður".format(name))
            print("-"*57)
            new_customer = self.customer_service.find_customer(email)
            return new_customer
        else:
            print("Viðskiptavinur með sama netfang er þegar til í kerfinu.")

    def deregister_customer(self):
        self.clear_screen()
        print("Afskrá viðskiptavin")
        self.print_divider()
        cust = self.find_customer_menu()
        email = cust.get_email()
        if cust != False:
            svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(),\
                email))
            self.print_divider()
            if svar.lower() == "j":
                if not self.order_service.find_order(email):
                    self.customer_service.delete_customer(email)
                    print("{} afskráð".format(cust.get_name()))
                else:
                    print("{} er ennþá með pöntun í framtíðinni".format(cust.get_name()))
                    choice = input("Ertu viss að þú viljir afskrá þennan viðskiptavin? (j/n): ")
                    if choice.lower() == "j":
                        self.customer_service.delete_customer(email)
                        print("{} afskráð".format(cust.get_name()))
                    else:
                        print("Hætt var við")
                        self.go_to_menu()
            else:
                print("Hætt við")
        else:
            print("Notandinn fannst ekki")
        self.print_divider()

    def return_car(self):
        """Biður um email pöntunar í input, kallar á ErrorCheck
        og sendir emailið svo í CarService til að skila viðkomandi bíl"""
        self.clear_screen()
        print("Skila bíl")

        order = False
        while order == False:
            email = self.error_catch.input_email()
            order_list = self.order_service.get_customer_orders(email)
            active_orders = self.order_service.get_active_orders(order_list)
            if active_orders == False:
                print("Virk pöntun finnst ekki á þessu netfangi.")
            elif len(active_orders) == 1:
                order = active_orders[0]
            else:
                print("Eftirfarandi pantanir eru virkar á þessu netfangi:")
                self.print_orders(active_orders)
                order_choice = int(input("Veldu pöntun til þess að skila: "))
                order = active_orders[order_choice-1]

        reg_num = self.car_service.return_car(order)
        self.order_service.move_to_past(order.get_order_no())
        self.customer_service.add_old_order(order.get_customer_email(),\
        order.get_order_no())
        print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))
        print("Bílnum {} hefur verið skilað!".format(reg_num))
        print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))
    
    def find_customer_menu(self):
        """
        Býður að leita eftir nafni, kennitölu eða netfangi, kallar í 
        customer_interface föll til að finna vsk vin og skilar Customer object
        """
        self.clear_screen()
        print("Fletta upp viðskiptavin")
        self.print_divider()
        print("Leita eftir:")
        menu_list = ["Nafni", "Netfangi", "Kennitölu"]
        self.print_menu(menu_list)
        self.print_divider()
        choice = input("Val: ")
        if choice == "1":
            return self.customer.find_by_name()
        elif choice == "2":
            return self.customer.find_by_email()
        elif choice == "3":
            return self.customer.find_by_ssn()
        elif choice == "4":
            return self.customer.find_by_phone_no()

    def delete_order(self):
        self.clear_screen()
        print("Bakfæra pöntun")
        print("-"*34)
        email = self.error_catch.input_email
        self.clear_screen()
        print("Bakfæra pöntun")
        list_of_orders = self.order_service.find_order(email)
        print("-"*72)
        self.print_orders(list_of_orders)
        print("-"*72)
        val = self.error_catch.integer_input("Veldu pöntun: ")
        print("-"*72)
        chosen_order = list_of_orders[int(val)-1]
        print("Þessi pöntun hefur verið valin: {}"\
        .format(chosen_order))
        print("-"*72)
        choice = input("Viltu eyða þessari pöntun? (j/n): ")
        print("-"*72)

        if choice == "j":
            self.order_service.delete_order(chosen_order)
            self.car_service.remove_order(chosen_order)
            print("Pöntuninni hefur verið eytt")
            print("-"*34)
        else:
            print("Hætt við")
            print("-"*34)
        return self.go_to_menu()  

    def change_order(self):
        self.clear_screen()
        print("Breyta Pöntun")
        print("-"*(20))
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
        print("-"*(27 + len(cust.get_name())))
        print("Hverju viltu breyta fyrir {}?".format(cust.get_name()))
        print("-"*(27 + len(cust.get_name())))
        menu_list = ["Dagsetningu", "Bíl", "Til baka"]
        self.print_menu(menu_list)
        print("-"*(27 + len(cust.get_name())))
        input_num = input("Val: ")

        self.clear_screen()

        if input_num == "1":
            self.order.change_date(customer)
        
        elif input_num == "2":
            self.order.change_car(customer)
        
        else:
            return self.go_to_menu()
    
    def create_order(self):
        '''
        1. Leita uppi viðskiptavin
        a) fundinn -> búa til nýja pöntun, mm
        b) ófundinn -> skrá nýjan? 
            i. Já, skrá viðskiptavin -> búa til nýja pöntun, mm
            ii. Nei, mm
        '''
        self.clear_screen()
        print("Skrá pöntun")
        self.print_divider(self.SHORT_DIVIDER)

        customer = self.find_customer_menu()
        if not customer:
            self.main_menu()
        else:
            email = customer.get_email()
            
        # print("Skrá pöntun")
        # self.customer.__is_banned(email) # Ef viðskiptavinurinn er bannaður
        # þá er maður sendur aftur í main menu

        if self.customer.is_banned(email):
            print("Þessi notandi er bannaður.")
            self.main_menu()

        pickup_date, return_date, free_cars = self.display_free_cars()
        reg_number = self.error_catch.input_reg_num()
        rented_car = ''
        insurance_price_coeff = 1.5

        while True:
            for car in free_cars:
                if reg_number == car.get_reg_num():
                    rented_car = car
                    break
            if not rented_car:
                print("Vinsamlegast veldu bíl á listanum")
                reg_number = self.error_catch.input_reg_num()
            else:
                break

        time_d = datetime.strptime(return_date, "%d%m%Y")\
        - datetime.strptime(pickup_date, "%d%m%Y")

        self.clear_screen()

        price = time_d.days * rented_car.get_price()
        print("Kostnaður fyrir bílinn {} í {} daga er: {:,d} kr."\
        .format(reg_number, time_d.days, price))
        
        print("Auka trygging kostar 50% af verði bílsins, kostnaður er þá {:,d} kr"\
        .format(round(price*insurance_price_coeff)))
        extra_insurance = input("Má bjóða þér auka tryggingu? (j/n): ")
        if extra_insurance.lower() == "j":
            insurance = "True"
            print("Nýja verðið er {:,d} kr."\
            .format(round(price*insurance_price_coeff)))
        else:
            insurance = "False"

        interim_order = self.order_service.log_order(reg_number,\
        pickup_date, return_date, email, insurance)
        
        rented_car.add_reservation(interim_order)
        #TODO: þetta make_reservation fall er mjög skrýtið...
        self.car_service.refresh_car(rented_car)

        print("Þér hefur tekist að panta bílinn {}".format(reg_number))
    
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
        print("-"*len("Veldu eitt af eftirfarandi"))
        
        self.print_menu(self.__menu_list)
        print("-"*len("Veldu eitt af eftirfarandi"))
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