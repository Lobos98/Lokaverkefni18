from repositories.CarRepo import CarRepo
from models.Car import Car

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def find_car(self, reg_num):
        ###finnur bíl og skilar tilviki af Car klasanum
        cars = self.__car_repo.get_all_cars()
        for car in cars:
            if car[0] == reg_num:
                found_car = Car(car[0], car[1], car[2], car[3], car[4], car[5], car[6])
                return found_car
    
    def log_broken_car(self):
        ###Find car and mark as broken
        pass

    def log_new_car(self):
        pass

    def delete_car(self):
        pass