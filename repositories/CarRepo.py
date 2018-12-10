from models.Car import Car
import datetime
import csv


class CarRepo:
    def __init__(self):
        self.__cars = []
        self.__filepath = "Data\list_of_cars.csv"

    def get_all_cars(self):
        """Á að skila lista af Car objects"""
        if self.__cars == []:
           
            file = open(self.__filepath, newline='')
            file_contents = csv.reader(file)
            self.__header = next(file_contents)
            for line in file_contents:
                # reg_number, model, car_type, color, broken = line
                reg_number = line[0]
                model = line[1]
                car_type = line[2]
                color = line[3]
                if line[4] == "True":
                    broken = True
                elif line[4] == "False":
                    broken = False
                # Hvað er þessi kóði að gera? Mjög óskýrt.
                # Viljum segja með kóðanum hvað hann gerir.
                history_list = line[5].split("--")
                if history_list == [""]:
                    history_dict = {}
                else:
                    history_dict = {}
                    for driver_dates in history_list:
                        driver = driver_dates.split(":")[0]
                        dates = driver_dates.split(":")[1]
                        history_dict[driver] = []
                        list_of_pickup_return_dates = dates.split(";")
                        for date_combo in list_of_pickup_return_dates:
                            pickup_date_string = date_combo.split("/")[0]
                            return_date_string = date_combo.split("/")[1]
                            pickup_date = datetime.datetime.strptime(\
                            pickup_date_string, "%d%m%Y")
                            return_date = datetime.datetime.strptime(\
                            return_date_string, "%d%m%Y")
                            history_dict[driver].append((pickup_date, return_date))

                reserved_dates_list = []
                reserved_dates_string_list = line[6].split(";")
                if reserved_dates_string_list == [""]:
                    pass
                else:
                    for date_combo in reserved_dates_string_list:
                        pickup_date_string = date_combo.split("/")[0]
                        return_date_string = date_combo.split("/")[1]
                        pickup_date = datetime.datetime.strptime(\
                        pickup_date_string, "%d%m%Y")
                        return_date = datetime.datetime.strptime(\
                        return_date_string, "%d%m%Y")
                        reserved_dates_list.append((pickup_date, return_date))
                car_to_add = Car(reg_number, model, car_type, color, broken, history_dict, reserved_dates_list)
                self.__cars.append(car_to_add)
            file.close()
            return self.__cars
        else:
            return self.__cars

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
        

        attributes = (reg_num, model, car_type, color, broken, history, reserved_dates)
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