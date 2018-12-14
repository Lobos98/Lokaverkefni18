class CustomerInterface:
    def __init__(self, staff_interface):
        self.__staff_interface = staff_interface
        self.__menu_list = ["Skrá viðskiptavin", "Fletta upp viðskiptavin",\
        "Afskrá viðskiptavin", 
        "Uppfæra viðskiptavin", "Setja á bannlista", "Taka af bannlista", 
        "Sekta viðskiptavin", "Prenta leigusögu viðskiptavinar","Til baka"]
        self.__print_lines = self.__staff_interface.print_divider
        self.__clear_screen = self.__staff_interface.clear_screen

    def menu(self):
        self.__clear_screen()
        print("Viðskiptavinir")
        self.__print_lines(31)
        
        self.__staff_interface.print_menu(self.__menu_list)
        self.__print_lines(31)
        input_num = input("Val: ")

        if input_num == "1":
            self.__staff_interface.register_customer()
        elif input_num == "2":
            self.find_customer()
        elif input_num == "3":
            self.__staff_interface.deregister_customer()
        elif input_num == "4":
            self.__staff_interface.edit_customer()
        elif input_num == "5":
            self.ban_customer()
        elif input_num == "6":
            self.unban_customer()
        elif input_num == "7":
            self.fine_customer()
        elif input_num == "8":
            self.print_past_orders()
        elif input_num == "9":
            self.__staff_interface.main_menu()
        else:
            pass
        return self.__staff_interface.go_to_menu()

    def is_banned(self, email):
        customer = self.__staff_interface.customer_service.find_customer(email)
        return customer.is_banned()

    def find_by_name(self):
        """"
        leitar að vskvini eftir nafnstrengi og býður að búa hann til 
        ef hann er ekki til. Skilar lista af vskvininum sem hafa 
        nafnstrenginn í nafninu sínu.
        """
        self.__clear_screen()
        print("Fletta upp viðskiptavin")
        self.__print_lines()
        name = self.__staff_interface.error_catch.input_name()
        if not name:
            return self.__staff_interface.go_to_menu()
        self.__clear_screen()

        customer_found_list = self.__staff_interface.customer_service.\
        find_customer(name = name)
        print("Fletta upp viðskiptavin")
        self.__print_lines()
        if not customer_found_list:
            print("Enginn viðskiptavinur fundinn á þessu nafni")
            choice = input("Viltu reyna aftur (j/n) eða skrá nýjan viðskiptavin "
                "(s)?: ")
            if choice.lower() == "j":
                 return self.find_by_name()
            elif choice.lower() == "s":
                return self.__staff_interface.register_customer()
            else:
                self.__staff_interface.go_to_menu()
        else:
            return customer_found_list

    def select_customer(self, list_of_customers):
        """
        Tekur inn lista af customer objects, prentar vskvinina út og
        býður manni að velja einn ef það eru fleiri en einn.
        Skilar customer object.
        """
        if len(list_of_customers) == 1:
            customer_found = list_of_customers[0]
            print("Viðskiptavinurinn {} hefur verið valinn".format(\
            customer_found.get_name()))
            self.__print_lines()
            return customer_found
        elif len(list_of_customers) > 1:

            for index, customer in enumerate(list_of_customers):
                print("{}. {}".format(index + 1, customer))
                if index < len(list_of_customers)-1:
                    print()
            self.__staff_interface.print_divider()
            choice = self.__staff_interface.error_catch.integer_input\
            ("Vinsamlegast veldu viðskiptavin hér fyrir ofan: ",
            len(list_of_customers))
            customer_found = list_of_customers[choice - 1]
            print("Viðskiptavinurinn {} hefur verið valinn".format(\
            customer_found.get_name()))
            self.__print_lines()
            return customer_found
            

    def find_by_ssn(self):
        """"
        leitar að vskvini eftir kennitölu og býður að búa hann til 
        ef hann er ekki til. Skilar vskvininum.
        """
        self.__clear_screen()
        print("Fletta upp viðskiptavin")
        self.__print_lines()

        customer_found = False
        while customer_found == False:
            ssn = self.__staff_interface.error_catch.input_ssn()
            if not ssn:
                return self.__staff_interface.go_to_menu()

            customer_found = self.__staff_interface.customer_service.\
            find_customer(ssn = ssn)
            if not customer_found:

                choice = input("Kennitala er ekki á skrá, reyndu aftur eða ýttu á "
                    "s til að skrá nýjan viðskiptavin: ")

                if choice.lower() == "s":
                    return self.__staff_interface.register_customer()
        return customer_found

        
    def find_by_email(self):
        """"
        leitar að vskvini eftir emaili og býður að búa hann til 
        ef hann er ekki til. Skilar vskvininum.
        """
        self.__clear_screen()
        print("Fletta upp viðskiptavin")
        self.__print_lines()

        customer_found = False
        while customer_found == False:
            email = self.__staff_interface.error_catch.input_email()
            if not email:
                return self.__staff_interface.go_to_menu()
            customer_found = self.__staff_interface.customer_service.\
            find_customer(email=email)
            if not customer_found:
                self.__clear_screen()
                print("Fletta upp viðskiptavin")
                self.__print_lines(81)
                choice = input("Netfang er ekki á skrá, "
                "reyndu aftur eða ýttu á s til að skrá nýjan viðskiptavin: ")
                if choice.lower() == "s":
                    return self.__staff_interface.register_customer()
        return customer_found

    def find_by_phone_no(self):
        """"
        leitar að vskvini eftir snr og býður að búa hann til 
        ef hann er ekki til. Skilar lista af vskvinum sem nota þetta snr.
        """
        self.__clear_screen()
        print("Fletta upp viðskiptavin")
        self.__print_lines()
        phone_no = self.__staff_interface.error_catch.input_phone()
        if not phone_no:
            return self.__staff_interface.go_to_menu()

        self.__clear_screen()

        phone_no_list = self.__staff_interface.customer_service.\
        find_customer(phone_no = phone_no)
        print("Fletta upp viðskiptavin")
        self.__print_lines()
        if not phone_no_list:
            print("Enginn viðskiptavinur fundinn á þessu símanúmeri")
            choice = input("Viltu reyna aftur (j/n) eða skrá nýjan viðskiptavin "
                "(s)?: ")
            if choice.lower() == "j":
                 return self.find_by_phone_no()
            elif choice.lower() == "s":
                return self.__staff_interface.register_customer()
            else:
                self.__staff_interface.go_to_menu()
        
        return phone_no_list
    
    def find_customer(self):
        customer_found = self.__staff_interface.find_customer_menu()
        if not customer_found:
            print("Viðskiptavinur fannst ekki.")
        self.__clear_screen()
        print("Fletta upp viðskiptavin")
        name_printer = customer_found.get_name()
        self.__print_lines((48+len(name_printer)))
        print(customer_found)
        self.__print_lines((48+len(name_printer)))
        choice = input("Viltu breyta viðskiptavin? (j/n): ")
        self.__print_lines((48+len(name_printer)))

        if choice.lower() == "j":
            self.__staff_interface.edit_customer(customer_found)


    def change_phone_no(self, customer):
        email = customer.get_email()
        self.__clear_screen()
        print("Uppfæra viðskiptavin")
        self.__print_lines(30)
        print("Núverandi símanúmer: {}".format(customer.get_phone_no()))
        phone_no = self.__staff_interface.error_catch.input_phone()
        if not phone_no:
            return self.__staff_interface.go_to_menu()
        self.__staff_interface.customer_service.edit_customer_phone_no(\
        email, phone_no)
        print("Símanúmeri hefur verið breytt.")
        self.__print_lines(30)

    def change_email(self, customer):
        self.__clear_screen()
        old_email = customer.get_email()
        print("Uppfæra viðskiptavin")
        self.__print_lines(40)
        print("Stimplið inn nýtt netfang.")
        new_email = self.__staff_interface.error_catch.input_email()
        if self.__staff_interface.customer_service.find_customer(email=new_email):
            print("Þessi viðskiptavinur er nú þegar til")
            self.__staff_interface.go_to_menu()
        if not new_email:
            return self.__staff_interface.go_to_menu()
        orders_list = self.__staff_interface.order_service.\
        get_customer_orders(old_email)
        if orders_list:
            for order in orders_list:
                self.__staff_interface.order_service.change_email(new_email, order)
        self.__staff_interface.customer_service.edit_customer_email(old_email, 
            new_email)
        print("Netfangi hefur verið breytt.")
        self.__print_lines(40)

    def change_card_no(self, customer):
        email = customer.get_email()
        self.__clear_screen()
        print("Uppfæra viðskiptavin")
        self.__print_lines((62))
        print("Stimplið inn nýtt kortanúmer.")
        card_no = self.__staff_interface.error_catch.input_card()
        if not card_no:
            self.__staff_interface.go_to_menu()
        self.__staff_interface.customer_service.edit_customer_card_no(email,card_no)
        print("Kortanúmeri hefur verið breytt.")
        self.__print_lines((62))
        
    def ban_customer(self):
        self.__clear_screen()
        print("Setja á bannlista")
        self.__print_lines()
        customer = self.__staff_interface.find_customer_menu()
        self.__clear_screen()

        print("Setja á bannlista")
        name = customer.get_name()
        email = customer.get_email()
        self.__print_lines(31 + len(name) + len(email))
        if customer:
            stadfesta = input("Setja á bannlista: {}, {}? (j/n): ".format(\
            name, email))
            if stadfesta == "j":
                self.__staff_interface.customer_service.ban_customer(email)
                print("{} hefur verið færður á bannlista.".format(name))
            else:
                print("Hætt við.")
            self.__print_lines(31 + len(name) + len(customer\
                .get_email()))
        else:
            print("Notandi fannst ekki")
        
    def unban_customer(self):
        self.__clear_screen()
        print("Taka af bannlista")
        self.__print_lines()
        customer = self.__staff_interface.find_customer_menu()
        self.__clear_screen()

        print("Taka af bannlista")
        name = customer.get_name()
        email = customer.get_email()
        self.__print_lines((31 + len(name) + len(email)))
        if customer:
            stadfesta = input("Taka af bannlista: {}, {}? (j/n): ".\
                format(name, email))
            self.__print_lines((31 + len(name) + len(customer.\
                get_email())))
            if stadfesta == "j":
                self.__staff_interface.customer_service.unban_customer(email)
                print("{} hefur verið tekinn af bannlista.".\
                    format(name))
            else:
                print("Hætt við.")
            self.__print_lines((31 + len(name) + len(email)))
        else:
            print("Notandi fannst ekki")

    def fine_customer(self):
        self.__clear_screen()
        print("Sekta viðskiptavin")
        self.__print_lines()
        customer = self.__staff_interface.find_customer_menu()
        self.__clear_screen()

        print("Sekta viðskiptavin")
        name = customer.get_name()
        email = customer.get_email()
        if customer:
            self.__print_lines((19 + len(name) + len(customer.\
                get_email())))
            stadfesta = input("Sekta: {}, {}? (j/n): "\
            .format(name, email))
            self.__print_lines((19 + len(name) + len(customer.\
                get_email())))

            if(stadfesta.lower() == "j"):
                fine_amount = self.__staff_interface.error_catch\
                .integer_input("Upphæð sektar (kr): ")
                self.__staff_interface.customer_service.fine_customer(email,\
                    fine_amount)
                print("{} hefur verið sektaður um {} kr.".\
                    format(name, fine_amount))
            else:
                print("Hætt við.")

            num_chars = 19 + len(name) + len(email)
            self.__print_lines(num_chars)
        else:
            print("Notandi fannst ekki")

    def print_past_orders(self):
        found_customer = self.__staff_interface.find_customer_menu()
        if not found_customer:
            print("Viðskiptavinur fannst ekki.")
            self.__staff_interface.go_to_menu()
        self.__clear_screen()
        if found_customer.get_history == []:
            print("Viðskiptavinur hefur ekki leigt bíl áður")
        else:
            name = found_customer.get_name()
            print("Leigusaga viðskiptavinar {}".format(name))
            self.__print_lines(61)
            order_list = self.__staff_interface.order_service.get_customers_past_orders(found_customer)
            self.__staff_interface.print_orders(order_list)
            self.__print_lines(61)