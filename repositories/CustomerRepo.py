from models.Customer import Customer
import csv

class CustomerRepo:
	def __init__(self):
		self.__link = "./Data/list_of_customers.csv"
		self.__customers = self.get_customer_list()
		self.__header = ["Email","Nafn", "Kort", "Simi", "Kennitala", "Ban",\
		"Fine", "History"]

	def get_customer_list(self):
		"""
		Skrifar __customers eigindi klasans aftur upp frá skránni og skilar
		 __customers eigindinu, sem er listi af customer objects
		"""
		self.__customers = []
		with open(self.__link, "r", encoding = "utf-8") as customer_file:
			csv_reader = csv.DictReader(customer_file)
			for line in csv_reader:
				#banned = False
				email = line["Email"]
				name = line["Nafn"]
				card_no = line["Kort"]
				phone_no = line["Simi"]
				ssn = line["Kennitala"]
				if line["Ban"] == "True":
					banned = True
				elif line["Ban"] == "False":
					banned = False
				fine = int(line["Fine"])
				history_string = line["History"]
				history_list_of_strings = history_string.split(";")
				if history_list_of_strings == [""]:
					history = []
				else:
					history = [int(item) for item in history_list_of_strings]
				new_customer = Customer(email, name,\
					card_no, phone_no, ssn,\
					banned, fine, history)
				self.__customers.append(new_customer)
		return self.__customers

	def add_customer(self, new_customer):
		"""
		tekur inn customer object, skrifar það í skrána og 
		bætir við í __customers eigindið
		"""
		with open(self.__link, "a+", newline="") as customer_file:
			csv_writer = csv.writer(customer_file)
			customer_attributes = self.__get_string_attributes(new_customer)
			csv_writer.writerow(customer_attributes)
			self.__customers.append(new_customer)

	def find_customer_by_email(self, customer_email):
		'''finnur viðskiptavin eftir tölvupósti og skilar customer object, 
		skilar False ef hann finnst ekki'''
		for customer in self.__customers:
			if customer_email == customer.get_email():
				return customer
		return False

	def find_customer_by_name(self, name):
		"""Tekur við nafni sem streng og skilar lista yfir þá viðskiptavini 
		sem eru með nafnbútinn í nafninu sínu. Skilar False ef ekkert finnst"""
		#list_of_customers = self.__customer_repo.get_customer_list()
		list_of_found_customers = []
		for customer in self.__customers:
			if name.lower() in customer.get_name().lower():
				list_of_found_customers.append(customer)
		if list_of_found_customers:
			return list_of_found_customers
		else:
			return False

	def find_customer_by_ssn(self, ssn):
		"""
		tekur við kennitölu sem streng á forminu 2903983209 og skilar
		viðskiptavini með þá kennitölu. Skilar False ef vskvinur finnst ekki
		"""
		for customer in self.__customers:
			if ssn == customer.get_ssn():
				return customer
		return False

	def find_customer_by_phone_no(self, phone_no):
		"""
		Tekur við símanúmeri á forminu 5556666 og skilar lista af þeim 
		viðskiptavinum sem hafa þetta símanúmer. Skilar False ef ekkert finnst.
		"""
		phone_list = []
		for customer in self.__customers:
			if phone_no == customer.get_phone_no():
				phone_list.append(customer)
		if phone_list:
			return phone_list
		else:
			return False

	def remove_customer(self, customer):
		"""
		Tekur við customer object sem skal eyða og eyðir 
		viðkomandi úr eigindi klasans og kallar svo á fall sem uppfærir skrána
		"""
		for customer_in_list in self.__customers:
			if customer.get_email() == customer_in_list.get_email():
				self.__customers.remove(customer)
		self.__update_customer_file()
		
	def __update_customer_file(self):
		"""
		Skrifar skrána upp á nýtt út frá Customer objects í __customers eigindi
		"""
		with open("./Data/list_of_customers.csv", "w") as customer_file:
			customer_file.write(','.join(self.__header) + '\n')
			for customer in self.__customers:
				customer_file.write(','.join(self.\
					__get_string_attributes(customer)) +'\n')

	def __get_string_attributes(self, customer):
		"""
		Tekur inn Customer og skilar lista af strengjum þar sem 
		hver strengur táknar einn dálk í gagnaskipaninni
		"""
		email = customer.get_email()
		name = customer.get_name()
		card_no = customer.get_card_no()
		phone_no = customer.get_phone_no()
		ssn = customer.get_ssn()
		if customer.is_banned():
			ban = "True"
		elif not customer.is_banned():
			ban ="False"
		fine = str(customer.get_fine())
		history = self.__get_history_string(customer)
		string_attributes = [email, name, card_no, phone_no, ssn,\
		ban, fine, history]
		return string_attributes

	def __get_history_string(self, customer):
		"""
		tekur við customer object og skilar history eigindinu 
		hans sem streng til þess að skrifa í gögnin
		"""
		history = ""
		for past_order_int in customer.get_history():
			history += str(past_order_int)
			history += ";"
		history = history[:-1]
		return history


	def __str__(self):
		return self.__customers