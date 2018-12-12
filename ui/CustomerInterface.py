class CustomerInterface:
    def __init__(self, staff_interface):
        self.__staff_interface = staff_interface
        self.__menu_list = ["Skrá viðskiptavin", "Fletta upp viðskiptavin", "Afskrá viðskiptavin", 
        "Uppfæra viðskiptavin", "Setja á bannlista", "Taka af bannlista", 
        "Sekta viðskiptavin", "Til baka"]

    def menu(self):
        self.__staff_interface.clear_screen()
        print("Viðskiptavinir")
        print("-"*27)
        
        self.__staff_interface.print_menu(self.__menu_list)
        print("-"*27)
        input_num = input("Val: ")

        if input_num == "1":
            self.__staff_interface.register_customer()
        elif input_num == "2":
            self.find_customer()
        elif input_num == "3":
            self.__staff_interface.deregister_customer()
        elif input_num == "4":
            self.edit_customer()
        elif input_num == "5":
            self.ban_customer()
        elif input_num == "6":
            self.unban_customer()
        elif input_num == "7":
            self.fine_customer()
        elif input_num == "8":
            self.__staff_interface.main_menu()
        else:
            pass
        return self.__staff_interface.go_to_menu()

    def __is_banned(self, email):
        if self.__staff_interface.customer_service.find_customer(email):
            if self.__staff_interface.customer_service.find_customer(email)\
            .is_banned() == "true":
                print("Þessi viðskiptavinur er bannaður")
                return self.__staff_interface.go_to_menu()

    def is_banned(self, email):
        customer = self.__staff_interface.customer_service.find_customer(email)
        if customer:
            return customer.is_banned() == "true"

    def find_by_name(self):

        self.__staff_interface.clear_screen()
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()
        name = self.__staff_interface.error_catch.input_name()
        if not name:
            return self.__staff_interface.go_to_menu()
        self.__staff_interface.clear_screen()

        customer_found_list = self.__staff_interface.customer_service.find_customer(name = name)
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()
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
            choice = int(input("Veldu einn viðskiptavin hér fyrir ofan: ")) - 1 #TODO
            customer_found = customer_found_list[choice]
            return customer_found
        else:
            print("Enginn viðskiptavinur fundinn á þessu nafni")
            choice = input("Viltu reyna aftur (j/n) eða skrá nýjan viðskiptavin (s)?: ")
            if choice.lower() == "j":
                 return self.find_by_name()
            elif choice.lower() == "s":
                return self.__staff_interface.register_customer()
            else:
                self.__staff_interface.go_to_menu()

    def find_by_ssn(self):
        self.__staff_interface.clear_screen()
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()

        customer_found = False
        while customer_found == False:
            ssn = self.__staff_interface.error_catch.input_ssn()
            if not ssn:
                return self.__staff_interface.go_to_menu()

            customer_found = self.__staff_interface.customer_service.find_customer(ssn = ssn)
            if not customer_found:

                choice = input("Kennitala er ekki á skrá, reyndu aftur eða ýttu á s til að skrá nýjan viðskiptavin: ")

                if choice.lower() == "s":
                    return self.__staff_interface.register_customer()
        return customer_found

        
    def find_by_email(self):
        """"
        leitar að vskvini eftir emaili og býður að búa hann til 
        ef hann er ekki til. Skilar vskvininum.
        """
        self.__staff_interface.clear_screen()
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()

        customer_found = False
        while customer_found == False:
            email = self.__staff_interface.error_catch.input_email()
            if not email:
                return self.__staff_interface.go_to_menu()
            customer_found = self.__staff_interface.customer_service.find_customer(email = email)
            if not customer_found:
                self.__staff_interface.clear_screen()
                print("Fletta upp viðskiptavin")
                print("-"*81)
                choice = input("Netfang er ekki á skrá, "
                "reyndu aftur eða ýttu á s til að skrá nýjan viðskiptavin: ")
                if choice.lower() == "s":
                    return self.__staff_interface.register_customer()
        return customer_found

    def find_by_phone_no(self):
        self.__staff_interface.clear_screen()
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()
        phone_no = self.__staff_interface.error_catch.input_phone()
        if not phone_no:
            return self.__staff_interface.go_to_menu()

        self.__staff_interface.clear_screen()

        phone_no_list = self.__staff_interface.customer_service.find_customer(phone_no = phone_no)
        print("Fletta upp viðskiptavin")
        self.__staff_interface.print_divider()
        if not phone_no_list:
            print("Enginn viðskiptavinur fundinn á þessu símanúmeri")
            choice = input("Viltu reyna aftur (j/n) eða skrá nýjan viðskiptavin (s)?: ")
            if choice.lower() == "j":
                 return self.find_by_phone_no()
            elif choice.lower() == "s":
                return self.__staff_interface.register_customer()
            else:
                self.__staff_interface.go_to_menu()
        elif len(phone_no_list) == 1:
            customer_found = phone_no_list[0]
            return customer_found
        elif len(phone_no_list) > 1:
            index = 1
            for customer in phone_no_list:
                print("{}. {}".format(index, customer))
                if index < len(phone_no_list):
                    print()
                index += 1
            print("-"*(50))
            choice = int(input("Veldu einn viðskiptavin hér fyrir ofan: ")) - 1 #TODO
            customer_found = phone_no_list[choice]
            return customer_found            
    
    def find_customer(self):
        customer_found = self.__staff_interface.find_customer_menu()
        self.__staff_interface.clear_screen()
        print("Fletta upp viðskiptavin")
        print("-"*(33+len(customer_found.get_name())))
        print(customer_found)
        print("-"*(33+len(customer_found.get_name())))
        choice = input("Viltu breyta viðskiptavin? (j/n): ")
        print("-"*(33+len(customer_found.get_name())))


        if choice.lower() == "j":
            self.edit_customer(customer_found)

    def edit_customer(self, customer_found=0 ):
        """Tekur við customer object, leitar að viðskiptavini ef enginn 
        customer er sendur inn. Breytir svo customernum"""
        if customer_found != 0:
            customer = customer_found
        else:
            customer = self.__staff_interface.find_customer_menu()

        self.__staff_interface.clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*(7+len(customer.get_email())))
        print(customer)
        print("-"*(7+len(customer.get_email())))
        print("Hverju viltu breyta?: ")
        print("-"*(7+len(customer.get_email())))
        menu_list = ["Símanúmeri", "Netfangi", "Kortanúmeri"]
        self.__staff_interface.print_menu(menu_list)
        print("-"*(7+len(customer.get_email())))
        val = input("Val: ")
        print("-"*(7+len(customer.get_email())))

        if val == "1":
            self.change_phone_no(customer)
        elif val == "2":
            self.change_email(customer)
        elif val == "3":
            self.change_card_no(customer)
        elif val == "4":
            print("-"*(6+len(customer.get_email())))

    def change_phone_no(self, customer):
        email = customer.get_email()
        self.__staff_interface.clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*30)
        print("Stimplið inn nýtt símanúmer.")
        #phone_no = input("Nýtt Símanúmer: ")
        #print("-"*30)
        phone_no = self.__staff_interface.error_catch.input_phone()
        if not phone_no:
            return self.__staff_interface.go_to_menu()
        #if self.error_catch.check_phone_no(phone_no):
        self.__staff_interface.customer_service.edit_customer_phone_no(\
        email, phone_no)
        print("Símanúmeri hefur verið breytt.")
        print("-"*30)

    def change_email(self, customer):
        self.__staff_interface.clear_screen()
        old_email = customer.get_email()
        print("Uppfæra viðskiptavin")
        print("-"*40)
        print("Stimplið inn nýtt netfang.")
        #netfang = input("Nýtt netfang: ")
        #print("-"*40)
        new_email = self.__staff_interface.error_catch.input_email()
        if not new_email:
            return self.__staff_interface.go_to_menu()
        orders_list = self.__staff_interface.order_service.\
        get_customer_orders(old_email)
        if orders_list:
            for order in orders_list:
                self.__staff_interface.order_service.change_email(new_email, order)
        self.__staff_interface.customer_service.edit_customer_email(old_email, new_email)
        print("Netfangi hefur verið breytt.")
        print("-"*40)

    def change_card_no(self, customer):
        email = customer.get_email()
        self.__staff_interface.clear_screen()
        print("Uppfæra viðskiptavin")
        print("-"*(62))
        print("Stimplið inn nýtt kortanúmer.")
        card_no = self.__staff_interface.error_catch.input_card()
        if not card_no:
            self.__staff_interface.go_to_menu()
        #kortanumer = self.card_input()
        #print("-"*(62))
        self.__staff_interface.customer_service.edit_customer_card_no(email,card_no)
        print("Kortanúmeri hefur verið breytt.")
        print("-"*(62))
        

    def ban_customer(self):
        self.__staff_interface.clear_screen()
        print("Setja á bannlista")
        self.__staff_interface.print_divider()
        customer = self.__staff_interface.find_customer_menu()
        self.__staff_interface.clear_screen()

        print("Setja á bannlista")
        print("-"*(31 + len(customer.get_name()) + len(customer.get_email())))
        if customer:
            stadfesta = input("Setja á bannlista: {}, {}? (j/n): ".format(\
            customer.get_name(), customer.get_email()))
            if stadfesta == "j":
                self.__staff_interface.customer_service.ban_customer(customer.get_email())
                print("{} hefur verið færður á bannlista.".format(\
                customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fannst ekki")
        
    def unban_customer(self):
        self.__staff_interface.clear_screen()
        print("Taka af bannlista")
        self.__staff_interface.print_divider()
        customer = self.__staff_interface.find_customer_menu()
        self.__staff_interface.clear_screen()

        print("Taka af bannlista")
        print("-"*(31 + len(customer.get_name()) + len(customer.get_email())))
        if customer:
            stadfesta = input("Taka af bannlista: {}, {}? (j/n): ".\
                format(customer.get_name(), customer.get_email()))
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
            if stadfesta == "j":
                self.__staff_interface.customer_service.unban_customer(customer.get_email())
                print("{} hefur verið tekinn af bannlista.".\
                    format(customer.get_name()))
            else:
                print("Hætt við.")
            print("-"*(31 + len(customer.get_name()) + len(customer.\
                get_email())))
        else:
            print("Notandi fannst ekki")

    def fine_customer(self):
        self.__staff_interface.clear_screen()
        print("Sekta viðskiptavin")
        self.__staff_interface.print_divider()
        customer = self.__staff_interface.find_customer_menu()
        self.__staff_interface.clear_screen()

        print("Sekta viðskiptavin")
        if customer:
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))
            stadfesta = input("Sekta: {}, {}? (j/n): "\
            .format(customer.get_name(), customer.get_email()))
            print("-"*(19 + len(customer.get_name()) + len(customer.\
                get_email())))

            if(stadfesta.lower() == "j"):
                fine_amount = self.__staff_interface.error_catch\
                .integer_input("Upphæð sektar (kr)")
                self.__staff_interface.customer_service.fine_customer(customer.get_email(),\
                    fine_amount)
                print("{} hefur verið sektaður um {} kr.".\
                    format(customer.get_name(), fine_amount))
            else:
                print("Hætt við.")

            num_chars = 19 + len(customer.get_name()) + len(customer.get_email())
            self.__staff_interface.print_divider(num_chars)
        else:
            print("Notandi fannst ekki")