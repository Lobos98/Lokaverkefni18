class VehicleInterface:

    def __init__(self, staff_interface):
        self.__staff_interface = staff_interface

        self.__menu_list = ["Birta lausa bíla", "Birta bíla í útleigu",
        "Skila bíl", "Skrá bíl", "Afskrá bíl", "Leita að bíl",
        "Bilaðir bílar", "Birta alla bíla", "Til baka"]
        self.__print_lines = self.__staff_interface.print_divider
        self.__clear_screen = self.__staff_interface.clear_screen

    def menu(self):
        """Setur bíla-valmyndina í gang"""
        self.__clear_screen()
        print("Bílafloti")
        self.__print_lines(24)
        
        self.__staff_interface.print_menu(self.__menu_list)
        self.__print_lines(24)
        input_num = input("Val: ")
        if input_num == "1":
            self.__staff_interface.display_free_cars()
        elif input_num == "2":
            self.display_currently_rented_cars()
        elif input_num == "3":
            self.__staff_interface.return_car()
        elif input_num == "4":
            self.add_car()
        elif input_num == "5":
            self.delete_car()
        elif input_num == "6":
            self.print_car()
        elif input_num == "7":
            self.broken_cars()
        elif input_num == "8":
            self.__staff_interface.display_list_of_cars(self.\
                __staff_interface.car_service.find_free_cars("01012100", "01012100"))
        elif input_num == "9":
            self.__staff_interface.main_menu()
        else:
            pass
        return self.__staff_interface.go_to_menu()

    def print_car_header(self):
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(\
        "Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))

    def display_currently_rented_cars(self):
        """Sækir lista af bílum sem eru í útleigu 
        í augnablikinu og prentar þá"""
        self.__clear_screen()
        print("Eftirfarandi bílar eru í útleigu í augnablikinu")
        self.__staff_interface.print_divider()
        self.print_car_header()
        self.__staff_interface.print_divider()
        rented_car_list = self.__staff_interface.car_service.get_rented_cars()
        for car in rented_car_list:
            print(car)
        self.__staff_interface.print_divider()

    def add_car(self):
        """Biður um bílnúmer, árgerð, tegund og lit bíls, 
        sendir svo þessar upplýsingar til CarService sem sér um að
        búa til Car object. Prentar staðfestingu"""
        self.__clear_screen()
        print("Skrá bíl")
        self.__print_lines()
        reg_num = self.__staff_interface.error_catch.input_reg_num()
        if reg_num:
            model = self.__staff_interface.error_catch.input_model()
            if model:
                car_type = self.__staff_interface.error_catch.input_type()
                color = self.__staff_interface.error_catch.input_color()
                self.__staff_interface.car_service.add_car(reg_num, model,\
                    car_type, color)
                self.__print_lines()
                print("Bíllinn {} hefur verið skráður!".format(reg_num))
                self.__print_lines()
        else:
            print("Hætt var við")
            
    def delete_car(self):
        """Biður um bílnúmer þangað til bíll fæst sem er til í kerfinu.
        sendir svo bílnúmerið í CarService svo bílnum verði eytt.
        Prentar staðfestingu"""
        self.__clear_screen()

        print("Afskrá bíl")
        self.__print_lines()
        car_to_delete = self.__find_car()
        if car_to_delete:
            reg_num = car_to_delete.get_reg_num()
            if car_to_delete.get_reserved_dates() == []:
                self.__staff_interface.car_service.delete_car(reg_num)
                    
                self.__staff_interface.clear_screen()

                print("Afskrá bíl")
                self.__print_lines()
                print("Bíllinn {} hefur verið afskráður!".format(reg_num))
                self.__print_lines()
            else:
                self.__print_lines()
                choice = input("Þessi bíll er frátekinn fyrir viðskiptavin.\n"
                "Ef bílnum er eytt verður tilsvarandi pöntunum einnig eytt.\n"
                "Eyða bíl? (j/n):")
                if choice == "j":
                    self.__staff_interface.car_service.delete_car(reg_num)
                    self.__staff_interface.order_service.car_deleted(reg_num)
                    self.__staff_interface.clear_screen()

                    print("Afskrá bíl")
                    self.__print_lines()
                    print("Bíllinn {} hefur verið afskráður!".format(reg_num))
                    self.__print_lines()
                else:
                    print("Þú hefur hætt við að eyða bílnum {}".format(reg_num))
        else:
            print("Hætt var við")
        

    def print_car(self):
        """Biður um bílnúmer þangað til bíll finnst og 
        prentar svo bílinn á skjáinn"""
        self.__clear_screen()
        print("Leita að bíl")
        self.__print_lines(30)
        car = self.__find_car()
        if car:        
            self.__staff_interface.clear_screen()
            print("Leita að bíl")
            self.__staff_interface.print_divider()
            self.print_car_header()
            self.__staff_interface.print_divider()
            print(car)
            self.__staff_interface.print_divider()
        else:
            print("Hætt var við að leita að bíl.")

    def broken_cars(self):
        """Setur bilaðra-bíla valmyndina í gang"""
        self.__clear_screen()
        print("Bilaðir bílar")
        self.__staff_interface.print_divider(25)
        print("1.  Skrá bilaðan bíl")
        print("2.  Endurskrá bilaðan bíl")
        print("3.  Birta bilaða bíla")
        print("4.  Til baka")
        self.__staff_interface.print_divider(25)
        input_num = input("Val: ")

        if input_num == "1":
            self.log_broken_car()
        elif input_num == "2":
            self.log_car_as_fixed()
        elif input_num == "3":
            self.print_broken_cars()
        elif input_num == "4":
            self.menu()
        return self.__staff_interface.go_to_menu()

    def log_broken_car(self):
        #TODO: ættum kannski að færa virkni fallsins í CarService...
        self.__clear_screen()
        print("Skrá bilaðan bíl")
        self.__print_lines(30)
        car = self.__find_car()
        if car:
            reg_num = car.get_reg_num()
            if car.get_broken() == False:
                car.change_broken_status()
                self.__staff_interface.clear_screen()
                print("Skrá bilaðan bíl")
                self.__print_lines(41 + len(reg_num))
                print("Bíllinn {} hefur verið skráður sem bilaður."\
                .format(reg_num))
                self.__print_lines(41 + len(reg_num))
            else:
                print("Bíllinn {} er þegar bilaður.".format(reg_num))
        else:
            print("Hætt var við")

    def log_car_as_fixed(self):
        #TODO: Ættum kannsk að færa virkni fallsins í CarService...
        self.__clear_screen()
        print("Afskrá bilaðan bíl")
        self.__print_lines(30)
        self.print_broken_cars()
        car = self.__find_car()
        if car:
            reg_num = car.get_reg_num()
            if car.get_broken() == True:
                car.change_broken_status()
                self.__clear_screen()
                print("Afskrá bilaðan bíl")
                self.__print_lines((48 + len(reg_num)))
                print("Bíllinn {} hefur verið lagaður og er skráður á ný."\
                .format(reg_num))
                self.__print_lines((48 + len(reg_num)))
            else:
                print("Bíllinn {} er ekki bilaður.".format(reg_num))
        else:
            print("Hætt var við.")

    def print_broken_cars(self):
        self.__clear_screen()
        print("Bilaðir bílar")
        broken_cars = self.__staff_interface.car_service.get_broken_cars()
        self.__staff_interface.print_divider()
        self.print_car_header()
        self.__staff_interface.print_divider()
        for car in broken_cars:
            print(car)
        self.__staff_interface.print_divider()

    def __find_car(self):
        """Biður um bílnúmer þangað til bíll finnst og skilar car object"""
        car = False
        while car == False:
            reg_num = self.__staff_interface.error_catch.input_reg_num()
            if reg_num == "":
                break
            car = self.__staff_interface.car_service.find_car(reg_num)
            if car == False:
                print("Bíllinn {} finnst ekki.".format(reg_num.upper()))
        return car