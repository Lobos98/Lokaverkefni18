class Customer:
	def __innit__(self, email, name, card_no, phone_no, ssn):
		self.__email = email
		self.__name = name
		self.__card_no = card_no
		self.__phone_no = phone_no
		self.__ssn = ssn
		self.__banned = False
		self.__history = {}
		self.__orders = []

	def get_name(self):
		return self.__name

	def get_email(self):
		return self.__email

	def get_phone_no(self):
		return self.__phone_no

	def get_ssn(self):
		return self.__ssn

	def get_orders(self):
		return self.__orders

	def get_history(self):
		return self.__history

	def get_banned(self):
		return self.__banned

	def set_name(self, new_name):
		self.__name = new_name

	def set_email(self, new_email):
		self.__email = new_email

	def set_phone_no(self, new_phone_no):
		self.__phone_no = new_phone_no

	def set_card_no(self, new_card_no):
		self.__card_no = new_card_no

	def set_ban(self, ban_bool):
		self.__banned = ban_bool

	def add_order(self, new_order):
		self.__orders.append(new_order)

	def add_history(self, old_order):
		self.__history[old_order.get_order_no()] = old_order