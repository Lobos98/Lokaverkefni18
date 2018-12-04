import os
from BusinessLayer.ErrorCatch import ErrorCatch

def cls():
    os.system('cls')


class StaffInterface:

    def main_menu(self):
        cls()
        print("Veldu eitt af eftirfarandi")
        print("-"*len("Veldu eitt af eftirfarandi"))
        print("1.  Viðskiptavinir")
        print("2.  Bílafloti")
        print("3.  Afgreiðsla")
        print("4.  Pantanir")
        print("5.  Hætta")
        print("-"*len("Veldu eitt af eftirfarandi"))
        input_num = input("Val: ")
        print()
        if input_num == "1":
            customer_menu()
        elif input_num == "2":
            vehicle_menu()
        elif input_num == "3":
            service_menu()
        elif input_num == "4":
            order_menu()
        elif input_num == "5":
            exit()
        else:
            print_options()
        
    # def customer_menu(self):
    #     cls()
    #     print("Viðskiptavinir")
    #     print("-"*len("1.  Skrá nýjan viðskiptavin"))
    #     print("1.  Skrá nýjan viðskiptavin")
    #     print("2.  Fletta upp viðskiptavin")
    #     print("3.  Afskrá viðskiptavin")
    #     print("4.  Uppfæra viðskiptavin")
    #     print("5.  Setja á bannlista")
    #     print("6.  Taka af bannlista")
    #     print("7.  Sekta viðskiptavin")
    #     print("8.  Til baka")
    #     print("-"*len("1.  Skrá nýjan viðskiptavin"))
    #     input_num = input("Val: ")
    #     print()
        # if input_num == "1":
        #     skra_vidskiptavin()
        # elif input_num == "2":
        #     fletta_vidskiptavin()
        # elif input_num == "3":
        #     afskra_vidskiptavin()
        # elif input_num == "4":
        #     breyta_vidskiptavin()
        # elif input_num == "5":
        #     setja_a_bannlista()
        # elif input_num == "6":
        #     taka_af_bannlista()
        # elif input_num == "7":
        #     sekta_vidskiptavini()
        # else:
        #     print_options()



