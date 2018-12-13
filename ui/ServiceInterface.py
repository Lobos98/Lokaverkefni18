from datetime import datetime

class ServiceInterface:
    def __init__(self, staff_interface):
        self.__staff_interface = staff_interface

        self.__menu_list = ["Birta lausa bíla", "Skrá nýjan viðskiptavin", 
        "Skrá pöntun", "Kostnaðarmat", "Skila bíl", 
        "Afskrá viðskiptavin", "Bakfæra pöntun", "Uppfæra viðskiptavin",
        "Breyta pöntun", "Til baka"]
        self.__print_lines = self.__staff_interface.print_divider

    def menu(self):
        self.__staff_interface.clear_screen()
        print("Afgreiðsla")
        self.__print_lines(27)
        
        self.__staff_interface.print_menu(self.__menu_list)
        self.__print_lines(27)
        input_num = input("Val: ")

        if input_num == "1":
            self.__staff_interface.display_free_cars()
        elif input_num == "2":
            self.__staff_interface.register_customer()
        elif input_num == "3":
            self.__staff_interface.create_order()
        elif input_num == "4":
            self.cost_amount()
        elif input_num == "5":
            self.__staff_interface.return_car()
        elif input_num == "6":
            self.__staff_interface.deregister_customer()
        elif input_num == "7":
            self.__staff_interface.delete_order()
        elif input_num == "8":
            self.__staff_interface.edit_customer()
        elif input_num == "9":
            self.__staff_interface.change_order()
        elif input_num == "10":
            self.__staff_interface.main_menu()
        else:
            pass
        return self.__staff_interface.go_to_menu()

    def cost_amount(self):
        pickup_date, return_date = self.__staff_interface.error_catch.\
        input_rental_dates()
        car_type_list = ["jeppi", "smabill", "folksbill", \
        "husbill", "sportbill"]
        car_dict = {"jeppi":5000, "folksbill":4000, "smabill":3000, \
        "husbill":6000, "sportbill":7000}
        while True:
            try:
                print("1.  Jeppi")
                print("2.  Smábíll")
                print("3.  Fólksbíll")
                print("4.  Húsbíll")
                print("5.  Sportbíll")
                car_type = int(input("Veldu tegund bíls: "))
                if car_type in range(1,6):
                    car = car_type_list[car_type-1]
                else:
                    raise ValueError
            except (IndexError, ValueError):
                print("Vinsamlegast sláðu inn heiltölu á bilinu 1-5.")
            else:
                break
        time_d = datetime.strptime(return_date, "%d%m%Y")\
        - datetime.strptime(pickup_date, "%d%m%Y")
        price = (time_d.days + 1) * car_dict[car]
        print("Verð á völdu tímabili: {:,d} kr".format(price))

        choice = input("Viltu leigja bíl? (j/n): ")
        if choice.lower() == "j":
            return self.__staff_interface.create_order()
        else:
            return self.__staff_interface.go_to_menu()