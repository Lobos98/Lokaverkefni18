class Customer:
	def __init__(self, email, name, card_no, phone_no, ssn = "0", ban = "false",\
		fine = "0", history = ""):
		self.__email = email
		self.__name = name
		self.__card_no = card_no
		self.__phone_no = phone_no
		self.__ssn = ssn
		self.__banned = ban
		self.__history = history
		self.__fine = fine

	def get_name(self):
		return self.__name

	def get_email(self):
		return self.__email

	def get_phone_no(self):
		return self.__phone_no

	def get_ssn(self):
		return self.__ssn

	def get_card_no(self):
		return self.__card_no

	def get_fine(self):
		return self.__fine

	def get_history(self):
		return self.__history

	def get_banned(self):
		return self.__banned

	def get_attribute_list(self):
		attribute_list = [self.__email, self.__name, self.__card_no,\
		self.__phone_no, self.__ssn, self.__banned, self.__fine, self.__history]
		return attribute_list

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

	def set_fine(self, fine):
		self.__fine = fine

	def add_history(self, old_order):
		self.__history = self.__history + old_order

	def __repr__(self):
		return "{},{},{},{},{}".format(self.__email, self.__name,\
			self.__card_no, self.__phone_no, self.__ssn)

	def __str__(self):
		return "Nafn: {}\nEmail: {}\nKortanúmer: {}\nSímanúmer: {}\
		\nKennitala: {}".format(self.__name, self.__email,self.__card_no,\
			self.__phone_no, self.__ssn)



