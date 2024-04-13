class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
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

    def apply_discount(self):
        self.price =self.price * self.pay_rate
item1 = Item("phone",100,9) #instance of class

#item1.has_numpad = False

item1.apply_discount()
print(item1.price)

item2 = Item("Laptop",24324,5) #instance of class
item2.pay_rate = 0.7 # if we want to have difeerent pay rate for every other item we can do it in instance level instead of class level
item2.apply_discount()
print(item2.price)




#print(Item.__dict__) # All attributes for class level
#print(item1.__dict__)# All the attributes for instance level



'''print(Item.pay_rate)
print(item1.pay_rate) # we can access class attributes from instance level
print(item2.pay_rate)'''






'''print(item1.name)
print(item1.price)
print(item2.name)
print(item1.quantity)
print(item2.price)
print(item2.quantity)'''