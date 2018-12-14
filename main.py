try:
    from ui.StaffInterface import StaffInterface

    def main(): 
        staff = StaffInterface()
        staff.start_menu()
        

    main()

except KeyboardInterrupt:
    print("Ýttu frekar á hætta kjáni")