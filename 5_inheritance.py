import csv

class Item: ...



class Phone(Item):
    all = []
    def __init__(self, name: str , price: float, quantity: int, broken_phones = 0):   # we can create obj inside init methods for every instance rather making objects for evry instance sepeartely
      
        #Call to super function  ti have attribute access form the parrent class
        super().__init__(name, price, quantity)
        
       # assert price >= 0, f"price: {price} is not greater than zero" # We Can Add exception messages
       # assert quantity >= 0
        assert broken_phones >= 0
       
       # Assign to self Object
        print(f"An instance created :{name}")
       #self.name = name
       #self.quantity = quantity
        self.broken_phones = broken_phones

        #the attribute access form the parrent class
        # Actions to execute
        Phone.all.append(self)
   
    def calculate_total_price(self):
        return self.price * self.quantity
    

phone1 = Phone("jscphonev10", 500, 5,1)
print(phone1.calculate_total_price())
#phone1.broken_phones = 1
phone2 = Phone("jscphonev20",700,5,1)
#phone2.broken_phones = 1

print(Item.all)
print(Phone.all)