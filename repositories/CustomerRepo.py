from models.Customer import Customer
import csv

class CustomerRepo:
	def __init__(self):
		self.__customers = self.get_customer_list()

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

	def add_customer(self, new_customer):
		with open("./Data/testcustomer.csv", "a") as customer_file:
			csv_writer = csv_writer(customer_file)
			for customer in new_customer:
				csv_writer.writerow(customer)

	def __str__(self):
		return self.__customers
