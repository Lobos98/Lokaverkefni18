class ErrorCatch:

    def check_SSN(SSN):
        if SSN[0] in ['0','1','2','3'] and int(SSN[2] + SSN[3]) in range(1,13):
            return True
        else: 
            return False

    def check_email(email):
        if email[0] != '@' and '@' in email and email[-1] != '.' and '.' in email:
            return True
        else:
            return False

    def check_phone_no(phone_number):
        phone_number = phone_number.replace('-', '').replace(' ', '')
        if len(phone_number) == 7:
            return True
        else:
            return False

    def check_card_number(card_number):
        card_number.replace('-', '').replace(' ', '')
        if len(card_number) in [13,15,16,19]:
            return True
        else:
            return False
    
    def check_reg_num(reg_num):
        try:
            int(reg_num[3] + reg_num[4])
        except ValueError:
            return False
        try:
            int(reg_num[0] + reg_num[1])
        except ValueError:
            return True

    def check_int(integer):
        try:
            int(integer)
        except:
            return False
        else:
            return True

    def check_date(date):
        return True