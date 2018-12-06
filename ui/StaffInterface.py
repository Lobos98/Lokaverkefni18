import os
from BusinessLayer.ErrorCatch import ErrorCatch
from BusinessLayer.CarService import CarService
from BusinessLayer.OrderService import OrderService
from BusinessLayer.CustomerService import CustomerService

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
        print("-"*len("1.  Skrá nýjan viðskiptavin"))
        print("1.  Skrá nýjan viðskiptavin")
        print("2.  Fletta upp viðskiptavin")
        print("3.  Afskrá viðskiptavin")
        print("4.  Uppfæra viðskiptavin")
        print("5.  Setja á bannlista")
        print("6.  Taka af bannlista")
        print("7.  Sekta viðskiptavin")
        print("8.  Til baka")
        print("-"*len("1.  Skrá nýjan viðskiptavin"))
        input_num = input("Val: ")
        print()
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
                    print("Kennitala er ógild, reyndu aftur eða 'q' til að hætta")
                    ssn = input("Kennitala: ")
            print("Kennitala er gild")
        return ssn
    
    def register_customer(self):
        cls()
        name = input("Nafn: ")
        phone = self.phone_input()
        email = self.email_input()
        card_number = self.card_input()
        ssn = self.ssn_checker()
        
        print("-"*57)
        self.__customer_service.add_customer(email, name, card_number, phone, ssn)
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
        svar = input("Afskrá: {}, {}? (j/n): ".format(cust.get_name(), email))
        print("-"*60)
        if svar.lower() == "j":
            self.__customer_service.delete_customer(email)
            print("{} afskráð".format(cust.get_name()))
        else:
            print("Hætt við")
        print("-"*60)
        self.go_to_menu()

    def find_customer(self):
        cls()
        #print("Fletta upp viðskiptavini eftir: ")
        email = input("Sláðu inn netfang viðskiptavins: ")
        print("-"*(33+len(email)))
        customer_found = self.__customer_service.find_customer(email)
        print(customer_found)
        print("-"*(33+len(email)))
        choice = input("Viltu breyta viðskiptavin? (j/n): ")
        print("-"*(33+len(email)))
        if choice.lower() == "j":
            self.edit_customer(customer_found)
        else:
            self.go_to_menu()

    def edit_customer(self, customer):
        cls()
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
            self.__customer_service.edit_customer_phone_no(customer.get_email(), simanr)
            print("Símanúmeri hefur verið breytt.")
            print("-"*30)
        elif val == "2":
            cls()
            netfang = input("Nýtt netfang: ")
            print("-"*(14+len(netfang)))
            self.__customer_service.edit_customer_email(customer.get_email(), netfang)
            print("Netfangi hefur verið breytt.")
            print("-"*(14+len(netfang)))
        elif val == "3":
            cls()
            kortanumer = input("Nýtt kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
            print("-"*(62))
            self.__customer_service.edit_customer_card_no(customer.get_email(), kortanumer)
            print("Kortanúmeri hefur verið breytt.")
            print("-"*(62))
        elif val == "4":
            print("----------------------------")
            self.go_to_menu()

        self.go_to_menu()
        

    def ban_customer(self):
        cls()
        print("Setja á bannlista")
        print("-"*60)
        email = self.email_input()
        customer = self.__customer_service.find_customer(email)
        cls()
        print("Setja á bannlista")
        print("-"*(31 + len(customer.get_name()) + len(email)))
        stadfesta = input("Setja á bannlista: {}, {}? (j/n): ".format(customer.get_name(), email))
        self.__customer_service.ban_customer(email)
        if stadfesta == "j":
            print("Jón Ólafsson hefur verið færður á bannlista.")
        else:
            print("Hætt við.")
        print("-"*(31 + len(customer.get_name()) + len(email)))
    
        self.go_to_menu()
        
    def unban_customer():
        cls()
        email = input("Netfang: ")
        print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))
        stadfesta = input("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala))
        print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))
        self.__customer_service.unban_customer(email)
        if stadfesta == "j":
            print("Jón Ólafsson hefur verið tekinn af bannlista.")
        else:
            print("Hætt við.")
        print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))

        self.go_to_menu()
        
    def fine_customer():
        cls()
        email = input("Kennitala/netfang: ")
        print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
        stadfesta = input("Sekta: Jón Ólafsson, {}? (j/n): ".format(kennitala))
        print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
        if(stadfesta == "j"):
            fine_amount = input("Upphæð sektar: ")
            self.__customer_service.fine_customer(email, fine_amount)
            print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
            print("Jón Ólafsson hefur verið sektaður um {} kr.".format(upphaed_sektar))
        else:
            print("Hætt við.") 
        print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def vehicle_menu(self):
        cls()
        print("Bílafloti")
        print("-"*len("2.  Birta útleigða bíla"))
        print("1.  Birta lausa bíla")
        print("2.  Birta útleigða bíla")
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
            self.display_reserved_cars()
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
            self.print_options()

    def display_free_cars(self):
        cls()
        dags_fyrri_string = input("Dagsetning leigu: ")
        print("-"*len("Dagsetning leigu: "))
        dags_seinni_string = input("Dagsetning skila: ")
        cls()
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
        print(60*"-")

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass
        

    def display_reserved_cars(self):
        cls()
        dags_fyrri_string = input("Dagsetning leigu: ")
        print("-"*len("Dagsetning leigu: "))
        dags_seinni_string = input("Dagsetning skila: ")
        cls()
        print("Eftirfarandi bílar eru í útleigu á tímabilinu frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SX-452", "Jeppi", "2003", "Grænn", "3000 kr/dag"))
        print(60*"-")

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def return_car(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        print("-"*len("Bílnum {} hefur verið skilað!".format(bilnumer)))
        print("Bílnum {} hefur verið skilað!".format(bilnumer))
        print("-"*len("Bílnum {} hefur verið skilað!".format(bilnumer)))

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def add_car(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        print("-"*len("Bílnum {} hefur verið skráður!".format(bilnumer)))
        print("Bíllinn {} hefur verið skráður!".format(bilnumer))
        print("-"*len("Bílnum {} hefur verið skráður!".format(bilnumer)))

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass
        #Hér eigum við eftir að bæta við virkni til þess að geyma lit, gerð, verð
        # og fleiri upplýsingar um bílinn sem myndu vera attributes í klasa

    def delete_car(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        print("-"*len("Bílnum {} hefur verið afskráður!".format(bilnumer)))
        print("Bíllinn {} hefur verið afskráður!".format(bilnumer))
        print("-"*len("Bílnum {} hefur verið afskráður!".format(bilnumer)))

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def find_car(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        cls()
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(bilnumer, "2003", "Jeppi", "Grænn", "3000 kr/dag"))
        print(60*"-")

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def broken_cars(self):
        cls()
        print("Bilaðir bílar")
        print("-"*len("3.  Birta bilaða bíla"))
        print("1.  Skrá bíl")
        print("2.  Afskrá bíl")
        print("3.  Birta bilaða bíla")
        print("4.  Til baka")
        print("-"*len("3.  Birta bilaða bíla"))
        input_num = input("Val: ")

        if input_num == "1":
            add_carada_bil()
        elif input_num == "2":
            delete_carada_bil()
        elif input_num == "3":
            skoda_bil()
        else:
            print_options()

    def add_carada_bil(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        reason = input("Af hverju er hann bilaður? ")
        cls()
        print("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer))
        print("-"*len("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer)))
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def delete_carada_bil(self):
        cls()
        bilnumer = input("Bílnúmer: ")
        cls()
        print("Bíllinn {} hefur verið skráður á ný.".format(bilnumer))
        print("-"*len("Bíllinn {} hefur verið skráður á ný.".format(bilnumer)))
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def skoda_bil(self):
        cls()
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("GHY-234", "Fólksbíll", "2009", "Blár", "Vélarbilun"))
        print(60*"-")

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def afgreidsla_options(self):
        cls()
        print("Afgreiðsla")
        print("-"*len("2.  Skrá nýjan viðskiptavin"))
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
        print("-"*len("2.  Skrá nýjan viðskiptavin"))
        input_num = input("Val: ")
        print()
        if input_num == "1":
            display_free_cars()
        elif input_num == "2":
            skra_vidskiptavin()
        elif input_num == "3":
            skra_pontun()
        elif input_num == "4":
            kostnadarmat()
        elif input_num == "5":
            return_car()
        elif input_num == "6":
            afskra_vidskiptavin()
        elif input_num == "7":
            bakfaera_pontun()
        elif input_num == "8":
            breyta_vidskiptavin()
        elif input_num == "9":
            breyta_pontun()
        else:
            print_options()

    def skra_pontun(self):
        cls()
        kt = input("Kennitala/netfang: ")
        print("-"*len("Kennitala/netfang: 1506992669"))
        print("Leigutímabil?")
        print("-"*len("Kennitala/netfang: 1506992669"))
        fra = input("Frá (YYYY, MM, DD): ")
        til = input("Til (YYYY, MM, DD): ")
        cls()
        print("Lausir bílar á leigutímabili ({}) - ({})".format(fra, til))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
        print(60*"-")
        bilnumer = input("Veldu bíl (AA-X99) eða n til að hætta við: ")
        print(60*"-")
        
        if bilnumer.lower() == "n":
            print("Þú hefur hætt við að leigja út bíl.")
            print("-"*len("Þú hefur hætt við að leigja út bíl."))

            svar = input("Fara aftur á valmynd? (j/n): ")
            if svar.lower() == "j":
                print_options()
            else:
                pass
        else:
            print("Áætlaður kostnaður án tryggingar: 45.000 kr.")
            print(60*"-")
            val = input("Samþykkja? (j/n): ")
            print(60*"-")

            if val.lower() == "j":
                trygging_check = input("Má bjóða þér aukatryggingu fyrir 500 kr. aukalega pr. dag? (j/n): ")
                print(60*"-")
                if trygging_check.lower() == "j":
                    print("Lokaverð 50.000 kr.")
                    val = input("Samþykkja? (j/n): ")
                    print(60*"-")
                    if val.lower() == "j":
                        print("Bíllinn",bilnumer,"hefur verið leigður út ({}) - ({})".format(fra, til))
                        print("-"*len("Bíllinn " + bilnumer + " hefur verið leigður út ({}) - ({})".format(fra, til)))
                        svar = input("Fara aftur á valmynd? (j/n): ")
                        if svar.lower() == "j":
                            print_options()
                        else:
                            pass
                    else:
                        print("Þú hefur hætt við að leigja út bíl")
                        print(60*"-")

                        svar = input("Fara aftur á valmynd? (j/n): ")
                        if svar.lower() == "j":
                            print_options()
                        else:
                            pass
                else:
                    print("Bíllinn",bilnumer,"hefur verið leigður út ({}) - ({})".format(fra, til))
                    print(60*"-")

                    svar = input("Fara aftur á valmynd? (j/n): ")
                    if svar.lower() == "j":
                        print_options()
                    else:
                        pass
            else:
                print("Þú hefur hætt við að leigja út bíl")
                print(60*"-")
                svar = input("Fara aftur á valmynd? (j/n): ")
                if svar.lower() == "j":
                    print_options()
                else:
                    pass

    def kostnadarmat(self):
        cls()
        fra = input("Frá (YYYY, MM, DD): ")
        til = input("Til (YYYY, MM, DD): ")
        cls()
        # Hér er sett inn copy úr fallinu display_free_cars()
        print("Eftirfarandi bílar eru lausir frá {} til {}:".format(fra, til))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "4500 kr/dag"))
        print(60*"-")
        dummy_input = input("Bílnúmer: ")
        bill_verd = 4500
        dagur_a = fra.split(",")[2]
        dagur_a = int(dagur_a.strip())
        dagur_b = til.split(",")[2]
        dagur_b = int(dagur_b.strip())
        # vantar með mán en erum ekki með date svo læt þetta duga
        # display_free_cars(fra, til) # fá hvaða bílar eru lausir
        # val = input("Veldu bíl (AA-X99): ")
        # við fáum tímabil frá fletta_pontun og mínusum fyrra tímabilið frá því seinna
        # þá fáum við hve marga daga viðkomandi hefur bílinn og margföldum dagana við dagskostnaðinn
        dagar = dagur_b - dagur_a + 1
        verd_samtals = dagar*bill_verd
        cls()
        print("Kostnaðarmat:", verd_samtals, "Kr.")
        print("-"*len("Kostnaðarmat: "+ str(verd_samtals) + " Kr."))

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def pantanir_options(self):
        cls()
        print("Pantanir")
        print("-"*len("3.  Fletta upp pöntun"))
        print("1.  Skrá pöntun")
        print("2.  Breyta pöntun")
        print("3.  Fletta upp pöntun")
        print("4.  Bakfæra pöntun")
        print("5.  Til baka")
        print("-"*len("3.  Fletta upp pöntun"))
        input_num = input("Val: ")
        print()
        if input_num == "1":
            skra_pontun()
        elif input_num == "2":
            breyta_pontun()
        elif input_num == "3":
            fletta_pontun()
        elif input_num == "4":
            bakfaera_pontun()
        else:
            print_options()

    def breyta_pontun(self):
        cls()
        kennitala = input("Hver er kennitalan/netfangið? ")
        cls()
        print("Hverju viltu breyta?")
        print("-"*len("Hverju viltu breyta?"))
        print("1. Dagsetningu")
        print("2. Bíl")
        print("3. Til baka")
        print("-"*len("Hverju viltu breyta?"))
        input_num = input("Val: ")

        cls()
        if input_num == "1":
            fra = input("Frá (YYYY, MM, DD): ")
            til = input("Til (YYYY, MM, DD): ")
            print("-"*len("Dagsetningu hefur verið breytt."))
            print("Dagsetningu hefur verið breytt.")
            print("-"*len("Dagsetningu hefur verið breytt."))
        
        elif input_num == "2":
            print("Eftirfarandi bílar eru lausir á tímabili þessarar pöntunar:")
            print(60*"-")
            print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
            print(60*"-")
            print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
            print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
            print(60*"-")
            print("Núverandi bíll: SG-X69")
            bil = input("Nýr bíll: ")
            print(60*"-")
            print("Nýr bíll hefur verið valinn.")

        else:
            svar = input("Fara aftur á valmynd? (j/n): ")
            if svar.lower() == "j":
                print_options()
            else:
                pass
        
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass
        

    def fletta_pontun(self):
        cls()
        kt = input("Kennitala/netfang pöntunar: ")
        cls()
        print("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt))
        print("SB-463 á tímabilinu 10/12/18 til 14/12/18")
        print("-"*len("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt)))
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass

    def bakfaera_pontun(self):
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
        
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass


