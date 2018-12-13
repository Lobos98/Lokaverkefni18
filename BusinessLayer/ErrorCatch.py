from datetime import datetime, timedelta
import string
import re


class ErrorCatch:

    def __init__(self):
        pass

    def input_reg_num(self):
        """Biður um bílnúmer þangað til löglegt bílnúmer er skrifað inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng"""
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
                "\n'q' til að hætta")
            

    def input_email(self):
        """Biður um netfang þangað til löglegt netfang er skrifað inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng"""
        check = False
        r = re.compile(r"^\w+@\w+\.[a-zA-Z]+[a-zA-Z.]{0,}[a-zA-Z]+$")
        while check == False:
            email = input("Netfang: ")
            if email.count("@") == 1 and email.count(".") > 0:
                if r.match(email) is not None:
                    return email.lower()
            elif email.lower() == "q":
                return ""

            print("Athugið að netfang skal skrifa inn á forminu\n"
            "nafn@lén.is og má ekki innihalda íslenska sérstafi\n"
            "q til að hætta.")

    def input_model(self):
        """Biður um árgerð þangað til lögleg árgerð er skrifuð inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng"""
        check = False
        while check == False:
            model = input("Árgerð: ")
            #TODO bæta við stuðning fyrir 5 stafa ár fyrir árið 10000 
            if len(model) == 4:
                if model.isdigit() == True:
                    if int(model) <= datetime.today().year:
                        return model
            if model.lower() == "q":
                return ""
            print("Athugið að árgerð skal skrifa inn á forminu\n"\
            "TTTT þar sem T er tölustafur og skal vera lögleg árgerð á bíl\n"
            "'q' til að hætta")

    def input_type(self):
        """
        Biður um bíltegund þangað til lögleg bíltegund er skrifuð inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng
        """
        check = False
        model_list = ["jeppi", "folksbill", "smabill", "husbill", "sportbill"]
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
            "folksbill, smabill, husbill eða sportbill\n"\
            "og skal skrifa án íslenskra sérstafa\n"
            "'q' til að hætta")

    def input_color(self):
        """
        Biður um lit á bíl þangað til löglegur litur er skrifaður inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng
        """
        list_of_colors = ["gulur", "raudur", "graenn", "blar", "svartur", \
        "hvitur", "fjolublar", "brunn", "bleikur", "appelsinugulur", \
        "grar", "silfur", "gull"]
        check = False
        while check == False:
            
            color = input("Litur: ")
            if color in list_of_colors:
                return color.lower()
            if color.lower() == "q":
                return ""
            print("Vinsamlegast skrifið inn lit."\
            " Tölustafir og íslenskir sérstafir eru ekki leyfðir")
            color_string = ", ".join(list_of_colors)
            print("Eftirfarandi eru löglegir litir: {}".format(color_string))
            print("'q' til að hætta")

    def input_name(self):
        """
        Biður um nafn þangað til löglegt nafn er skrifað inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng
        """
        name = input("Sláðu inn nafn viðskiptavinar: ")
        r = re.compile("[a-zA-Z\s.'-,]+")
        while not r.match(name):
            name = input("Sláðu inn nafn viðskiptavinar: ")
        return name


    def input_rental_dates(self):
        """Biður um tvö inputs á forminu ddmmáááá þangað til þau passa við 
        okkar reglur og skilar svo strengjunum.
        Hér er ekki boðið upp á að hætta við."""
        pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
        return_date_string = input("Dagsetning skila (ddmmáááá): ")
#        Hér mætti skrifa inn virkni til að taka við 12-03-2018, 12.03.2018, 12/03/2018
#        o.s.frv.
#        if dates_with_slashes(pickup_date_string, return_date_string):
#            pass
#        elif dates_with_dots(pickup_date_string, return_date_string):
#            pass
#        elif dates_clean(pickup_date_string, return_date_string):
#            pass
        while self.check_rental_date(\
        pickup_date_string, return_date_string) == False:
            print("-"*27)
            print("Athugið eftirfarandi:\n"
            "Dagsetningar skal skrifa inn á forminu ddmmáááá.\n"
            "Hámarksleigutími er eitt ár.\n"
            "Ekki er hægt að velja leigutímabil sem er liðið.\n"
            "Ekki er hægt að skrá pöntun meira en ár fram í tímann.")
            print("-"*27)
            pickup_date_string = input("Dagsetning leigu (ddmmáááá): ")
            return_date_string = input("Dagsetning skila (ddmmáááá): ")
        return pickup_date_string, return_date_string

    def input_phone(self):
        """
        Biður um snr þangað til löglegt snr er skrifað inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng 
        """
        phone = input("Símanúmer: ")
        while not self.check_phone_no(phone):
            if phone.lower() == "q":
                return ""
            else:
                print("Ógilt símanúmer, reyndu aftur eða 'q' til að hætta")
                phone = input("Símanúmer: ")
        return phone

    def input_card(self):
        """
        Biður um kortanr þangað til löglegt kortanr er skrifað inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng 
        """
        card_number = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        while not self.check_card_number(card_number):
            if card_number.lower() == "q":
                return ""
            else:
                print("Ógilt kortanúmer, reyndu aftur eða 'q' til að hætta")
                card_number = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        card_number = card_number.replace("-", "").replace(" ", "")
        return card_number

    def input_ssn(self):
        """
        Biður um kennitölu þangað til lögleg kennitala er skrifuð inn. 
        Býður upp á að skrifa inn q til að hætta við og skilar þá tómum streng 
        """
        ssn = input("Kennitala: ")
        print("-"*52)
        while not self.check_SSN(ssn):
            if ssn.lower() == "q":
                return ""
            else:
                print("Kennitala er ógild, reyndu aftur eða 'q' " 
                "til að hætta")
                ssn = input("Kennitala: ")
        print("Kennitala er gild")
        return ssn
    

    def check_SSN(self, SSN):
        """
        Skilar false ef lengd kennitölu er röng, dagsetning er ólögleg eða 
        ef viðkomandi er of ungur að árum til þess að vera með bílpróf
        """
        if len(SSN) != 10:
            return False
        day_date = int(SSN[0:2])
        month = int(SSN[2:4])
        year_now = datetime.today().year
        if int(SSN[4:6]) < year_now-2000:
            birth_year = int(SSN[4:6]) + 2000
        else:
            birth_year = int(SSN[4:6]) + 1900
        if year_now - birth_year < 17:
            return False
        if day_date not in range(1,32):
            return False
        if month not in range(1,13):
            return False
        if month in [4, 6, 9,11] and day_date == 31:
            return False
        if month == 2 and birth_year % 4 != 0 and day_date > 28:
            return False
        elif month == 2 and birth_year % 4:
            if day_date > 29:
                return False
        return True

    def check_email(self, email):
        """
        Tekur við email streng sem input, skilar False 
        ef hann uppgyllir eitthvað af eftirfarandi skilyrðum:
        er með @ fremst
        hefur ekki @
        hefur ekki punkt
        hefur punktinn aftast
        """
        if email[0] != '@' and '@' in email and\
        email[-1] != '.' and '.' in email:
            return True
        else:
            return False

    def check_phone_no(self, phone_number):
        """
        Tekur við símanúmeri á strengjaformi, losar það við 
        bandstrik og bil og skilar False ef númerið er er styttra en 
        2 stafir eða inniheldur eitthvað annað en tölur
        """
        phone_number = phone_number.replace('-', '').replace(' ', '')
        if not phone_number.isdigit():
            return False
        if len(phone_number) not in range(2, 21):
            return False
        return True

    def check_card_number(self, card_number):
        """
        Tekur við kreditkortanúmeri sem er strengur, fjarlægir bandstrik og 
        bil og skilar False ef númerið er ekki 13, 15, 16 eða 19 tölustafir
        """
        card_number = card_number.replace('-', '').replace(' ', '')
        if not card_number.isdigit():
            return False
        if not len(card_number) in [13,15,16,19]:
            return False
        return True
    
    def check_reg_num(self, reg_num):
        """
        Skilar True fyrir ólöglegt bílnúmer
        """
        try:
            int(reg_num[3] + reg_num[4])
        except ValueError:
            return False
        try:
            int(reg_num[0] + reg_num[1])
        except ValueError:
            return True

    def integer_input(self, message, max_int):
        """
        While loopa sem biður um heiltölu input frá 
        einum og upp að efra markinu sem er sett inn í fallið
        Setur inn skilaboð sem þú vilt að sé gefið í hvert sinn
        sem er spurt um gildið
        """
        while True:
            try:
                check_if_int = int(input(str(message)))
                if check_if_int not in range(1, max_int + 1):
                    raise ValueError
            except:
                print("Vinsamlegast sláðu inn heiltölu.")
            else:
                return check_if_int

    def check_rental_date(self, date1, date2):
        try:
            first_date = datetime.strptime(date1, "%d%m%Y").date()
            second_date = datetime.strptime(date2, "%d%m%Y").date()
            todays_date = datetime.today().date()
        except ValueError:
            return False
        else:
            # If the inputted date is before today return false
            if first_date < todays_date:
                return False
            # Longest rental-time is one year.
            elif first_date - todays_date > timedelta(days=365):
                return False
            if second_date - first_date > timedelta(days=365):
                return False
            # If the second date is before the first date
            # or the difference is less than 1 day, return False
            if second_date < first_date:
                return False
            elif  (second_date - first_date) < timedelta(days=0):
                return False
            return True