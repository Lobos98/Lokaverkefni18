import os
import datetime
from BusinessLayer.ErrorCatch import ErrorCatch
from BusinessLayer.CarService import CarService
from BusinessLayer.OrderService import OrderService
from BusinessLayer.CustomerService import CustomerService
from models.Car import Car

def cls():
    os.system('cls')


class StaffInterface:
    def __init__(self):
        self.__car_service = CarService()
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__error_catch = ErrorCatch()


    def main_menu(self):
        cls()
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
            self.main_menu()

    def go_to_menu(self):
        choice = input("Fara aftur á valmynd? (j/n): ")
        if choice.lower() == "j":
            self.main_menu()
        else:
            pass
        
    def customer_menu(self):
        cls()
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
                self.go_to_menu()
            else:
                print("Rangt kortanúmer, reyndu aftur eða 'q' til að hætta")
                card_number = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        return card_number
    
    def phone_input(self):
        phone = input("Símanúmer: ")
        while not self.__error_catch.check_phone_no(phone):
            if phone.lower() == "q":
                self.go_to_menu()
            else:
                print("Rangt símanúmer, reyndu aftur eða 'q' til að hætta")
                phone = input("Símanúmer: ")
        return phone
    
    def email_input(self):
        email = input("Netfang: ")
        while not self.__error_catch.check_email(email):
            if email.lower() == "q":
                self.go_to_menu()
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
                    self.go_to_menu()
                else:
                    print("Kennitala er ógild, reyndu aftur eða 'q' til að\
                        hætta")
                    ssn = input("Kennitala: ")
            print("Kennitala er gild")
            return ssn
        else:
            return "0"
        
    
    def register_customer(self):
        cls()
        print("Skrá nýjan viðskiptavin")
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
        self.go_to_menu()

    def deregister_customer(self):
        cls()
        print("Afskrá viðskiptavin")
        print("-"*60)
        email = self.email_input()
        print("-"*60)
        cust = self.__customer_service.find_customer(email)
        if cust != False:
            svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(),\
                email))
            print("-"*60)
            if svar.lower() == "j":
                self.__customer_service.delete_customer(email)
                print("{} afskráð".format(cust.get_name()))
            else:
                print("Hætt við")
        else:
            peint("Notandinn fannst ekki")
        print("-"*60)
        self.go_to_menu()

    def find_customer(self):
        cls()
        print("Fletta upp viðskiptavin")
        print("-"*60)
        email = input("Sláðu inn netfang viðskiptavins: ")
        print("-"*(33+len(email)))
        customer_found = self.__customer_service.find_customer(email)
        if customer_found != False:
            print(customer_found)
            print("-"*(33+len(email)))
            choice = input("Viltu breyta viðskiptavin? (j/n): ")
            print("-"*(33+len(email)))
            if choice.lower() == "j":
                self.edit_customer(customer_found)
        self.go_to_menu()

    def edit_customer(self, customer):
        cls()
        print("Uppfæra viðskiptavin")
        print("-"*(6+len(customer.get_email())))
        print(customer)
        print("-"*(6+len(customer.get_email())))
        print("Hverju viltu breyta?: ")
        print("-"*(6+len(customer.get_email())))
        print("1. Símanúmeri")
        print("2. Netfangi")
        print("3. Kreditkortanúmeri")
        print("4. Til baka")
        print("-"*(6+len(customer.get_email())))
        val = input("Val: ")
        print("-"*(6+len(customer.get_email())))

        if val == "1":
            cls()
            simanr = input("Nýtt Símanúmer: ")
            print("-"*30)
            self.__customer_service.edit_customer_phone_no(customer.\
                get_email(),simanr)
            print("Símanúmeri hefur verið breytt.")
            print("-"*30)
        elif val == "2":
            cls()
            netfang = input("Nýtt netfang: ")
            print("-"*(14+len(netfang)))
            self.__customer_service.edit_customer_email(customer.get_email(),\
                netfang)
            print("Netfangi hefur verið breytt.")
            print("-"*(14+len(netfang)))
        elif val == "3":
            cls()
            kortanumer = input("Nýtt kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
            print("-"*(62))
            self.__customer_service.edit_customer_card_no(customer.\
                get_email(),kortanumer)
            print("Kortanúmeri hefur verið breytt.")
            print("-"*(62))
        elif val == "4":
            print("-"*(6+len(customer.get_email())))
            self.go_to_menu()

        self.go_to_menu()
        

    def ban_customer(self):
        cls()
        print("Setja á bannlista")
        print("-"*60)
        email = self.email_input()
        customer = self.__customer_service.find_customer(email)
        if customer != False:
            print("-"*(31 + len(customer.get_name()) + len(email)))
            stadfesta = input("Setja á bannlista: {}, {}? (j/n): ".\
                format(customer.get_name(), email))
            self.__customer_service.ban_customer(email)
            if stadfesta == "j":
                print("{} hefur verið færður á bannlista.".\
                    format(customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(email)))
        else:
            print("Notandi fannst ekki")
        self.go_to_menu()
        
    def unban_customer(self):
        cls()
        print("Taka af bannlista")
        print("-"*60)
        email = self.email_input()
        customer = self.__customer_service.find_customer(email)
        if customer != False:
            print("-"*(31 + len(customer.get_name()) + len(email)))
            stadfesta = input("Taka af bannlista: {}, {}? (j/n): ".\
                format(customer.get_name(), email))
            print("-"*(31 + len(customer.get_name()) + len(email)))
            self.__customer_service.unban_customer(email)
            if stadfesta == "j":
                print("{} hefur verið tekinn af bannlista.".\
                    format(customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(email)))
        else:
            print("Notandi fannst ekki")

        self.go_to_menu()
        
    def fine_customer(self):
        cls()
        print("Sekta viðskiptavin")
        print("-"*60)
        email = self.email_input()
        customer = self.__customer_service.find_customer(email)
        if customer != False:
            print("-"*len("Sekta: {}, {}? (j/n)  ".format(customer.get_name(),\
                email)))
            stadfesta = input("Sekta: {}, {}? (j/n): ".\
                format(customer.get_name(),email))
            print("-"*len("Sekta: {}, {}? (j/n)  ".format(customer.get_name(),\
                email)))
            if(stadfesta == "j"):
                fine_amount = input("Upphæð sektar (kr): ")
                self.__customer_service.fine_customer(email, fine_amount)
                print("{} hefur verið sektaður um {} kr.".\
                    format(customer.get_name(), fine_amount))
            else:
                print("Hætt við.") 
            print("-"*len("Sekta: {}, {}? (j/n)  ".format(customer.get_name(),\
                email)))
        else:
            print("Notandi fanns ekki")
        self.go_to_menu()

    def vehicle_menu(self):
        cls()
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
            self.find_car()
        elif input_num == "7":
            self.broken_cars()
        else:
            self.main_menu()

    def date_input(self):
        pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
        return_date_string = input("Dagsetning skila (ddmmáááá): ")
        while self.__error_catch.check_rental_date(\
        pickup_date_string, return_date_string) == False:
            print("Athugið eftirfarandi:\n\
            Dagsetningar skal skrifa inn á forminu ddmmáááá\n\
            Hámarksleigutími er eitt ár\n\
            Ekki er hægt að velja leigutímabil sem er liðið")
            pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
            return_date_string = input("Dagsetning skila (ddmmáááá): ")
        return pickup_date_string, return_date_string

    def display_free_cars(self):
        cls()
        print("Birta lausa bíla")
        print("-"*37)
        pickup_date_string, return_date_string = self.date_input()

        cls()
        print("Birta lausa bíla")
        print(60*"-")
        free_car_list = self.__car_service.find_free_cars(\
        pickup_date_string, return_date_string)
        pickup_date_string = pickup_date_string[0:2] + "."\
        + pickup_date_string[2:4] + "." + pickup_date_string[4:8]
        return_date_string = return_date_string[0:2] + "."\
        + return_date_string[2:4] + "." + return_date_string[4:8]
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(\
        pickup_date_string, return_date_string))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
        "Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        for car in free_car_list:
            print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
            car.get_reg_num(), car.get_type(), car.get_model(), car.get_color(), \
            str(self.__car_service.get_price(car)) + "kr/dag"))
        print(60*"-")

        return pickup_date_string, return_date_string, free_car_list

        

    def display_currently_rented_cars(self):
        cls()
        print("Eftirfarandi bílar eru í útleigu í augnablikinu")
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        rented_car_list = self.__car_service.get_rented_cars()
        for car in rented_car_list:
            print(car)
        print(60*"-")

        self.go_to_menu()

    def return_car(self):
        """Biður um email pöntunar í input, kallar á ErrorCheck
        og sendir emailið svo í CarService til að skila viðkomandi bíl"""
        #Ath hér vantar að fjarlægja order úr future orders í past orders
        cls()
        email = self.__error_catch.input_email()
        order = self.__order_service.find_order(email)
        if order == False:
            print("Pöntun finnst ekki á þessu netfangi.")
            self.return_car()
        else:
            reg_num = self.__car_service.return_car(order)

            print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))
            print("Bílnum {} hefur verið skilað!".format(reg_num))
            print("-"*len("Bílnum {} hefur verið skilað!".format(reg_num)))
        

        self.go_to_menu()

    def add_car(self):
        cls()
        reg_num = self.__error_catch.input_reg_num()
        model = self.__error_catch.input_model()
        type = self.__error_catch.input_type()
        color = self.__error_catch.input_color()
        self.__car_service.add_car(reg_num, model, type, color)
        print("-"*len("Bíllinn {} hefur verið skráður!".format(reg_num)))
        print("Bíllinn {} hefur verið skráður!".format(reg_num))
        print("-"*len("Bílnum {} hefur verið skráður!".format(reg_num)))

        self.go_to_menu()
        #Hér eigum við eftir að bæta við virkni til þess að geyma lit, gerð, verð
        # og fleiri upplýsingar um bílinn sem myndu vera attributes í klasa

    def delete_car(self):
        cls()
        reg_num = self.__error_catch.input_reg_num()
        car = False
        while car == False:
            car = self.__car_service.find_car(reg_num)
            if car == False:
                print("Bíllinn {} finnst ekki.".format(reg_num.upper()))
        self.__car_service.delete_car(reg_num)


        print("-"*len("Bíllinn {} hefur verið afskráður!".format(reg_num)))
        print("Bíllinn {} hefur verið afskráður!".format(reg_num))
        print("-"*len("Bíllinn {} hefur verið afskráður!".format(reg_num)))

        self.go_to_menu()

    def find_car(self):
        cls()
        car = False
        while car == False:
            reg_num = self.__error_catch.input_reg_num()
            car = self.__car_service.find_car(reg_num)
            if car == False:
                print("Bíllinn {} finnst ekki.".format(reg_num.upper()))
        cls()
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print(car)
        print(60*"-")

        self.go_to_menu()

    def broken_cars(self):
        cls()
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
            self.vehicle_menu()

    def log_broken_car(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        reason = input("Af hverju er hann bilaður? ")
        cls()
        print("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer))
        print("-"*len("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer)))
        
        self.go_to_menu()

    def log_car_as_fixed(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        cls()
        print("Bíllinn {} hefur verið skráður á ný.".format(bilnumer))
        print("-"*len("Bíllinn {} hefur verið skráður á ný.".format(bilnumer)))
        
        self.go_to_menu()

    def print_broken_cars(self):
        cls()
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("GHY-234", "Fólksbíll", "2009", "Blár", "Vélarbilun"))
        print(60*"-")

        self.go_to_menu()

    def service_menu(self):
        cls()
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

    def create_order(self):
        cls()
        pickup_date, return_date, free_cars = self.display_free_cars()
        reg_number = self.__error_catch.input_reg_num()
        free_cars_reg_num = [car.get_reg_num() for car in free_cars]
        while True:
            if reg_number not in free_cars_reg_num:
                print("Vinsamlegast veldu bíl á listanum")
                reg_number = self.__error_catch.input_reg_num()
            else:
                break
        email = self.__error_catch.input_email()
        if self.__customer_service.find_customer(email):
            if self.__customer_service.find_customer(email)\
            .get_banned() == "true":
                print("Þessi viðskiptavinur er bannaður")
                return self.go_to_menu()
        order_input_tuple = (reg_number, pickup_date, return_date, email)
        while True:
            extra_insurance = input("Má bjóða þér auka tryggingu? (j/n): ")
            if extra_insurance.lower() == "j":
                self.__order_service.log_order(*order_input_tuple, "true")
                break
            else:
                self.__order_service.log_order(*order_input_tuple, "false")
                break
        print("Þér hefur tekist að panta bílinn {}".format(reg_number))
        return self.go_to_menu()


    def cost_amount(self):
        pickup_date, return_date = self.date_input()
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
        print("Verð á völdu tímabili:", price)
        choice = input("Viltu leigja bíl? (j/n): ")
        if choice.lower() == "j":
            return self.create_order()
        else:
            return self.go_to_menu()

    def order_menu(self):
        cls()
        print("Pantanir")
        print("-"*21)
        print("1.  Skrá pöntun")
        print("2.  Breyta pöntun")
        print("3.  Fletta upp pöntun")
        print("4.  Bakfæra pöntun")
        print("5.  Til baka")
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
        else:
            self.go_to_menu()

    def change_order(self):
        '''Alls ekki tilbúið fall!!!! hallóóó'''
        cls()
        print("Breyta Pöntun")
        print("-"*(20))
        email = input("Hvað er netfangið?: ")
        cls()
        print("Breyta Pöntun")
        print("-"*(20 + len(email)))
        # hérna er ég að gera breyta fyrir nafnið á viðskiptavin
        print("Hverju viltu breyta fyrir {}?".format(order_info.get))
        print("-"*(20 + len(email)))
        print("1. Dagsetningu")
        print("2. Bíl")
        print("3. Til baka")
        print("-"*(20 + len(email)))
        input_num = input("Val: ")

        cls()
        if input_num == "1":
            pickup_date, return_date = self.date_input()
            self.__order_service.change_order(email, input_num, pickup_date, return_date)
            print("-"*(20 + len(email)))
            print("Dagsetningu hefur verið breytt.")
            print("-"*(20 + len(email)))
        
        elif input_num == "2":

            pickup_date, return_date, free_cars = self.display_free_cars()
            order_info = self.__order_service.find_order(email)
            print("Núverandi bíll: {}".format(order_info.get_car_reg_num()))
            reg_number = self.__error_catch.input_reg_num()
            free_cars_reg_num = [car.get_reg_num() for car in free_cars]
            while True:
                if reg_number not in free_cars_reg_num:
                    print("Vinsamlegast veldu bíl á listanum")
                    reg_number = self.__error_catch.input_reg_num()
                else:
                    break

            self.__order_service.change_order(email, input_num, pickup_date, return_date, reg_number)
            
            print("-"*(20 + len(email)))
            print("Bíllinn {} hefur verið valinn.".format(reg_number))
            print("-"*(20 + len(email)))
        
        else:
            self.go_to_menu()
        
        self.go_to_menu()
        

    def find_order(self):
        cls()
        kt = input("Kennitala/netfang pöntunar: ")
        cls()
        print("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt))
        print("SB-463 á tímabilinu 10/12/18 til 14/12/18")
        print("-"*len("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt)))
        return self.go_to_menu()

    def delete_order(self):
        # fletta_pontun()
        cls()
        kt = input("Kennitala/netfang pöntunar: ")
        cls()
        print("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt))
        print("SB-463 á tímabilinu 10/12/18 til 14/12/18")
        print("-"*len("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt)))
        choice = input("Viltu eyða þessari pöntun? (j/n): ")
        cls()
        if(choice == "j"):
            print("Pöntuninni hefur verið eytt")
            print("---------------------------")
        else:
            print("Hætt við")
            print("--------")
        
        self.go_to_menu()
