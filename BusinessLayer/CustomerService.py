from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo
from models.Customer import Customer

class CustomerService:
	def __init__(self):
		self.__customer_repo = CustomerRepo()
		self.__order_repo = OrderRepo()

	def update_customer(self, customer):
		'''Tekur inn customer object og uppfærir viðskiptavin með því
		 að taka hann úr skránniog setja aftur inn'''
		self.__customer_repo.remove_customer(customer)
		self.__customer_repo.add_customer(customer)


	def edit_customer_email(self, customer_email, new_email):
		'''Tekur við gömlu netfangi og nýju netfangi, lætur repo taka hann 
		úr skrá, breytir netfanginu og lætur skrifa hann aftur í skrá. 
		Skilar False ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_email(new_email)
		self.__customer_repo.add_customer(customer)

	def edit_customer_phone_no(self, customer_email, new_phone_no):
		'''Tekur við netfangi og nýju símanúmeri, finnur vskvin, 
		lætur repo taka hann úr skrá, breytir símanúmeri og lætur repo 
		skrifa hann aftur í skrá. Skilar False ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_phone_no(new_phone_no)
		self.__customer_repo.add_customer(customer)

	def edit_customer_card_no(self, customer_email, new_card_no):
		'''Tekur við netfangi og nýju kortanúmeri, finnur vskvin, 
		lætur repo taka hann úr skrá, breytir símanúmeri og lætur repo 
		skrifa hann aftur í skrá. Skilar False ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_card_no(new_card_no)
		self.__customer_repo.add_customer(customer)

	def delete_customer(self, customer_email):
		'''Tekur við netfangi og eyðir vskvini. Skilar False 
		ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)

	def ban_customer(self, customer_email):
		'''finnur vskvin eftir netfangi, tekur hann úr skrá, 
		bannar hann og skrifar aftur í skrá
		Skilar false ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_ban(True)
		self.__customer_repo.add_customer(customer)

	def unban_customer(self, customer_email):
		'''finnur vskvin eftir netfangi, tekur hann úr skrá, afbannar hann og 
		skrifar aftur í skrá. Skilar false ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_ban(False)
		self.__customer_repo.add_customer(customer)

	def fine_customer(self, customer_email, fine_amount):
		'''Tekur við netfangi og int upphæð, finnur vskvin eftir netfangi, 
		lætur taka hann úr repo, gefur honum sekt og skrifar aftur í skrána'''
		customer = self.__customer_repo.find_customer_by_email(customer_email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.set_fine(fine_amount)
		self.__customer_repo.add_customer(customer)

	def add_customer(self, email, name, card_no, phone_no, ssn = "0"):
		'''Tekur við netfangi, nafni, kortanúmeri, símanúmeri og kennitölu og 
		býr til Customer object sem er svo bætt í skrána og skilar True til 
		staðfestingar. Skilar False ef netfang vskvinar er þegar í notkun'''
		if self.__customer_repo.find_customer_by_email(email):
			return False
		new_customer = Customer(email, name, card_no, phone_no, ssn)
		self.__customer_repo.add_customer(new_customer)
		return True

	def add_old_order(self, email, order_num):
		'''Tekur inn netfang vskvinar og pöntunarnúmer, finnur vskvin 
		frá netfangi, eyðir vskvini úr skrá, bætir pöntunarnúmerinu í 
		customer_history og skrifar vskvin aftur í skrána.
		Skilar False ef vskvinur finnst ekki'''
		customer = self.__customer_repo.find_customer_by_email(email)
		if not customer:
			return False
		self.__customer_repo.remove_customer(customer)
		customer.add_history(order_num)
		self.__customer_repo.add_customer(customer)

	def list_of_banned_customers(self):
		'''Skilar lista af vskvinum sem eru bannaðir. 
		Skilar False ef engir vskvinir eru bannaðir'''
		all_customers = self.__customer_repo.get_customer_list()
		banned_customer_list = []
		for customer in all_customers:
			if customer.is_banned():
				banned_customer_list.append(customer)
		if banned_customer_list:
			return banned_customer_list
		else:
			return False
	def find_customer(self, email = "", ssn = "", phone_no = "", name = ""):
		"""
		Tekur inn eina færibreytu sem verður að vera strengur.
		Skrifið email = "test@test.is" eða ssn = "2903983209" eða 
		phone_no = "5812345" eða name = "robert" eftir því sem á við.
		Skilar alltaf customer nema ef leitað er eftir nafni eða snr, 
		þá skilast listi af Customers
		skilar False ef ekkert finnst
		"""
		#TODO: Ath köll í þetta fall - hvort það skili false
		if email:
			customer = self.__customer_repo.find_customer_by_email(email)
			return customer
		elif ssn:
			customer = self.__customer_repo.find_customer_by_ssn(ssn)
			return customer
		elif phone_no:
			customer_list = self.__customer_repo.find_customer_by_phone_no(phone_no)
			return customer_list
		elif name:
			customer_list = self.__customer_repo.find_customer_by_name(name)
			return customer_list
		return False
