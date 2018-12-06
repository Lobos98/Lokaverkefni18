from repositories.CarRepo import CarRepo
from models.Car import Car
from datetime import datetime

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()
        self.__price_list = {"jeppi": 5000, "folksbill": 4000, "smabill": 3000}

    def get_price(self, car):
        """Tekur við Car object og skilar verðinu á bílnum"""
        return self.__price_list[car.get_type()]

    def find_car(self, reg_num):
        """ tekur við bílnúmeri AAX99, finnur bíl og skilar\
        tilviki af Car klasanum"""
        cars = self.__car_repo.get_all_cars()
        for car in cars:
            if car.get_reg_num() == reg_num:
                found_car = car
                return found_car
            else:
                return False
    
    def log_broken_car(self, reg_num):
        """ Finnur bíl, fjarlægir hann úr gagnagrunni,\
        breytir ástandinu og skrifar hann aftur í gagnagunninn """
        car_to_be_changed = self.find_car(reg_num)
        if car_to_be_changed == False:
            return False
        self.__car_repo.delete_car(car_to_be_changed)
        car_to_be_changed.change_broken_status()
        self.__car_repo.add_car(car_to_be_changed)
        pass

    def log_new_car(self, reg_num, model, type, color):
        """Býr til nýtt instance af Car klasanum og sendir til CarRepo.\
        Skilar False ef bíllinn er þegar til"""
        if self.find_car(reg_num) == False:
            new_car = Car(reg_num, model, type, color)
            self.__car_repo.add_car(new_car)
        else:
            return False

    def delete_car(self, reg_num):
        """Leitar að bíl eftir bílnúmeri og eyðir honum
        skilar False ef bíllinn er ekki í skránni"""
        car_to_be_deleted = self.find_car(reg_num)
        if car_to_be_deleted == False:
            return False
        self.__car_repo.delete_car(car_to_be_deleted)

    def find_free_cars(self, date_string_1, date_string_2):
        """Tekur við 2 dags.str. á forminu ddmmáááá og skilar lista\
        af lausum bílum á tímabilinu """
        pickup_date = datetime.strptime(date_string_1, "%d%m%Y")
        return_date = datetime.strptime(date_string_2, "%d%m%Y")
        car_list = self.__car_repo.get_all_cars()
        free_car_list = [car for car in car_list]
        for car in car_list:
            reservations = car.get_reserved_dates()
            for date_tuple in reservations:
                if  date_tuple[0] <= pickup_date <= date_tuple[1]:
                    free_car_list.remove(car)
                elif date_tuple[0] <= return_date <= date_tuple[1]:
                    free_car_list.remove(car)
                elif pickup_date <= date_tuple[0] and date_tuple[1] <= return_date:
                    free_car_list.remove(car)
        return free_car_list

    def get_rented_cars(self):
        """Skilar lista af bílum sem eru í útleigu í augnablikinu"""
        list_of_cars = self.__car_repo.get_all_cars()
        rented_cars = []
        for car in list_of_cars:
            reserved_dates = car.get_reserved_dates()
            for date_tuple in reserved_dates:
                if date_tuple[0]< datetime.today() < date_tuple[1]:
                    rented_cars.append(car)
        return rented_cars