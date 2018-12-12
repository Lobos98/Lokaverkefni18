from repositories.CustomerRepo import CustomerRepo
from repositories.OrderRepo import OrderRepo
from models.Customer import Customer

class CustomerService:
	def __init__(self):
		self.__customer_repo = CustomerRepo()
		self.__order_repo = OrderRepo()
		self.__customers = self.__customer_repo.get_customer_list()

	def update_customer(self, customer_email, customer):
		'''uppfærir viðskiptavin með því að taka hann út
		og setja aftur inn'''
		self.__customer_repo.remove_customer(customer_email)
		attribute_list = customer.get_attribute_list()
		self.__customer_repo.add_customer(customer, attribute_list)


	def edit_customer_email(self, customer_email, new_email):
		'''breytir email hjá viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(customer_email)
		customer.set_email(new_email)
		self.__customer_repo.remove_customer(customer_email)
		#self.update_customer(customer_email, customer)

	def edit_customer_phone_no(self, customer_email, new_phone_no):
		'''breytir símanúmer hjá viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(customer_email)
		customer.set_phone_no(new_phone_no)
		self.update_customer(customer_email, customer)

	def edit_customer_card_no(self, customer_email, new_card_no):
		'''breytir kortanúmeri hjá viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(customer_email)
		customer.set_card_no(new_card_no)
		self.update_customer(customer_email, customer)

	def delete_customer(self, customer_email):
		'''eyðir viðskiptavin með því að kalla á repóið'''
		self.__customer_repo.remove_customer(customer_email)
		#else:

	def find_customer(self, customer_email):
		return self.__customer_repo.find_customer_by_email(customer_email)

	def find_customer_by_name(self, name):
		return self.__customer_repo.find_customer_by_name(name)

	def find_customer_by_ssn(self, ssn):
		return self.__customer_repo.find_customer_by_ssn(ssn)

	def find_customer_by_phone_no(self, phone_no):
		return self.__customer_repo.find_customer_by_phone_no(phone_no)

	def ban_customer(self, banned_customer):
		'''bannar viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(banned_customer)
		customer.set_ban("true")
		self.update_customer(banned_customer, customer)

	def unban_customer(self, unbanned_customer):
		'''afbannar viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(unbanned_customer)
		customer.set_ban("false")
		self.update_customer(unbanned_customer, customer)

	def fine_customer(self, customer_email, fine_amount):
		'''sektar viðskiptavin og uppfærir hann í repóinu'''
		customer = self.find_customer(customer_email)
		customer.set_fine(fine_amount)
		self.update_customer(customer_email, customer)

	def add_customer(self, email, name, card_no, phone_no, ssn = "0"):
		'''bætir við viðskiptavin og kallar á repóið til að bæta hann í
		skránni'''
		if not self.find_customer(email):
			new_customer = Customer(email, name, card_no, phone_no, ssn)
			customer_list = new_customer.get_attribute_list()
			self.__customer_repo.add_customer(new_customer, customer_list)
			return True
		else:
			return False

	def add_old_order(self, email, order_num):
		'''bætir við gamla pöntun í customer history og uppfærir hann í
		repóinu'''
		customer = self.find_customer(email)
		if customer != False:
			customer.add_history(order_num)
		self.update_customer(email, customer)

	def list_of_banned_customers(self):
		'''safnar saman viðskiptavini sem eru bannaðir'''
		banned_customer_list = []
		for customer in self.__customers:
			if customer.get_banned() == "true":
				banned_customer_list.append(customer)
		return banned_customer_list

