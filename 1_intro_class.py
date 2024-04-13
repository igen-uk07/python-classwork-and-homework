item1= 'phone'
item_price = 100
iten_price2 = 5
item_total = item_price + iten_price2  
print(type(item1))


class Item:
    def calculate_total_price(self, x, y):  # function inside class is called methods
       # reasson behind Self : python passses the object itself as its first argument when we go ahead and call that methods 
       return x*y

item1 = Item() #instance of class
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))  #passes objects itsef as a first argument

item2 = Item() #instance of class
item2.name = "Laptop"
item2.price = 300
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))  

#random_str = "aaa"
#print(random_str.upper())

print(type(item1))
print(type(item1.price))
print(type(item1.quantity))