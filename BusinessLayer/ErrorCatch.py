import datetime


class ErrorCatch:

    def __init__(self):
        pass

    def input_reg_num(self):
        check = False
        while check == False:
        reg_num = input("Bílnúmer: ")
            if len(reg_num) == 5:
                if reg_num[0:2].isalpha()== True:
                    if reg_num[2].isalnum() == True:
                        if reg_num[3:5].isdigit() == True:
                            return reg_num.upper()
            print("Athugið að bílnúmer skal skrifa inn á forminu AAXTT\n\
    þar sem A er bókstafur, T er tölustafur og X er annaðhvort")

    def check_SSN(self, SSN):
        if len(SSN) == 10:
            if SSN[0] in ['0','1','2','3'] and int(SSN[2] + SSN[3]) in range(1,13):
                return True
        else: 
            return False

    def check_email(self, email):
        if email[0] != '@' and '@' in email and email[-1] != '.' and '.' in email:
            return True
        else:
            return False

    def check_phone_no(self, phone_number):
        phone_number = phone_number.replace('-', '').replace(' ', '')
        if len(phone_number) == 7:
            return True
        else:
            return False

    def check_card_number(self, card_number):
        card_number.replace('-', '').replace(' ', '')
        if len(card_number) in [13,15,16,19]:
            return True
        else:
            return False
    
    def check_reg_num(self, reg_num):
        try:
            int(reg_num[3] + reg_num[4])
        except ValueError:
            return False
        try:
            int(reg_num[0] + reg_num[1])
        except ValueError:
            return True

    def check_int(self, integer):
        try:
            int(integer)
        except:
            return False
        else:
            return True

    def check_rental_date(self, date1, date2):
            first_date = datetime.datetime.strptime(date1, "%d%m%Y").date()
            second_date = datetime.datetime.strptime(date2, "%d%m%Y").date()
            todays_date = datetime.datetime.today().date()
            # If the inputted date is before today return false
            if first_date < todays_date:
                return False
            # Longest rental-time is one year.
            elif todays_date - first_date > datetime.timedelta(days=365):
                return False
            if second_date - first_date > datetime.timedelta(days=365):
                return False
            # If the second date is before the first date
            # or the difference is less than 1 day, return False
            if second_date < first_date:
                return False
            elif  (second_date - first_date) < datetime.timedelta(days=1):
                return False
            return True