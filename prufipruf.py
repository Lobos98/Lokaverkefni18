from BusinessLayer.OrderService import OrderService
from models.Order import Order



serv = OrderService()
#print(serv.get_list_of_orders())
 
#print(serv.find_order("magga@gmail.com"))

order = Order(1,"AB123",("12122018","14122018"),"magga@gmail.com",0)
serv.move_to_past("magga@gmail.com")
#print(serv.get_list_of_past_orders())

# serv.log_order("AU123","12132018","14122018","maggi@email.com","false")
# serv.change_order("magga@gmail.com","2", reg_number="RE345")
 
# order = Order(2,"CD234",("03052017","12052017"),"siggi@gmail.com","true")
#serv.delete_order(order)






# from repositories.OrderRepo import OrderRepo
# from models.Order import Order

# repo = OrderRepo()
# print(repo.get_all_orders())
# print("-"*50)
# order = Order(3,"AB123",("12122018","14122018"),"magga@gmail.com","false")
# repo.add_order(order)

# order = Order(2,"CD234",("03052017","12052017"),"siggi@gmail.com","true")
# repo.remove_order(order)

# email = "magga@gmail.com"
# print(repo.get_order(email))

