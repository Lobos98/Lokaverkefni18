from models.Car import Car
import datetime
import csv


class CarRepo:
    def __init__(self):
        self.__cars = []
        self.__filepath = "Data\list_of_cars.csv"

    def get_all_cars(self):
        """Skilar lista af Car objects sem eru skráð hjá okkur"""
        if self.__cars == []:
           
            file = open(self.__filepath, newline='')
            file_contents = csv.reader(file)
            self.__header = next(file_contents)
            for line in file_contents:
                # line = reg_number, model, car_type, color, 
                # broken, history, future_reservations
                reg_number = line[0]
                model = line[1]
                car_type = line[2]
                color = line[3]
                broken = self.__get_broken(line[4])
                list_of_histories_by_customer = line[5].split("--")
                if list_of_histories_by_customer == [""]:
                    history_dict = {}
                else:
                    history_dict = self.__get_history_dict(\
                    list_of_histories_by_customer)

                list_of_reserved_date_strings = line[6].split(";")
                if list_of_reserved_date_strings == [""]:
                    reserved_dates_list = []
                else:
                    reserved_dates_list = self.__get_reserved_dates_list(\
                    list_of_reserved_date_strings)
                car_to_add = Car(reg_number, model, car_type, color, \
                broken, history_dict, reserved_dates_list)
                self.__cars.append(car_to_add)
            file.close()
            return self.__cars
        else:
            return self.__cars

    def __get_broken(self, bool_string):
        """Tekur við streng úr 4. dálki gagnanna okkar og skilar 
        boolean gildi True eða False"""
        if bool_string == "False":
            return False
        elif bool_string == "True":
            return True

    def __get_history_dict(self, history_list):
        """Tekur við lista úr 5. dálki gagnanna þar sem hvert stak er á forminu
        kúnni@net.is:ddmmáááá/ddmmáááá;ddmmáááá/áááá;... og skilar dict þar sem
        lyklarnir eru netföng og gildi lykilsins er listi af túplum þar sem 
        hver túpla inniheldur leigu- og skiladagsetningu"""
        history_dict = {}
        for driver_and_dates in history_list:
            driver, dates = driver_and_dates.split(":")
            history_dict[driver] = self.__fill_date_list(dates)
        return history_dict

    def __fill_date_list(self, date_string):
        """Tekur við streng af dagsetningum á forminu 
        ddmmáááá/ddmmáááá;ddmmáááá/áááá;... og skilar lista af túplum þar sem
        hver túpla inniheldur leigu- og skiladagsetningu"""
        date_tuple_list = []
        list_of_pickup_return_dates = date_string.split(";")
        for date_combo in list_of_pickup_return_dates:
            date_tuple = self.__read_dates(date_combo)
            date_tuple_list.append(date_tuple)
        return date_tuple_list

    def __read_dates(self, date_string):
        """Tekur við streng á forminu ddmmáááá/ddmmáááá og skilar túplu með
        tveimur datetime objects"""
        pickup_date_string , return_date_string = date_string.split("/")
        pickup_date = self.__string_to_datetime_converter(pickup_date_string)
        return_date = self.__string_to_datetime_converter(return_date_string)
        return (pickup_date, return_date)

    def __string_to_datetime_converter(self, date_string):
        return datetime.datetime.strptime(date_string, "%d%m%Y")
    
    def __get_reserved_dates_list(self, list_of_reserved_date_strings):
        """Tekur við lista þar sem hvert stak er á forminu ddmmáááá/ddmmáááá
        og skilar lista þar sem hvert stak er túpla með tveimur datetime obj"""
        reserved_dates = []
        for date_combo in list_of_reserved_date_strings:
            date_tuple = self.__read_dates(date_combo)
            reserved_dates.append(date_tuple)
        return reserved_dates

    def find_car(self, reg_num):
        for car in self.__cars:
            if reg_num == car.get_reg_num():
                return car
        return False

    def add_car(self, car):
        self.__cars.append(car)
        file = open(self.__filepath, "a")
        reg_num = car.get_reg_num()
        model = car.get_model()
        car_type = car.get_type()
        color = car.get_color()
        broken = str(car.get_broken())
        history_dict = car.get_history()
        history = ""
        for key in history_dict:
            history += key
            history += ":"
            for pickup_return_date_tuple in history_dict[key]:
                pickup_date = pickup_return_date_tuple[0]
                return_date = pickup_return_date_tuple[1]
                history += str(pickup_date.strftime("%d%m%Y"))
                history += "/"
                history += str(return_date.strftime("%d%m%Y"))
                history += ";"
            history = history[:-1] 
            #Þetta er til að fjarlægja síðasta ; delimiterinn
            history += "--"
        history = history[:-2]
        #Þetta er til að fjarlægja síðasta -- delimiterinn
        reserved_dates_list = car.get_reserved_dates()
        reserved_dates = ""
        for reservation in reserved_dates_list:
            pickup_date = reservation[0]
            return_date = reservation[1]
            reserved_dates += pickup_date.strftime("%d%m%Y")
            reserved_dates += "/"
            reserved_dates += return_date.strftime("%d%m%Y")
            reserved_dates += ";"
        reserved_dates = reserved_dates[:-1]
        

        attributes = (reg_num, model, car_type, color, broken, \
        history, reserved_dates)
        line_to_append = ",".join(attributes)
        file.write("\n" + line_to_append)
        file.close()

    def delete_car(self, car):
        self.__cars.remove(car)
        file_path = "./Data/list_of_cars.csv"
        file = open(file_path, newline='')
        file_contents = csv.reader(file)
        r_string = ''
        for line in file_contents:
            if line[0] != car.get_reg_num():
                r_string += ",".join(line) + "\n"
        r_string = r_string.strip("\n")
        file.close()
        file = open(file_path, "w")
        file.write(r_string)
        file.close()