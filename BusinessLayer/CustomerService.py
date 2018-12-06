from repositories.CustomerRepo import CustomerRepo
from models.Customer import Customer

class CustomerService:
	def __init__(self):
		self.__customers = customer_repo.get_customer_list()

	def edit_customer_email(self, customer_email, new_email):
		customer = find_customer(customer_email)
		customer.set_email(new_email)

	def edit_customer_phone_no(self, customer_email, new_phone_no):
		customer = find_customer(customer_email)
		customer.set_phone_no(new_phone_no)

	def edit_customer_card_no(self, customer_email, new_card_no):
		customer = find_customer(customer_email)
		customer.set_card_no(new_card_no)

	def delete_customer(self, customer_email):
		customer_repo.remove_customer(customer_email)

	def find_customer(self, customer_email):
		for customer in self.__customers:
			if(customer_email == customer.get_email()):
				return customer
		return None

	def ban_customer(self, banned_customer):
		customer = self.find_customer(banned_customer)
		customer.set_ban(True)
		#Þarf ekki að breyta þessu í skránni líka og ef svo þá hvernig?????

	def unban_customer(self, unbanned_customer):
		customer = self.find_customer(unbanned_customer)
		customer.set_ban(False)
		#Þarf ekki að breyta þessu í skránni líka og ef svo þá hvernig?????

	def fine_customer(self, customer_email, fine_amount):
		customer = self.find_customer(customer_email)
		customer.set_fine(fine_amount)

	def add_customer(self, email, name, card_no, phone_no, ssn = "0"):
		new_customer = Customer(email, name, card_no, phone_no, ssn)
		customer_list = new_customer.get_attribute_list()
		customer_repo.add_customer(new_customer, customer_list)
		
customer_repo = CustomerRepo()