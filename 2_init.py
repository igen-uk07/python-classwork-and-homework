class Item:
    #constructer
    def __init__(self, name: str , price: float, quantity: int):   # we can create obj inside init methods for every instance rather making objects for evry instance sepeartely
      # Run validation to teh received arguments
        assert price >= 0, f"price: {price} is not greater than zero" # We Can Add exception messages
        assert quantity >= 0
       
       # Assign to self Object
        print(f"An instance created :{name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        
    #def calculate_total_price(self, x, y):  # function inside class is called methods
       # reasson behind Self : python passses the object itself as its first argument when we go ahead and call that methods 
      # return x*y
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("phone",100,9) #instance of class
item2 = Item("Laptop",24324,5) #instance of class
#item1.has_numpad = False
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item1.name)
print(item1.price)
print(item2.name)
print(item1.quantity)
print(item2.price)
print(item2.quantity)

'''item1 = Item("phone") #instance of class
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))  #passes objects itsef as a first argument

item2 = Item("Laptop") #instance of class
item2.name = "Laptop"
item2.price = 300
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))  

#random_str = "aaa"
#print(random_str.upper())

print(type(item1))
print(type(item1.price))
print(type(item1.quantity))'''