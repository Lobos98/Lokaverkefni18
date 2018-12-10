from repositories.CustomerRepo import CustomerRepo
from models.Customer import Customer

class CustomerService:
	def __init__(self):
		self.__customers = customer_repo.get_customer_list()

	def edit_customer_email(self, customer_email, new_email):
		customer = self.find_customer(customer_email)
		customer.set_email(new_email)
		customer_repo.remove_customer(customer_email)
		attribute_list = customer.get_attribute_list()
		customer_repo.add_customer(customer, attribute_list)

	def edit_customer_phone_no(self, customer_email, new_phone_no):
		customer = self.find_customer(customer_email)
		customer.set_phone_no(new_phone_no)
		customer_repo.remove_customer(customer_email)
		attribute_list = customer.get_attribute_list()
		customer_repo.add_customer(customer, attribute_list)

	def edit_customer_card_no(self, customer_email, new_card_no):
		customer = self.find_customer(customer_email)
		customer.set_card_no(new_card_no)
		customer_repo.remove_customer(customer_email)
		attribute_list = customer.get_attribute_list()
		customer_repo.add_customer(customer, attribute_list)

	def delete_customer(self, customer_email):
		customer_repo.remove_customer(customer_email)

	def find_customer(self, customer_email):
		for customer in self.__customers:
			if(customer_email == customer.get_email()):
				return customer
		return False

	def ban_customer(self, banned_customer):
		customer = self.find_customer(banned_customer)
		customer.set_ban("true")
		attribute_list = customer.get_attribute_list()
		customer_repo.remove_customer(customer.get_email())
		customer_repo.add_customer(customer, attribute_list)

	def unban_customer(self, unbanned_customer):
		customer = self.find_customer(unbanned_customer)
		customer.set_ban("false")
		attribute_list = customer.get_attribute_list()
		customer_repo.remove_customer(customer.get_email())
		customer_repo.add_customer(customer, attribute_list)

	def fine_customer(self, customer_email, fine_amount):
		customer = self.find_customer(customer_email)
		customer.set_fine(str(fine_amount))
		attribute_list = customer.get_attribute_list()
		customer_repo.remove_customer(customer_email)
		customer_repo.add_customer(customer, attribute_list)

	def add_customer(self, email, name, card_no, phone_no, ssn = "0"):
		new_customer = Customer(email, name, card_no, phone_no, ssn)
		customer_list = new_customer.get_attribute_list()
		customer_repo.add_customer(new_customer, customer_list)

	def add_old_order(self, email, order_num):
		customer = self.find_customer(email)
		if customer != False:
			customer.add_history(order_num)
			print(customer.get_history())

	def list_of_banned_customers(self):
		banned_customer_list = []
		for customer in self.__customers:
			if customer.get_banned() == "true":
				banned_customer_list.append(customer)
		return banned_customer_list
		
customer_repo = CustomerRepo()

