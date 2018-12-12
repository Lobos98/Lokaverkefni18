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
        """Prentar 60 bandstrik"""
        print("-"*60)
    
    def start_menu(self):
        """Prentar logo fyrirtækisins og spyr hvort keyra skuli forritið"""
        clear_screen()
        print("Velkomin í Bílaleiguna IceCarRentals.")
        print("-"*37)
        n = 7
        print(r"""{}        _______""".format(" "*n))
        print(r"""{}       //  ||\ \ """.format(" "*n))
        print(r"""{}  ____//___||_\ \__""".format(" "*n))
        print(r"""{} )  _          _    \ """.format(" "*n))
        print(r"""{} |_/ \________/ \___|""".format(" "*n))
        print(r"""{}___\_/________\_/_____""".format(" "*n))
        print(r"""{}Drive cheap, not safe!""".format(" "*n))
        print("-"*37)
        answer = input("Keyra forrit? (j/n): ")
        if answer.lower() == "j":
            self.main_menu()
        else:
            exit()

    def print_a_menu(self, a_list):
        for index, text in enumerate(a_list):
            print("{}.  {}".format(index + 1, text))

    def main_menu(self):
        """Dregur upp aðalvalmyndina og leyfir okkur að velja milli 
        fjögurra yfirvalmynda"""
        clear_screen()
        print("Veldu eitt af eftirfarandi")
        print("-"*len("Veldu eitt af eftirfarandi"))
        menu_list = ["Viðskiptavinir", "Bílafloti", 
        "Afgreiðsla", "Pantanir", "Hætta"]
        self.print_a_menu(menu_list)
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
            pass
        return self.go_to_menu()

    def go_to_menu(self):
        choice = input("Fara aftur á aðalvalmynd? (j/n): ")
        if choice.lower() == "j":
            return self.main_menu()
        
    def customer_menu(self):
        clear_screen()
        print("Viðskiptavinir")
        print("-"*27)
        menu_list = ["Skrá viðskiptavin", "Fletta upp viðskiptavin", "Afskrá viðskiptavin", 
        "Uppfæra viðskiptavin", "Setja á bannlista", "Taka af bannlista", 
        "Sekta viðskiptavin", "Til baka"]
        self.print_a_menu(menu_list)
        print("-"*27)
        input_num = input("Val: ")

        if input_num == "1":
            self.register_customer()
        elif input_num == "2":
            self.find_customer()
        elif input_num == "3":
            self.deregister_customer()
        elif input_num == "4":
            self.edit_customer()
        elif input_num == "5":
            self.ban_customer()
        elif input_num == "6":
            self.unban_customer()
        elif input_num == "7":
            self.fine_customer()
        else:
            pass
        return self.go_to_menu()
    
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
            return ""
    
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

    def deregister_customer(self):
        clear_screen()
        print("Afskrá viðskiptavin")
        self.__print_divider()
        cust = self.find_customers()
        email = cust.get_email()
        if cust != False:
            svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(),\
                email))
            self.__print_divider()
            if svar.lower() == "j":
                if not self.__order_service.find_order(email):
                    self.__customer_service.delete_customer(email)
                    print("{} afskráð".format(cust.get_name()))
                else:
                    print("{} er ennþá með pöntun í framtíðinni".format(cust.get_name()))
                    choice = input("Ertu viss að þú viljir afskrá þennan viðskiptavin? (j/n): ")
                    if choice.lower() == "j":
                        self.__customer_service.delete_customer(email)
                        print("{} afskráð".format(cust.get_name()))
                    else:
                        print("Hætt var við")
                        self.go_to_menu()
            else:
                print("Hætt við")
        else:
            print("Notandinn fannst ekki")
        self.__print_divider()

    def find_customers(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)
        print("Leita eftir:")
        menu_list = ["Nafni", "Netfangi", "Kennitala", "Til baka"]
        self.print_a_menu(menu_list)
        print("-"*50)
        choice = input("Val: ")
        if choice == "1":
            return self.find_by_name()
        elif choice == "2":
            return self.find_by_email()
        elif choice == "3":
            return self.find_by_ssn()

    def find_by_name(self):

        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)
        name = input("Sláðu inn nafn viðskiptavins: ")
        clear_screen()


        customer_found_list = self.__customer_service.\
        find_customer_by_name(name)
        print("Fletta upp viðskiptavin")
        print("-"*50)
        if len(customer_found_list) == 1:
            customer_found = customer_found_list[0]
            return customer_found
        elif len(customer_found_list) > 1:
            index = 1
            for customer in customer_found_list:
                print("{}. {}".format(index, customer))
                if index < len(customer_found_list):
                    print()
                index += 1
            print("-"*(50))
            choice = int(input("Veldu einn viðskiptavin hér fyrir ofan: ")) - 1
            customer_found = customer_found_list[choice]
            return customer_found
        else:
            print("Enginn viðskiptavinur fundinn á þessu nafni")
            choice = input("viltu reyna aftur (j/n) eða skrá nýjan viðskiptavin (s)?: ")
            if choice.lower() == "j":
                 return self.find_by_name()
            elif choice.lower() == "s":
                return self.register_customer()
            else:
                self.go_to_menu()

    def find_by_ssn(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)

        customer_found = False
        while customer_found == False:
            ssn = self.ssn_checker()
            customer_found = self.__customer_service.find_customer_by_ssn(ssn)
            if customer_found == False:
                choice = input("Kennitala er ekki á skrá, "
                "reyndu aftur eða ýttu á s til að skrá nýjan viðskiptavin: ")
                if choice.lower() == "s":
                    return self.register_customer()
        return customer_found

        
    def find_by_email(self):
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*50)

        customer_found = False
        while customer_found == False:
            email = self.email_input()
            customer_found = self.__customer_service.find_customer(email)
            if customer_found == False:
                choice = input("Netfang er ekki á skrá, "
                "reyndu aftur eða ýttu á s til að skrá nýjan viðskiptavin: ")
                if choice.lower() == "s":
                    return self.register_customer()
        return customer_found
    
    def find_customer(self):
        customer_found = self.find_customers()
        clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*(33+len(customer_found.get_name())))
        print(customer_found)
        print("-"*(33+len(customer_found.get_name())))
        choice = input("Viltu breyta viðskiptavin? (j/n): ")
        print("-"*(33+len(customer_found.get_name())))


        if choice.lower() == "j":
            self.edit_customer(customer_found)
        else:
            return self.go_to_menu()

    def edit_customer(self, customer_found=0 ):
        if customer_found != 0:
            customer = customer_found
        else:
            customer = self.find_customers()

        clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*(7+len(customer.get_email())))
        print(customer)
        print("-"*(7+len(customer.get_email())))
        print("Hverju viltu breyta?: ")
        print("-"*(7+len(customer.get_email())))
        menu_list = ["Símanúmeri", "Netfangi", "Kortanúmeri"]
        self.print_a_menu(menu_list)
        print("-"*(7+len(customer.get_email())))
        val = input("Val: ")
        print("-"*(7+len(customer.get_email())))

        if val == "1":
            self.change_phone_no(customer)
        elif val == "2":
            self.change_email()
        elif val == "3":
            self.change_card_no()
        elif val == "4":
            print("-"*(6+len(customer.get_email())))
            #return self.go_to_menu()

        #return self.go_to_menu()

    def change_phone_no(self, customer):
        clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*30)
        #phone_no = input("Nýtt Símanúmer: ")
        #print("-"*30)
        phone_no = self.phone_input()
        #if self.__error_catch.check_phone_no(phone_no):
        self.__customer_service.edit_customer_phone_no(customer.\
            get_email(),phone_no)
        print("Símanúmeri hefur verið breytt.")
        print("-"*30)

    def change_email(self, customer):
        clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*40)
        #netfang = input("Nýtt netfang: ")
        #print("-"*40)
        email = self.email_input()
        self.__customer_service.edit_customer_email(customer.get_email()\
            , email)
        print("Netfangi hefur verið breytt.")
        print("-"*40)

    def change_card_no(self, customer):
        clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*(62))
        card_no = self.card_input()
        #kortanumer = self.card_input()
        #print("-"*(62))
        self.__customer_service.edit_customer_card_no(customer.\
            get_email(),card_no)
        print("Kortanúmeri hefur verið breytt.")
        print("-"*(62))
        

    def ban_customer(self):
        clear_screen()
        print("Setja á bannlista")
        self.__print_divider()
        customer = self.find_customers()
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
        customer = self.find_customers()
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
        customer = self.find_customers()
        clear_screen()

        print("Sekta viðskiptavin")
        if customer != False:
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))
            stadfesta = input("Sekta: {}, {}? (j/n): "\
            .format(customer.get_name(), customer.get_email()))
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))

            if(stadfesta.lower() == "j"):
                fine_amount = self.__error_catch\
                .integer_input("Upphæð sektar (kr)")
                self.__customer_service.fine_customer(customer.get_email(),\
                    fine_amount)
                print("{} hefur verið sektaður um {} kr.".\
                    format(customer.get_name(), fine_amount))
            else:
                print("Hætt við.") 
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fannst ekki")

    def vehicle_menu(self):
        """Setur bíla-valmyndina í gang"""
        #tilbúið
        clear_screen()
        print("Bílafloti")
        print("-"*len("2.  Birta bíla í útleigu"))
        menu_list = ["Birta lausa bíla", "Birta bíla í útleigu",
        "Skila bíl", "Skrá bíl", "Afskrá bíl", "Leita að bíl",
        "Bilaðir bílar", "Til baka"]
        self.print_a_menu(menu_list)
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
        self.__print_divider()
        free_car_list = self.__car_service.find_free_cars(\
        pickup_date_string, return_date_string)
        pickup_print = "{}{}.{}{}.{}{}{}{}".format(*pickup_date_string)
        return_print = "{}{}.{}{}.{}{}{}{}".format(*return_date_string)
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(\
        pickup_print, return_print))
        self.__print_divider()
        self.print_car_header()
        self.__print_divider()
        if free_car_list:
            for car in free_car_list:
                print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\

                car.get_reg_num(), car.get_type(), \
                car.get_model(), car.get_color(), \
                str(self.__car_service.get_price(car)) + "kr/dag"))
            self.__print_divider()
        else:
            print("Engir bílar eru lausir á þessu tímabili")
        return pickup_date_string, return_date_string, free_car_list

        

    def display_currently_rented_cars(self):
        """Sækir lista af bílum sem eru í útleigu 
        í augnablikinu og prentar þá"""
        #tilbúið
        clear_screen()
        print("Eftirfarandi bílar eru í útleigu í augnablikinu")
        self.__print_divider()
        self.print_car_header()
        self.__print_divider()
        rented_car_list = self.__car_service.get_rented_cars()
        for car in rented_car_list:
            print(car)
        self.__print_divider()

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
        if car_to_delete.get_reserved_dates() == []:
            self.__car_service.delete_car(reg_num)
                
            clear_screen()

            print("Afskrá bíl")
            print("-"*(31 + len(reg_num)))
            print("Bíllinn {} hefur verið afskráður!".format(reg_num))
            print("-"*(31 + len(reg_num)))
        else:
            choice = input("Þessi bíll er frátekinn fyrir viðskiptavin.\n\
            Ef bílnum er eytt verður tilsvarandi pöntunum einnig eytt.\n\
            Eyða bíl? (j/n):")
            if choice == "j":
                self.__car_service.delete_car(reg_num)
                self.__order_service.car_deleted(reg_num)
                clear_screen()

                print("Afskrá bíl")
                print("-"*(31 + len(reg_num)))
                print("Bíllinn {} hefur verið afskráður!".format(reg_num))
                print("-"*(31 + len(reg_num)))
            else:
                print("Þú hefur hætt við að eyða bílnum {}".format(reg_num))
        

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
        self.__print_divider()
        self.print_car_header()
        self.__print_divider()
        print(car)
        self.__print_divider()

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
        return self.go_to_menu()
        #return self.vehicle_menu()

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
        self.__print_divider()
        self.print_car_header()
        self.__print_divider()
        for car in broken_cars:
            print(car)
        self.__print_divider()

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
        menu_list = ["Birta lausa bíla", "Skrá nýjan viðskiptavin", 
        "Skrá pöntun", "Kostnaðarmat", "Skila bíl", 
        "Afskrá viðskiptavin", "Bakfæra pöntun", "Uppfæra viðskiptavin",
        "Breyta pöntun", "Til baka"]
        self.print_a_menu(menu_list)
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
            self.find_customers()
        elif input_num == "9":
            self.change_order()
        else:
            self.main_menu()

    def __is_banned(self, email):
        if self.__customer_service.find_customer(email):
            if self.__customer_service.find_customer(email)\
            .get_banned() == "true":
                print("Þessi viðskiptavinur er bannaður")
                return self.go_to_menu()

    def create_order(self):
        '''Þetta fall þarf að skoða'''
        clear_screen()
        print("Skrá pöntun")
        print("-"*34)
        customer = self.find_customers()
        if not customer:
            self.register_customer()
            
        print("Skrá pöntun")    
        email = customer.get_email()
        self.__is_banned(email) # Ef viðskiptavinurinn er bannaður
        # þá er maður sendur aftur í main menu

        #TODO finna goða lausn til að búa til nýjann viðskiptavin hér

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
        
        print("Auka trygging kostar 50% af verði bílsins, kostnaður er \
        þá {:,d} kr".format(round(price*insurance_price_coeff)))
        extra_insurance = input("Má bjóða þér auka tryggingu? (j/n): ")
        if extra_insurance.lower() == "j":
            insurance = "True"
            print("Nýja verðið er {:,d} kr."\
            .format(round(price*insurance_price_coeff)))
        else:
            insurance = "False"

        interim_order = self.__order_service.log_order(reg_number,\

        pickup_date, return_date, email, insurance)
        rented_car.add_reservation(interim_order)
        #TODO: þetta make_reservation fall er mjög skrýtið...
        self.__car_service.refresh_car(rented_car)

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
        menu_list = ["Skrá pöntun", "Breyta pöntun", "Fletta upp pöntun",
        "Bakfæra pöntun", "Prenta allar pantanir", "Til baka"]
        self.print_a_menu(menu_list)
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
        menu_list = ["Dagsetningu", "Bíl", "Til baka"]
        self.print_a_menu(menu_list)
        print("-"*(27 + len(cust.get_name())))
        input_num = input("Val: ")

        clear_screen()

        if input_num == "1":
            self.change_date(email, input_num)
        
        elif input_num == "2":
            self.change_car(email, input_num)
        
        else:
            return self.go_to_menu()
        
        

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
        while True:
            order_num = self.__error_catch.integer_input(
            "Veldu númer pöntunarinnar til að breyta: ")
            if order_num not in range(1, len(ordered_cars) + 1): 
                print("Vinsamlegast veldu pöntun á listanum")
                order_num = self.__error_catch.integer_input(
                "Veldu númer pöntunarinnar til að breyta: ")
            else:
                break

        car = ordered_cars[order_num - 1]            
        old_pickup_date = car.get_pickup_date()
        old_return_date = car.get_return_date()

        while True:
            free_cars = self.display_free_cars(old_pickup_date,
            old_return_date)[2]
            new_car_reg_num = self.__error_catch.input_reg_num()
            for a_car in free_cars:
                if a_car.get_reg_num() == new_car_reg_num:
                    print("Þú hefur leigt {}".format(new_car_reg_num))
                    print("-"*60)
                    return \
                    self.__order_service.change_order\
                    (car, "2", reg_number=new_car_reg_num)
        
        
    def change_date(self, email, input_num):
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
        
        while True:
            order_num = self.__error_catch.integer_input(
            "Veldu númer pöntunarinnar til að breyta: ")
            if order_num not in range(1, len(ordered_cars) + 1): 
                print("Vinsamlegast veldu pöntun á listanum")
                order_num = self.__error_catch.integer_input(
                "Veldu númer pöntunarinnar til að breyta: ")
            else:
                break
            
        car = ordered_cars[order_num - 1]

        pickup_date, return_date, free_cars\
         = self.display_free_cars()
        clear_screen()
        free_reg_numbers = [a_car.get_reg_num() for a_car in free_cars]
        if car.get_car_reg_num() in free_reg_numbers:
            print("Þú hefur breytt dagsetningunni")
            return \
            self.__order_service.change_order\
            (car, "1", pickup_date, return_date)
        print("Bíll sem er bundinn pöntun er frátekinn á þessu timabili.")


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
        val = self.__error_catch.integer_input("Veldu pöntun: ")
        print("-"*72)
        print("Þessi pöntun hefur verið valin: {}"\
        .format(order_info[int(val)-1]))
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
        
