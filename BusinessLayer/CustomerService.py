from repositories.CustomerRepo import CustomerRepo

class CustomerService:
	def __init__(self):
		self.__customers = CustomerRepo.get_customer_list()

	def edit_customer(self):

	def delete_customer(self):
		self.__customers.remove_customer()

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

	def add_customer(self):
		new_customer = Customer(email, name, card_no, phone_no, kt)
		self.__customers.add_customer(new_customer)