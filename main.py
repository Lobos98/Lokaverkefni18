from ui.StaffInterface import StaffInterface
from services.CarService import CarService

service = CarService()
car = service.find_car("MAT69")
print(car.__repr__())
service.log_broken_car("MAT69")
car = service.find_car("MAT69")
print(car.__repr__())

def main():
    print()
    print("Velkomin í Bílaleiguna IceCarRentals.")
    print("-"*37)
    n = 7
    print("{}        _______".format(" "*n))
    print("{}       //  ||\ \ ".format(" "*n))
    print("{}  ____//___||_\ \__".format(" "*n))
    print("{} )  _          _    \ ".format(" "*n))
    print("{} |_/ \________/ \___|".format(" "*n))
    print("{}___\_/________\_/_____".format(" "*n))
    print("{}Drive cheap, not safe!".format(" "*n))
    print("-"*37)
    answer = input("Keyra forrit? (j/n): ")
    if answer.lower() == "j":
        staff = StaffInterface()
        staff.main_menu()
    else:
        pass

main()