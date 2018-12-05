from models.Car import Car
import csv


class CarRepo:
    def __init__(self):
        self.get_all_cars()
        self.car_object_list = []
        for line in self.data:
            if line[0] == "Bilnumer":
                pass
            interim_car = Car(*line)
            self.car_object_list.append(interim_car)   

    def get_all_cars(self):
        file_path = "Data\list_of_cars.csv"
        file = open(file_path, newline='')
        file_contents = csv.reader(file)
        self.__header = next(file_contents)
        self.data = []
        # row = [reg_number, model, type, color, 
        # broken, history, reserved_dates]
        self.data.append(self.__header)
        for line in file_contents:
            reg_number = line[0]
            model = line[1]
            car_type = line[2]
            color = line[3]
            broken = bool(line[4])
            try:
                history_list = line[5].split("--")
                history_list = [pair.split(":") for pair in history_list]
                history_dict = {driver: time_rented \
                for (driver, time_rented) in history_list}
            except:
                history_dict = line[5]

            try:
                reserved_dates_list = line[6].split("--")
                reserved_dates_list = [pair.split(":") \
                for pair in reserved_dates_list]
                reserved_dates_dict = {date_rented: date_returned \
                for (date_rented, date_returned) in reserved_dates_list}
            except:
                reserved_dates_dict = line[6]

            self.data.append([reg_number, model, car_type, color, broken, \
            history_dict, reserved_dates_dict])
        file.close()
        return self.data

    def add_car(self, car):
    #def add_car(self, reg_number, model, car_type, color):
        file_path = "./data/list_of_cars.csv"
        file = open(file_path, "a")
        attributes = (car.get_reg_num(), car.get_model(), car.get_type(),\
        car.get_color(), str(car.get_broken()), car.get_history(),\
        car.get_reserved_dates())
        line_to_append = ",".join(attributes)
        file.write("\n" + line_to_append)
        file.close()

    def delete_car(self, car):
        file_path = "./data/list_of_cars.csv"
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