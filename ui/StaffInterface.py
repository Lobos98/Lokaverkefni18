import os
import datetime
from BusinessLayer.ErrorCatch import ErrorCatch
from BusinessLayer.CarService import CarService
from BusinessLayer.OrderService import OrderService
from BusinessLayer.CustomerService import CustomerService


def clear_screen():
    os.system('cls')


class StaffInterface:
    def __init__(self):
        self.__car_service = CarService()
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__error_catch = ErrorCatch()

    def __print_divider(self):
        print("-"*60)
    
    def start_menu(self):
        clear_screen()
        print("Velkomin í Bílaleiguna IceCarRentals.")
        print("-"*37)
        n = 7
        print("{}        _______".format(" "*n))
        print("{}       //  ||\ \ ".format(" "*n))
        print("{}  ____//___||_\ \__".format(" "*n))
        print("{} )  _          _    \ ".format(" "*n))
        print("{} |_/ \________/ \___|".format(" "*n))
        print("{}___\_/________\_/_____".format(" "*n))
        print("{}Drive cheap, not safe!".format(" "*n))
        print("-"*37)
        answer = input("Keyra forrit? (j/n): ")
        if answer.lower() == "j":
            self.main_menu()
        else:
            exit()

    def main_menu(self):
        clear_screen()
        print("Veldu eitt af eftirfarandi")
        print("-"*len("Veldu eitt af eftirfarandi"))
        print("1.  Viðskiptavinir")
        print("2.  Bílafloti")
        print("3.  Afgreiðsla")
        print("4.  Pantanir")
        print("5.  Hætta")
        print("-"*len("Veldu eitt af eftirfarandi"))
        input_num = input("Val: ")
        print()
        if input_num == "1":
            self.customer_menu()
        elif input_num == "2":
            self.vehicle_menu()
        elif input_num == "3":
            self.service_menu()
        elif input_num == "4":
            self.order_menu()
        elif input_num == "5":
            exit()
        else:
            return self.main_menu()

    def go_to_menu(self):
        choice = input("Fara aftur á aðalvalmynd? (j/n): ")
        if choice.lower() == "j":
            return self.main_menu()
        
    def customer_menu(self):
        clear_screen()
        print("Viðskiptavinir")
        print("-"*27)
        print("1.  Skrá nýjan viðskiptavin")
        print("2.  Fletta upp viðskiptavin")
        print("3.  Afskrá viðskiptavin")
        print("4.  Uppfæra viðskiptavin")
        print("5.  Setja á bannlista")
        print("6.  Taka af bannlista")
        print("7.  Sekta viðskiptavin")
        print("8.  Til baka")
        print("-"*27)
        input_num = input("Val: ")

        if input_num == "1":
            self.register_customer()
        elif input_num == "2":
            self.find_customer()
        elif input_num == "3":
            self.deregister_customer()
        elif input_num == "4":
            self.find_customer()
        elif input_num == "5":
            self.ban_customer()
        elif input_num == "6":
            self.unban_customer()
        elif input_num == "7":
            self.fine_customer()
        else:
            self.main_menu()
    
    def card_input(self):
        card_number = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        while not self.__error_catch.check_card_number(card_number):
            if card_number.lower() == "q":
                 return self.go_to_menu()
            else:
                print("Rangt kortanúmer, reyndu aftur eða 'q' til að hætta")
                card_number = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        return card_number
    
    def phone_input(self):
        phone = input("Símanúmer: ")
        while not self.__error_catch.check_phone_no(phone):
            if phone.lower() == "q":
                return self.go_to_menu()
            else:
                print("Rangt símanúmer, reyndu aftur eða 'q' til að hætta")
                phone = input("Símanúmer: ")
        return phone
    
    def email_input(self):
        email = input("Netfang: ")
        while not self.__error_catch.check_email(email):
            if email.lower() == "q":
                return self.go_to_menu()
            else:
                print("Rangt netfang, reyndu aftur eða 'q' til að hætta")
                email = input("Netfang: ")
        return email
    
    def ssn_checker(self):
        ssn_check = input("Er viðskiptavinur með kennitölu? (j/n): ")
        if ssn_check.lower() == "j":
            ssn = input("Kennitala: ")
            print("-"*52)
            while not self.__error_catch.check_SSN(ssn):
                if ssn_check.lower() == "q":
                    return self.go_to_menu()
                else:
                    print("Kennitala er ógild, reyndu aftur eða 'q' " 
                    "til að hætta")
                    ssn = input("Kennitala: ")
            print("Kennitala er gild")
            return ssn
        else:
            return "0"
    
    def register_customer(self):
        clear_screen()
        print("Skrá nýjann viðskiptavin")
        print("-"*57)
        name = input("Nafn: ")
        phone = self.phone_input()
        email = self.email_input()
        card_number = self.card_input()
        ssn = self.ssn_checker()
        
        print("-"*57)
        self.__customer_service.add_customer(email, name, card_number, phone,\
            ssn)
        print("Viðskiptavinur {} hefur verið skráður".format(name))
        print("-"*57)
        return self.go_to_menu()

    def deregister_customer(self):
        clear_screen()
        print("Afskrá viðskiptavin")
        self.__print_divider()
        cust = self.find_customer()
        email = cust.get_email()
        if cust != False:
            svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(),\
                email))
            self.__print_divider()
            if svar.lower() == "j":
                self.__customer_service.delete_customer(email)
                print("{} afskráð".format(cust.get_name()))
            else:
                print("Hætt við")
        else:
            print("Notandinn fannst ekki")
        self.__print_divider()
        return self.go_to_menu()

    def find_customer(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)
        print("Leita eftir:")
        print("1. Nafni")
        print("2. Netfangi")
        print("3. Til baka")
        print("-"*50)
        choice = input("Val: ")
        if choice == "1":
            return self.find_by_name()
        elif choice == "2":
            return self.find_by_email()
        else:
            return self.go_to_menu()

    def find_by_name(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)
        name = input("Sláðu inn nafn viðskiptavins: ")
        print("-"*(50))
        customer_found_list = self.__customer_service.find_customer_by_name(name)
        if len(customer_found_list) == 1:
            customer_found = customer_found_list[0]
        elif len(customer_found_list) > 1:
            index = 1
            for customer in customer_found_list:
                print("{}. {}".format(index, customer))
            choice = int(input("Veldu einn viðskiptavin hér fyrir ofan: "))
            customer_found = customer_found_list[choice]
        else:
            print("Enginn viðskiptavinur fundinn á þessu nafni")
            pass
        print(customer_found)
        print("-"*(33+len(customer_found.get_name())))
        choice = input("Viltu breyta viðskiptavin? (j/n): ")
        print("-"*(33+len(customer_found.get_name())))
        if choice.lower() == "j":
            self.edit_customer(customer_found)
        else:
            return customer_found

    def find_by_email(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)
        email = self.email_input()
        customer_found = self.__customer_service.find_customer(email)
        if customer_found:
            print(customer_found)
            print("-"*(33+len(email)))
            choice = input("Viltu breyta viðskiptavin? (j/n): ")
            print("-"*(33+len(email)))
            if choice.lower() == "j":
                self.edit_customer(customer_found)
            else:
                return customer_found
        return self.go_to_menu()

    def edit_customer(self, customer):
        clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*(7+len(customer.get_email())))
        print(customer)
        print("-"*(7+len(customer.get_email())))
        print("Hverju viltu breyta?: ")
        print("-"*(7+len(customer.get_email())))
        print("1. Símanúmeri")
        print("2. Netfangi")
        print("3. Kreditkortanúmeri")
        print("4. Til baka")
        print("-"*(7+len(customer.get_email())))
        val = input("Val: ")
        print("-"*(7+len(customer.get_email())))

        if val == "1":
            clear_screen()
            print("Uppfæra viðskiptavin")
            print("-"*30)
            simanr = input("Nýtt Símanúmer: ")
            print("-"*30)
            self.__customer_service.edit_customer_phone_no(customer.\
                get_email(),simanr)
            print("Símanúmeri hefur verið breytt.")
            print("-"*30)
        elif val == "2":
            clear_screen()
            print("Uppfæra viðskiptavin")
            print("-"*40)
            netfang = input("Nýtt netfang: ")
            print("-"*40)
            self.__customer_service.edit_customer_email(customer.get_email(),\
                netfang)
            print("Netfangi hefur verið breytt.")
            print("-"*40)
        elif val == "3":
            clear_screen()
            print("Uppfæra viðskiptavin")
            print("-"*(62))
            kortanumer = card_input()
            print("-"*(62))
            self.__customer_service.edit_customer_card_no(customer.\
                get_email(),kortanumer)
            print("Kortanúmeri hefur verið breytt.")
            print("-"*(62))
        elif val == "4":
            print("-"*(6+len(customer.get_email())))
            return self.go_to_menu()

        return self.go_to_menu()
        

    def ban_customer(self):
        clear_screen()
        print("Setja á bannlista")
        self.__print_divider()
        customer = self.find_customer()
        clear_screen()

        print("Setja á bannlista")
        print("-"*(31 + len(customer.get_name()) + len(customer.get_email())))
        if customer != False:
            stadfesta = input("Setja á bannlista: {}, {}? (j/n): ".\
                format(customer.get_name(), customer.get_email()))
            self.__customer_service.ban_customer(customer.get_email())
            if stadfesta == "j":
                print("{} hefur verið færður á bannlista.".\
                    format(customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fannst ekki")
        return self.go_to_menu()
        
    def unban_customer(self):
        clear_screen()
        print("Taka af bannlista")
        self.__print_divider()
        customer = self.find_customer()
        clear_screen()

        print("Taka af bannlista")
        print("-"*(31 + len(customer.get_name()) + len(customer.get_email())))
        if customer != False:
            stadfesta = input("Taka af bannlista: {}, {}? (j/n): ".\
                format(customer.get_name(), customer.get_email()))
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
            self.__customer_service.unban_customer(customer.get_email())
            if stadfesta == "j":
                print("{} hefur verið tekinn af bannlista.".\
                    format(customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fannst ekki")

        return self.go_to_menu()
        
    def fine_customer(self):
        clear_screen()
        print("Sekta viðskiptavin")
        self.__print_divider()
        customer = self.find_customer()
        clear_screen()

        print("Sekta viðskiptavin")
        if customer != False:
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))
            stadfesta = input("Sekta: {}, {}? (j/n): ".\
                format(customer.get_name(), customer.get_email()))
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))

            if(stadfesta == "j"):
                fine_amount = input("Upphæð sektar (kr): ")
                self.__customer_service.fine_customer(customer.get_email(),\
                    fine_amount)
                print("{} hefur verið sektaður um {} kr.".\
                    format(customer.get_name(), fine_amount))
            else:
                print("Hætt við.") 
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fanns ekki")
        return self.go_to_menu()

    def vehicle_menu(self):
        """Setur bíla-valmyndina í gang"""
        #tilbúið
        clear_screen()
        print("Bílafloti")
        print("-"*len("2.  Birta bíla í útleigu"))
        print("1.  Birta lausa bíla")
        print("2.  Birta bíla í útleigu")
        print("3.  Skila bíl")
        print("4.  Skrá bíl")
        print("5.  Afskrá bíl")
        print("6.  Leita að bíl")
        print("7.  Bilaðir bílar")
        print("8.  Til baka")
        print("-"*len("2.  Birta útleigða bíla"))
        input_num = input("Val: ")
        if input_num == "1":
            self.display_free_cars()
        elif input_num == "2":
            self.display_currently_rented_cars()
        elif input_num == "3":
            self.return_car()
        elif input_num == "4":
            self.add_car()
        elif input_num == "5":
            self.delete_car()
        elif input_num == "6":
            self.print_car()
        elif input_num == "7":
            self.broken_cars()
        else:
            pass
        return self.go_to_menu()

    def print_car_header(self):
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
        "Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))

    def display_free_cars(self, date1='', date2=''):
        """Biður um tvær dagsetningar og prentar þá bíla sem 
        eru lausir yfir allt tímabilið"""
        clear_screen()
        print("Birta lausa bíla")
        print("-"*37)
        if date1 and date2:
            pickup_date_string = date1
            return_date_string = date2
        else:
            pickup_date_string, return_date_string =\
            self.__error_catch.input_rental_dates()

        clear_screen()
        print("Birta lausa bíla")
        print(60*"-")
        free_car_list = self.__car_service.find_free_cars(\
        pickup_date_string, return_date_string)
        pickup_print = "{}{}.{}{}.{}{}{}{}".format(*pickup_date_string)
        return_print = "{}{}.{}{}.{}{}{}{}".format(*return_date_string)
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(\
        pickup_print, return_print))
        print(60*"-")
        self.print_car_header()
        print(60*"-")
        if free_car_list:
            for car in free_car_list:
                print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
                car.get_reg_num(), car.get_type(), car.get_model(), car.get_color(), \
                str(self.__car_service.get_price(car)) + "kr/dag"))
            print(60*"-")
        else:
            print("Engir bílar eru lausir á þessu tímabili")
        return pickup_date_string, return_date_string, free_car_list

        

    def display_currently_rented_cars(self):
        """Sækir lista af bílum sem eru í útleigu 
        í augnablikinu og prentar þá"""
        #tilbúið
        clear_screen()
        print("Eftirfarandi bílar eru í útleigu í augnablikinu")
        print(60*"-")
        self.print_car_header()
        print(60*"-")
        rented_car_list = self.__car_service.get_rented_cars()
        for car in rented_car_list:
            print(car)
        print(60*"-")

    def return_car(self):
        """Biður um email pöntunar í input, kallar á ErrorCheck
        og sendir emailið svo í CarService til að skila viðkomandi bíl"""
        clear_screen()
        print("Skila bíl")

        order = False
        while order == False:
            email = self.__error_catch.input_email()
            order_list = self.__order_service.get_customer_orders(email)
            if order_list == False:
                print("Pöntun finnst ekki á þessu netfangi.")
            elif len(order_list) == 1:
                order = order_list[0]
            else:
                print("Eftirfarandi pantanir eru skráðar á þetta netfang:")
                self.print_orders(order_list)
                order_choice = int(input("Veldu pöntun til þess að skila:"))
                order = order_list[order_choice-1]

        reg_num = self.__car_service.return_car(order)
        self.__order_service.move_to_past(order.get_order_no())
        self.__customer_service.add_old_order(order.get_customer_email(),\
        order.get_order_no())
        print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))
        print("Bílnum {} hefur verið skilað!".format(reg_num))
        print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))

    def add_car(self):
        """Biður um bílnúmer, árgerð, tegund og lit bíls, 
        sendir svo þessar upplýsingar til CarService sem sér um að
        búa til Car object. Prentar staðfestingu"""
        #tilbúið
        clear_screen()
        print("Skrá bíl")
        print("-"*80)
        reg_num = self.__error_catch.input_reg_num()
        model = self.__error_catch.input_model()
        type = self.__error_catch.input_type()
        color = self.__error_catch.input_color()
        self.__car_service.add_car(reg_num, model, type, color)
        print("-"*80)
        print("Bíllinn {} hefur verið skráður!".format(reg_num))
        print("-"*80)

    def delete_car(self):
        """Biður um bílnúmer þangað til bíll fæst sem er til í kerfinu.
        sendir svo bílnúmerið í CarService svo bílnum verði eytt.
        Prentar staðfestingu"""
        #Tilbúið
        clear_screen()

        print("Afskrá bíl")
        print("-"*30)
        car_to_delete = self.__find_car()
        reg_num = car_to_delete.get_reg_num()
        self.__car_service.delete_car(reg_num)
                
        clear_screen()

        print("Afskrá bíl")
        print("-"*(31 + len(reg_num)))
        print("Bíllinn {} hefur verið afskráður!".format(reg_num))
        print("-"*(31 + len(reg_num)))

    def print_car(self):
        """Biður um bílnúmer þangað til bíll finnst og 
        prentar svo bílinn á skjáinn"""
        #tilbúið
        clear_screen()
        print("Leita að bíl")
        print("-"*30)
        car = self.__find_car()
        
        clear_screen()
        print("Leita að bíl")
        print(60*"-")
        self.print_car_header()
        print(60*"-")
        print(car)
        print(60*"-")

    def broken_cars(self):
        """Setur bilaðra-bíla valmyndina í gang"""
        #Tilbúið
        clear_screen()
        print("Bilaðir bílar")
        print("-"*21)
        print("1.  Skrá bilaðan bíl")
        print("2.  Afskrá bilaðan bíl")
        print("3.  Birta bilaða bíla")
        print("4.  Til baka")
        print("-"*21)
        input_num = input("Val: ")

        if input_num == "1":
            self.log_broken_car()
        elif input_num == "2":
            self.log_car_as_fixed()
        elif input_num == "3":
            self.print_broken_cars()
        else:
            pass
        return self.vehicle_menu()

    def log_broken_car(self):
        #TODO: ættum kannski að færa virkni fallsins í CarService...
        clear_screen()
        print("Skrá bilaðan bíl")
        print("-"*30)
        car = self.__find_car()
        reg_num = car.get_reg_num()
        if car.get_broken() == False:
            car.change_broken_status()
            clear_screen()
            print("Skrá bilaðan bíl")
            print("-"*(41 + len(reg_num)))
            print("Bíllinn {} hefur verið skráður sem bilaður."\
            .format(reg_num))
            print("-"*(41 + len(reg_num)))
        else:
            print("Bíllinn {} er þegar bilaður.".format(reg_num))

    def log_car_as_fixed(self):
        #TODO: Ættum kannsk að færa virkni fallsins í CarService...
        clear_screen()
        print("Afskrá bilaðan bíl")
        print("-"*30)
        car = self.__find_car()
        reg_num = car.get_reg_num()
        if car.get_broken() == True:
            car.change_broken_status()
            clear_screen()
            print("Afskrá bilaðan bíl")
            print("-"*(45 + len(reg_num)))
            print("Bíllinn {} hefur verið lagaður og er skráður á ný."\
            .format(reg_num))
            print("-"*(44 + len(reg_num)))
        else:
            print("Bíllinn {} er ekki bilaður.".format(reg_num))

    def print_broken_cars(self):
        # tilbúið
        clear_screen()
        print("Birta bilaða bíla")
        broken_cars = self.__car_service.get_broken_cars()
        print(60*"-")
        self.print_car_header()
        print(60*"-")
        for car in broken_cars:
            print(car)
        print(60*"-")

    def __find_car(self):
        """Biður um bílnúmer þangað til bíll finnst og skilar car object"""
        #Tilbúið
        car = False
        while car == False:
            reg_num = self.__error_catch.input_reg_num()
            car = self.__car_service.find_car(reg_num)
            if car == False:
                print("Bíllinn {} finnst ekki.".format(reg_num.upper()))
        return car

    def service_menu(self):
        clear_screen()
        print("Afgreiðsla")
        print("-"*27)
        print("1.  Birta lausa bíla")
        print("2.  Skrá nýjan viðskiptavin")
        print("3.  Skrá pöntun")
        print("4.  Kostnaðarmat")
        print("5.  Skila bíl")
        print("6.  Afskrá viðskiptavin")
        print("7.  Bakfæra pöntun")
        print("8.  Uppfæra viðskiptavin") 
        print("9.  Breyta pöntun")
        print("10. Til baka")
        print("-"*27)
        input_num = input("Val: ")

        if input_num == "1":
            self.display_free_cars()
        elif input_num == "2":
            self.register_customer()
        elif input_num == "3":
            self.create_order()
        elif input_num == "4":
            self.cost_amount()
        elif input_num == "5":
            self.return_car()
        elif input_num == "6":
            self.deregister_customer()
        elif input_num == "7":
            self.delete_order()
        elif input_num == "8":
            self.find_customer()
        elif input_num == "9":
            self.change_order()
        else:
            self.main_menu()

    def is_banned(self, email):
        if self.__customer_service.find_customer(email):
            if self.__customer_service.find_customer(email)\
            .get_banned() == "true":
                print("Þessi viðskiptavinur er bannaður")
                return self.go_to_menu()

    def create_order(self):
        clear_screen()
        print("Skrá pöntun")
        print("-"*34)
        email = self.__error_catch.input_email()
        self.is_banned(email) # Ef viðskiptavinurinn er bannaður
        # þá er maður sendur aftur í main menu

        pickup_date, return_date, free_cars = self.display_free_cars()
        reg_number = self.__error_catch.input_reg_num()
        rented_car = ''
        insurance_price_coeff = 1.5

        while True:
            for car in free_cars:
                if reg_number == car.get_reg_num():
                    rented_car = car
                    break
            if not rented_car:
                print("Vinsamlegast veldu bíl á listanum")
                reg_number = self.__error_catch.input_reg_num()
            else:
                break

        time_d = datetime.datetime.strptime(return_date, "%d%m%Y")\
        - datetime.datetime.strptime(pickup_date, "%d%m%Y")

        clear_screen()

        price = time_d.days * rented_car.get_price()
        print("Kostnaður fyrir bílinn {} í {} daga er: {:,d} kr."\
        .format(reg_number, time_d.days, price))
        
        print("Athugið að auka trygging kostar 50% af verði bílsins")
        extra_insurance = input("Má bjóða þér auka tryggingu? (j/n): ")
        if extra_insurance.lower() == "j":
            insurance = "True"
            print("Nýja verðið er {:,d} kr."\
            .format(round(price*insurance_price_coeff)))
        else:
            insurance = "False"

        interim_order = self.__order_service.log_order(reg_number, pickup_date, return_date, email, insurance)
        rented_car.add_reservation(interim_order)
        #TODO: þetta make_reservation fall er mjög skrýtið...
        self.__car_service.make_reservation(rented_car)

        print("Þér hefur tekist að panta bílinn {}".format(reg_number))
        return self.go_to_menu()


    def cost_amount(self):
        pickup_date, return_date = self.__error_catch.input_rental_dates()
        car_type_list = ["jeppi", "smabill", "folksbill"]
        car_dict = {"jeppi":5000, "folksbill":4000, "smabill":3000}
        while True:
            try:
                print("1.  Jeppi")
                print("2.  Smábíll")
                print("3.  Fólksbíll")
                car_type = int(input("Veldu tegund bíls: "))
                car = car_type_list[car_type]
            except (IndexError, ValueError):
                print("Vinsamlegast sláðu inn heiltölu á bilinu 1-3.")
            else:
                break
        time_d = datetime.datetime.strptime(return_date, "%d%m%Y")\
        - datetime.datetime.strptime(pickup_date, "%d%m%Y")
        price = (time_d.days + 1) * car_dict[car]
        print("Verð á völdu tímabili: {:,d} kr".format(price))

        choice = input("Viltu leigja bíl? (j/n): ")
        if choice.lower() == "j":
            return self.create_order()
        else:
            return self.go_to_menu()

    def order_menu(self):
        clear_screen()
        print("Pantanir")
        print("-"*21)
        print("1.  Skrá pöntun")
        print("2.  Breyta pöntun")
        print("3.  Fletta upp pöntun")
        print("4.  Bakfæra pöntun")
        print("5.  Prenta allar pantanir")
        print("6.  Til baka")
        print("-"*21)
        input_num = input("Val: ")
        print()
        if input_num == "1":
            self.create_order()
        elif input_num == "2":
            self.change_order()
        elif input_num == "3":
            self.find_order()
        elif input_num == "4":
            self.delete_order()
        elif input_num == "5":
            self.print_orders(self.__order_service.get_list_of_orders())
        else:
            return self.go_to_menu()

    def change_order(self):
        # tilbúið nema vantar núverandi verð 
        # TODO:laga fall þannig að ef fleiri en ein pöntun er á emaili þá velur
        # maður hvaða pöntun á að breyta
        # TODO:passa að þegar pöntun er breytt eyðist upprunalega úr skránni 

        clear_screen()
        print("Breyta Pöntun")
        print("-"*(20))
        email = self.email_input()
        clear_screen()
        cust = self.__customer_service.find_customer(email)
        print("Breyta Pöntun")
        print("-"*(27 + len(cust.get_name())))
        print("Hverju viltu breyta fyrir {}?".format(cust.get_name()))
        print("-"*(27 + len(cust.get_name())))
        print("1. Dagsetningu")
        print("2. Bíl")
        print("3. Til baka")
        print("-"*(27 + len(cust.get_name())))
        input_num = input("Val: ")

        clear_screen()

        if input_num == "1":
            self.change_date(cust, email, input_num)
        
        elif input_num == "2":
            self.change_car(email, input_num)
        
        else:
            return self.go_to_menu()
        
        return self.go_to_menu()


    def change_date(self, cust, email, input_num):
        # TODO: Fjör fyrir kleinar
        print("Breyta Pöntun")
        print("-"*(27 + len(cust.get_name())))
        order_info = self.__order_service.find_order(email)
        print(order_info)
        # print("Núverandi Verð {}")
        print("-"*(27 + len(cust.get_name())))
        pickup_date, return_date = self.__error_catch.input_rental_dates()
        self.__order_service.change_order(email, input_num, pickup_date,\
            return_date)
        print("-"*(27 + len(cust.get_name())))
        print("Dagsetningu hefur verið breytt.")
        print("-"*(27 + len(cust.get_name())))

    def change_car(self, email, input_num):
        # TODO: Fjör fyrir einar.
        print("Breyta Pöntun")
        order_info = self.__order_service.find_order(email)
        ordered_cars = []  
        if order_info:
            for order in enumerate(order_info):
                ordered_cars.append(order[1])
                print("{}. Pöntun á bíl {} frá {} til {}"\
                .format(order[0] + 1,
                order[1].get_car_reg_num(),
                order[1].get_pickup_date(),
                order[1].get_return_date()))
        #TODO passa að viðskiptavinurinn velji tölu á réttu bili
        order_num = self.__error_catch.integer_input(
            "Veldu númer pöntunarinnar til að breyta: ")

        while order_num in range(1, len(ordered_cars) + 1):
            car = ordered_cars[order_num - 1]
            new_car_reg_num = self.__error_catch.input_reg_num()
            old_pickup_date = car.get_pickup_date()
            old_return_date = car.get_return_date()

            if new_car_reg_num:
                break      
            print("Vinsamlegast veldu pöntun á listanum")
            order_num = self.__error_catch.integer_input(
            "Veldu númer pöntunarinnar til að breyta: ")

        free_cars = self.display_free_cars(old_pickup_date,
        old_return_date)[2]

        reg_number = self.__error_catch.input_reg_num()
        free_cars_reg_num = [car.get_reg_num() for car in free_cars]
        while reg_number not in free_cars_reg_num:
            print("Vinsamlegast veldu bíl á listanum")
            reg_number = self.__error_catch.input_reg_num()

        #print("Núverandi bíll: {}".format(order_info.get_car_reg_num()))
        car_to_exchange = self.__error_catch.input_reg_num()

        reg_number = self.__error_catch.input_reg_num()
        free_cars_reg_num = [car.get_reg_num() for car in free_cars]
        while reg_number not in free_cars_reg_num:
            print("Vinsamlegast veldu bíl á listanum")
            reg_number = self.__error_catch.input_reg_num()
        
    def jchange_car(self, email, input_num):
        order_info = self.__order_service.find_order(email)
        if order_info:
            print("Pantanir:", "\n" + "-"*35)
            for order in order_info:
                print("Bíll: {}, Tímabil:{}-{}"\
                .format(
                order.get_car_reg_num(), 
                order.get_pickup_date(),
                order.get_return_date()))

        car_to_exchange = self.__error_catch.input_reg_num()
        for order in order_info:
            if order.get_car_reg_num() == car_to_exchange:
                pickup_date = order.get_pickup_date()
                return_date = order.get_return_date()
                free_cars_list = self.display_free_cars()[2]

        









        self.__order_service.change_order(email, input_num, pickup_date,\
            return_date, reg_number)
            
        print("-"*(20 + len(email)))
        print("Bíllinn {} hefur verið valinn.".format(reg_number))
        print("-"*(20 + len(email)))

    def delete_order(self):
        # tilbúið
        clear_screen()
        print("Bakfæra pöntun")
        print("-"*34)
        email = self.email_input()
        clear_screen()
        print("Bakfæra pöntun")
        order_info = self.__order_service.find_order(email)
        print("-"*72)
        self.print_orders(order_info)
        print("-"*72)
        val = input("Veldu pöntun: ")
        print("-"*72)
        print("Þessi pöntun hefur verið valin: {}".format(order_info[int(val)-1]))
        print("-"*72)
        choice = input("Viltu eyða þessari pöntun? (j/n): ")
        print("-"*72)

        if choice == "j":
            self.__order_service.delete_order(order_info[int(val)-1])
            print("Pöntuninni hefur verið eytt")
            print("-"*34)
        else:
            print("Hætt við")
            print("-"*34)
        
        return self.go_to_menu()

    def print_orders(self, list_of_orders):
        print("{:<8}{:<11}{:<14}{:<12}{:<20}".format(\
        "Nr.", "Frá", "Til", "Bílnúmer", "Viðbótartrygging"))
        list_no = 1
        for order in list_of_orders:
            print("{:<8}".format(list_no) + order.__str__())
            list_no += 1
    
    def find_order(self):
        clear_screen()
        print("Finna pöntun")
        print("-"*34)
        email = self.email_input()
        clear_screen() 
        order_list = self.__order_service.get_customer_orders(email)
        self.print_orders(order_list)
        return self.go_to_menu()
