class OrderInterface:
    def __init__(self, staff_interface):
        self.__staff_interface = staff_interface
        self.__menu_list = ["Skrá pöntun", "Breyta pöntun", "Fletta upp pöntun",
        "Bakfæra pöntun", "Prenta allar pantanir", "Til baka"]
        self.__print_lines = self.__staff_interface.print_divider
        self.__clear_screen = self.__staff_interface.clear_screen

    def menu(self):
        self.__clear_screen()
        print("Pantanir")
        self.__print_lines(25)
        
        self.__staff_interface.print_menu(self.__menu_list)
        self.__print_lines(25)
        input_num = input("Val: ")
        if input_num == "1":
            self.__staff_interface.create_order()
        elif input_num == "2":
            self.__staff_interface.change_order()
        elif input_num == "3":
            self.find_order()
        elif input_num == "4":
            self.__staff_interface.delete_order()
        elif input_num == "5":
            self.__clear_screen()
            self.__staff_interface.print_orders(self.__staff_interface.\
                order_service.get_list_of_orders())
        elif input_num == "6":
            self.__staff_interface.main_menu()
        else:
            pass
        return self.__staff_interface.go_to_menu()      
        
    def change_car(self, customer_object):
        email = customer_object.get_email()
        ordered_cars, order_info = self.return_ord_cars_and_info(email)
        order_num = self.order_pick(ordered_cars)
        
        chosen_order = order_info[order_num -1]
        order = ordered_cars[order_num - 1]      
        car = self.__staff_interface.car_service.find_car(order.get_car_reg_num())      
        old_pickup_date = order.get_pickup_date()
        old_return_date = order.get_return_date()

        while True:
            self.__clear_screen()
            free_cars = self.__staff_interface.car_service.\
            find_free_cars(old_pickup_date, old_return_date)
            free_cars_of_same_type = self.__staff_interface.car_service.\
            cars_of_same_type(\
            free_cars, car)
            print("Birta lausa bíla")
            self.__print_lines()
            pickup_print = old_pickup_date.strftime("%d.%m.%Y")
            return_print = old_return_date.strftime("%d.%m.%Y")
            print("Eftirfarandi bílar eru lausir frá {} til {}:".format(\
            pickup_print, return_print))
            self.__staff_interface.display_list_of_cars(free_cars_of_same_type)
            new_car_reg_num = self.__staff_interface.error_catch.input_reg_num()
            if  not new_car_reg_num:
                self.__staff_interface.go_to_menu()

            for a_car in free_cars_of_same_type:
                if a_car.get_reg_num() == new_car_reg_num:
                    print("Þú hefur leigt {}".format(new_car_reg_num))
                    self.__print_lines(60)
                    self.__staff_interface.car_service.remove_order(chosen_order)
                    self.__staff_interface.car_service.add_reservation_dates(a_car,
                        chosen_order)
                    return \
                    self.__staff_interface.order_service.change_order\
                    (order, "2", new_reg_number=new_car_reg_num)
        
        
    def change_date(self, customer_object):
        email = customer_object.get_email()
        print("Breyta Pöntun")
        self.__print_lines(46)
        ordered_cars, order_info = self.return_ord_cars_and_info(email)

        order_num = self.order_pick(ordered_cars)

        car = ordered_cars[order_num - 1]
        pickup_date, return_date, free_cars\
         = self.__staff_interface.display_free_cars()
        if free_cars:
            self.__clear_screen()
            print("Breyta Pöntun")
            self.__print_lines(57)
            free_reg_numbers = [a_car.get_reg_num() for a_car in free_cars]
            reg_num = car.get_car_reg_num()
        else:
            print("Hætt var við")
            return self.__staff_interface.go_to_menu()

        if reg_num in free_reg_numbers:
            vehicle = self.__staff_interface.car_service.find_car(reg_num)
            car_price = self.__staff_interface.car_service.get_price(vehicle)
            price = self.__staff_interface.order_service.calculate_price\
            (car_price, pickup_date, return_date)[1]
            print("Þú hefur breytt dagsetningunni, nýja verðið er: {:,d} Kr".\
                format(price))
            self.__staff_interface.order_service.change_order\
            (car, "1", pickup_date, return_date)
            self.__print_lines(57)
            return self.__staff_interface.go_to_menu
        print("Bíll sem er bundinn pöntun er frátekinn á þessu timabili.")
        choice = input("Viltu reyna aftur? (j/n eða q til að hætta): ")
        if choice.lower() == "n":
            return self.__staff_interface.go_to_menu()
        elif choice.lower() == "j":
            return self.change_date(customer_object)
        else:
            exit()
    
    def return_ord_cars_and_info(self, email):
        print("Breyta Pöntun")
        self.__print_lines(46)
        order_info = self.__staff_interface.order_service.find_order(email)
        ordered_cars = []  
        if order_info:
            for index, order in enumerate(order_info):
                ordered_cars.append(order)
                print("{}. Pöntun á bíl {} frá {} til {}"\
                .format(index + 1,
                order.get_car_reg_num(),
                order.get_pickup_date().strftime("%d.%m.%Y"),
                order.get_return_date().strftime("%d.%m.%Y")))
        self.__print_lines(46)
        return ordered_cars, order_info
        
    def order_pick(self, ordered_cars):
        while True:
            order_num = self.__staff_interface.error_catch.integer_input(
            "Veldu númer pöntunar: ")
            if order_num not in range(1, len(ordered_cars) + 1): 
                print("Vinsamlegast veldu pöntun á listanum")
                order_num = self.__staff_interface.error_catch.integer_input(
                "Veldu númer pöntunar: ")
            else:
                return order_num
    
    def find_order(self):
        self.__clear_screen()
        print("Finna pöntun")
        self.__print_lines(34)
        customer = self.__staff_interface.find_customer_menu()
        email = customer.get_email()
        self.__clear_screen() 
        print("Finna pöntun")
        self.__print_lines(34)
        order_list = self.__staff_interface.order_service.get_customer_orders(email)
        if not order_list:
            print("Það er engin pöntun á þessu netfangi")
            self.__staff_interface.go_to_menu()
        self.__staff_interface.print_orders(order_list)