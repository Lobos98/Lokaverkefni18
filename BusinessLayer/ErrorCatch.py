import datetime
import string
import re


class ErrorCatch:

    def __init__(self):
        pass

    def input_reg_num(self):
        check = False
        r = re.compile(r"^[a-zA-Z]{2}\w[0-9]{2}$")
        while check == False:
            reg_num = input("Bílnúmer: ")
            if len(reg_num) == 5:
                if r.match(reg_num) is not None:
                    return reg_num.upper()
            if reg_num.lower() == "q":
                return ""
            else:
                print("Athugið að bílnúmer skal skrifa inn á forminu AAXTT\n"
                "þar sem A er bókstafur, T er tölustafur og X er annaðhvort"
                "'q' til að hætta")
            

    def input_email(self):
        check = False
        r = re.compile(r"^\w+@\w+\.[a-zA-Z]+[a-zA-Z.]{0,}[a-zA-Z]+$")
        while check == False:
            email = input("Netfang: ")
            if email.count("@") == 1 and email.count(".") > 0:
                if r.match(email) is not None:
                    return email.lower()
            elif email.lower() == "q":
                return email.lower()

            print("Athugið að netfang skal skrifa inn á forminu\n"
            "nafn@lén.is og má ekki innihalda íslenska sérstafi\n"
            "q til að hætta.")

    def input_model(self):
        check = False
        while check == False:
            model = input("Árgerð: ")
            if len(model) == 4:
                if model.isdigit() == True:
                    if int(model) <= datetime.datetime.today().year:
                        return model
            if model.lower() == "q":
                return ""
            print("Athugið að árgerð skal skrifa inn á forminu\n"\
            "TTTT þar sem T er tölustafur og skal vera lögleg árgerð á bíl\n"
            "'q' til að hætta")

    def input_type(self):
        check = False
        model_list = ["jeppi", "folksbill", "smabill"]
        while check == False:
            model = input("Tegund bíls: ")
            if model.isalpha():
                if model.isascii():
                    for item in model_list:
                        if model.lower() == item:
                            return model.lower()
            if model.lower() == "q":
                return ""
            print("Athugið að tegund bíls getur verið jeppi, "\
            "folksbill eða smabill\nog skal skrifa án íslenskra sérstafa\n"
            "'q' til að hætta")

    def input_color(self):
        check = False
        while check == False:
            color = input("Litur: ")
            if len(color) < 15:
                if color.isalpha() == True:
                    if color.isascii() == True:
                        return color.lower()
            if color.lower() == "q":
                return ""
            print("Vinsamlegast skrifið inn lit."\
            " Tölustafir og íslenskir sérstafir eru ekki leyfðir"
            "'q' til að hætta")

    def input_name(self):
        check = False
        while check == False:
            name = input("Sláðu inn nafn viðskiptavinar: ")
            if name.isalpha() == True:
                if name.isascii() == True:
                    return name.lower()
            print("Vinsamlegast skrifið inn nafn.\n"
            "Athugið að nafn má ekki innihalda íslenska sérstafi.")

    def input_rental_dates(self):
        """Biður um tvö inputs á forminu ddmmáááá og skilar strengjunum ef 
        þeir passa við okkar reglur"""
        pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
        return_date_string = input("Dagsetning skila (ddmmáááá): ")
        while self.check_rental_date(\
        pickup_date_string, return_date_string) == False:
            print("-"*27)
            print("Athugið eftirfarandi:\n"
            "Dagsetningar skal skrifa inn á forminu ddmmáááá\n"
            "Hámarksleigutími er eitt ár\n"
            "Ekki er hægt að velja leigutímabil sem er liðið")
            print("-"*27)
            pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
            return_date_string = input("Dagsetning skila (ddmmáááá): ")
        return pickup_date_string, return_date_string


    def check_SSN(self, SSN):
        if len(SSN) == 10:
            if SSN[0] in ['0','1','2','3'] and\
            int(SSN[2] + SSN[3]) in range(1,13):
                return True
        else: 
            return False

    def check_email(self, email):
        if email[0] != '@' and '@' in email and\
        email[-1] != '.' and '.' in email:
            return True
        else:
            return False

    def check_phone_no(self, phone_number):
        phone_number = phone_number.replace('-', '').replace(' ', '')
        if len(phone_number) in range(2, 21):
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

    def integer_input(self, message):
        while True:
            try:
                check_if_int = int(input(str(message)))
            except:
                print("Vinsamlegast sláðu inn heiltölu.")
            else:
                return check_if_int

    def check_rental_date(self, date1, date2):
        try:
            first_date = datetime.datetime.strptime(date1, "%d%m%Y").date()
            second_date = datetime.datetime.strptime(date2, "%d%m%Y").date()
            todays_date = datetime.datetime.today().date()
        except ValueError:
            return False
        else:
            # If the inputted date is before today return false
            if first_date < todays_date:
                return False
            # Longest rental-time is one year.
            elif first_date - todays_date > datetime.timedelta(days=365):
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