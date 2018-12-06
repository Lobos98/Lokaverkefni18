from repositories.CarRepo import CarRepo
from models.Car import Car

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def find_car(self, reg_num):
        """ finnur bíl og skilar tilviki af Car klasanum"""
        # Ath bug - returnar none ef bíllinn finnst ekki
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