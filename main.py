from ui.StaffInterface import StaffInterface

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