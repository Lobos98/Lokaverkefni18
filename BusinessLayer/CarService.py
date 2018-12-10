from repositories.CarRepo import CarRepo
from models.Car import Car
from datetime import datetime

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def get_price(self, car):
        """Tekur við Car object og skilar verðinu á bílnum"""
        return car.get_price()

    def find_car(self, reg_num):
        """ tekur við bílnúmeri t.d. AAX99, finnur bíl og skilar
        tilviki af Car klasanum, skilar False ef bíll finnst ekki"""
        all_cars = self.__car_repo.get_all_cars()
        for car in all_cars:
            if car.get_reg_num() == reg_num:
                found_car = car
                return found_car
        return False
    
    # def log_broken_car(self, reg_num):
    #     """ Finnur bíl, fjarlægir hann úr gagnagrunni,
    #     breytir ástandinu og skrifar hann aftur í gagnagunninn
    #     skilar False ef bíllinn finnst ekki"""
    #     car_to_be_changed = self.find_car(reg_num)
    #     if car_to_be_changed == False:
    #         return False
    #     self.__car_repo.delete_car(car_to_be_changed)
    #     car_to_be_changed.change_broken_status()
    #     self.__car_repo.add_car(car_to_be_changed)
    #     pass

    def new_car(self, reg_num, model, type, color):
        """Býr til nýtt instance af Car klasanum og sendir til CarRepo.
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

    # def find_free_cars(self, pickup_date, return_date):
    #     """Tekur við 2 dags.str. á forminu ddmmáááá og skilar lista
    #     af lausum bílum á tímabilinu """
    #     pickup_date = datetime.strptime(pickup_date, "%d%m%Y")
    #     return_date = datetime.strptime(return_date, "%d%m%Y")
        
    #     car_list = self.__car_repo.get_all_cars()
    #     free_car_list = [car for car in car_list]
    #     for car in car_list:
    #         reservations = car.get_reserved_dates()
    #         for from_date, to_date = car.get_reserved_dates()
    #         for date_tuple in reservations:
    #             if  date_tuple[0] <= pickup_date <= date_tuple[1]:
    #                 free_car_list.remove(car)
    #             elif date_tuple[0] <= return_date <= date_tuple[1]:
    #                 free_car_list.remove(car)
    #             elif pickup_date <= date_tuple[0] and date_tuple[1] <= return_date:
    #                 free_car_list.remove(car)
    #     for car in free_car_list:
    #         if car.get_broken() == True:
    #             free_car_list.remove(car)
    #     return free_car_list

    def find_free_cars(self, wanted_pickup_date, wanted_return_date):
        """Tekur við 2 dags.str. á forminu ddmmáááá og skilar lista
        af lausum bílum á tímabilinu """

        wanted_pickup_date = datetime.strptime(wanted_pickup_date, "%d%m%Y")
        wanted_return_date = datetime.strptime(wanted_return_date, "%d%m%Y")

        free_car_list = []

        for car in self.__car_repo.get_all_cars():
            reserved_dates = [date for date_tuple in car.get_reserved_dates() for date in date_tuple]
            dates_ok = [not (wanted_pickup_date < date < wanted_return_date) for date in reserved_dates]
            if all(dates_ok) and not car.get_broken():
                free_car_list.append(car)

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

    def return_car(self, order):
        """Tekur við order object, finnur bílinn sem samsvarar pöntuninni og
        færir pöntunina sem er í gangi í history. Skilar bílnúmerinu"""
        reg_num = order.get_car_reg_num()
        car_to_be_returned = self.find_car(reg_num)
        self.__car_repo.delete_car(car_to_be_returned)
        car_to_be_returned.add_to_history(order)
        self.__car_repo.add_car(car_to_be_returned)
        return reg_num

    def add_car(self, reg_num, model, type, color):
        new_car = Car(reg_num, model, type, color)
        self.__car_repo.add_car(new_car)

        
    def make_reservation(self, car):
        self.delete_car(car.get_reg_num())
        self.__car_repo.add_car(car)
    
    def get_broken_cars(self):
        car_list = self.__car_repo.get_all_cars()
        broken_car_list = []
        for car in car_list:
            if car.get_broken():
                broken_car_list.append(car)
        return broken_car_list