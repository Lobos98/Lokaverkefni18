from models.Customer import Customer
import csv

class CustomerRepo:
	def __init__(self):
		self.__customers = []

	def get_customer_list(self):
		if self.__customers == []:
			with open("./Data/testcustomer.csv", "r") as customer_file:
				csv_reader = csv.DictReader(customer_file)
				for line in csv_reader:
					new_customer = Customer(line["email"], line["Nafn"],\
						line["Kort"], line["Sími"], line["Kennitala"])
					self.__customers.append(new_customer)
			return self.__customers
		return self.__customers

	def add_customer(self, new_customer, customer_list):
		with open("./Data/testcustomer.csv", "a") as customer_file:
			csv_writer = csv.writer(customer_file)
			csv_writer.writerow(customer_list + "\n")
			self.__customers.append(new_customer)

	def remove_customer(self, take_out):
		for customer in self.__customers:
			if(take_out == customer.get_email()):
				self.__customers.remove(customer)
		with open("./Data/testcustomer.csv", "w") as customer_file:
			csv_writer = csv.writer(customer_file)
			for customer in self.__customers:
				csv_writer.writerow(customer)

	def __str__(self):
		return self.__customers
