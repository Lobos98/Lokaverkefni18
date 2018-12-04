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