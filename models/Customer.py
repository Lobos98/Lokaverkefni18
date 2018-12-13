class Customer:
	def __init__(self, email, name, card_no, phone_no, ssn = "", ban = False,\
		fine = "0", history = None):
		self.__email = email
		self.__name = name
		self.__card_no = card_no
		self.__phone_no = phone_no
		self.__ssn = ssn
		self.__banned = ban
		if history == None:
			self.__history = []
		else:
			self.__history = history
		self.__fine = fine

	def get_name(self):
		"""
		Skilar nafni viðskiptavinar, sem er strengur
		"""
		return self.__name

	def get_email(self):
		"""
		Skilar tölvupósti viðskiptavinar, sem er strengur
		"""
		return self.__email

	def get_phone_no(self):
		"""
		Skila símanúmeri viðskiptavinar, sem er strengur á forminu 7774444
		"""
		return self.__phone_no

	def get_ssn(self):
		"""
		Skila kennitölu vskvinar, sem er strengur á forminu 0101993209
		"""
		return self.__ssn

	def get_card_no(self):
		"""
		Skilar kreditkortanúmeri vskvinar, sem er strengur
		á forminu 1111222233334444
		"""
		return self.__card_no

	def get_fine(self):
		"""
		Skilar skuld vskvinar í krónum sem int
		"""
		return self.__fine

	def get_history(self):
		"""
		Skilar lista þar sem hvert stak í listanm er int sem samsvarar 
		pöntunarnúmeri á pöntun sem hefur liðið
		"""
		return self.__history

	def is_banned(self):
		"""
		Skilar boolean gildi True eða False eftir því hvort 
		viðskiptavinur er bannaður
		"""
		return self.__banned

	def set_name(self, new_name):
		"""
		Breytir __name eigindi klasans - helst í streng
		"""
		self.__name = new_name

	def set_email(self, new_email):
		"""
		Breytir __email eigindi klasans - helst í streng
		"""
		self.__email = new_email

	def set_phone_no(self, new_phone_no):
		"""
		breytir __phone_no eigindi klasans - helst í streng á forminu 7776666
		"""
		self.__phone_no = new_phone_no

	def set_card_no(self, new_card_no):
		"""
		Breytir car_no eigindi klasans - 
		helst í streng á forminu 1111222233334444
		"""
		self.__card_no = new_card_no

	def set_ban(self, ban_bool):
		"""
		Breytir __ban eigindi klasans - helst í boolean
		"""
		self.__banned = ban_bool

	def set_fine(self, fine):
		"""
		Breytir __fine eigindi klasans - helst í int
		"""
		self.__fine = str(int(self.__fine) + fine)

	def add_history(self, old_order_no):
		"""Tekur við pöntunarnúmeri sem int og bætir því í customer history"""
		self.__history = self.__history.append(old_order_no)

	def __repr__(self):
		if self.__ssn == "":
			return "{},{},{},{}".format(self.__email, self.__name,\
				self.__card_no, self.__phone_no)
		else:
			return "{},{},{},{},{}".format(self.__email, self.__name,\
				self.__card_no, self.__phone_no, self.__ssn)

	def __str__(self):
		if self.__ssn == "":
			return "Nafn: {}\nEmail: {}\nKortanúmer: {}\nSímanúmer: {}\
			".format(self.__name, self.__email,self.__card_no,\
				self.__phone_no)
		else:
			return "Nafn: {}\nEmail: {}\nKortanúmer: {}\nSímanúmer: {}\
			\nKennitala: {}".format(self.__name, self.__email,self.__card_no,\
				self.__phone_no, self.__ssn)



