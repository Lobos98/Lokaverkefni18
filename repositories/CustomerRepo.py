from models.Customer import Customer
import csv

class CustomerRepo:
	def __init__(self):
		self.__customers = []
		self.__header = ["Email","Nafn", "Kort", "Simi", "Kennitala", "Ban",\
		"Fine", "History"]

	def get_customer_list(self):
		if self.__customers == []:
			with open("./Data/list_of_customers.csv", "r") as customer_file:
				# DOnt repeat urself, gera fasta fyrir ./Data/list_of_customers.csv
				csv_reader = csv.DictReader(customer_file)
				next(csv_reader) # We don't need the header...
				# self.__customers.append(["Email","Nafn", "Kort", "Simi",\
				# 	"Kennitala", "Ban", "Fine", "History"])
				for line in csv_reader:
					new_customer = Customer(line["Email"], line["Nafn"],\
						line["Kort"], line["Simi"], line["Kennitala"],\
						line["Ban"], line["Fine"], line["History"])
					self.__customers.append(new_customer)
			return self.__customers
		return self.__customers

	def add_customer(self, new_customer, customer_list):
		with open("./Data/list_of_customers.csv", "a+", newline="") as\
		customer_file:
			csv_writer = csv.writer(customer_file)
			csv_writer.writerow(customer_list)
			self.__customers.append(new_customer)

	# def remove_customer(self, take_out):
	# 	#index = 0
	# 	for customer in self.__customers:
	# 		try:
	# 			if(take_out == customer.get_email()):
	# 				self.__customers.remove(customer)
	# 		except AttributeError:
	# 			pass
	# 	with open("./Data/list_of_customers.csv", "w") as customer_file:
	# 		index = 0
	# 		for customer in self.__customers:
	# 			if index == 0:
	# 				customer_file.write(','.join(customer))
	# 				customer_file.write("\n")
	# 				index += 1
	# 			else:
	# 				attribute_list = customer.get_attribute_list()
	# 				#self.add_customer(customer, attribute_list)
	# 				email = customer.get_email()
	# 				name = customer.get_name()
	# 				card_no = customer.get_card_no()
	# 				phone_no = customer.get_phone_no()
	# 				ssn = customer.get_ssn()
	# 				ban = customer.get_banned()
	# 				fine = customer.get_fine()
	# 				#customer_file.write("{},{},{},{},{},{},{}\n".format(email, name, card_no, phone_no, ssn, ban, fine))
	# 				#attribute_list = customer.get_attribute_list()
	# 				customer_file.write('\n' + ','.join(attribute_list))
	# 		customer_file.write("\n")
	# 	#print(self.__customers)

	def remove_customer(self, email_to_remove):
		"TODO: Docstring..."
		for customer in self.__customers:
			if email_to_remove == customer.get_email():
				self.__customers.remove(customer)
		
		self.__update_customer_file()
		
	def __update_customer_file(self):
		with open("./Data/list_of_customers.csv", "w") as customer_file:
			customer_file.write(','.join(self.__header) + '\n')
			for customer in self.__customers:
				customer_file.write(','.join(customer.get_attribute_list()) +\
					'\n')

	def __str__(self):
		return self.__customers
