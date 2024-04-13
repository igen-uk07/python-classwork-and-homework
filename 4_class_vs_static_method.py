
import csv
class Item:
    pay_rate = 0.8 
    all = []
    def __init__(self, name: str , price: float, quantity: int):   # we can create obj inside init methods for every instance rather making objects for evry instance sepeartely
      
        assert price >= 0, f"price: {price} is not greater than zero" # We Can Add exception messages
        assert quantity >= 0
       
       # Assign to self Object
        print(f"An instance created :{name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
   
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price =self.price * self.pay_rate


    @classmethod 
    def instantiated_from_csv(cls):
        '''
        This should also do something that has a realtiosnhipppp with the class , but 
        usaully, those are used to manipulate differet=nt structures 
        of data to instattiate objects, like we have donw wiht csv
        '''
        with open('4_1.csv', 'r') as f:
          reader = csv.DictReader(f)
          items = list(reader)

        for item in items:
           print(Item(
               name = item.get('name'),
                price = int(item.get('price')),
                 quantity = int(item.get('quantity')),
           ))

    def __repr__(self):
        return  f"Item('{self.name}',{self.price}, {self.quantity})"
    
    @staticmethod

    def is_integer(num):
        '''
      This should do something that has a relatioonship
      with the class, but not something that must be unique per instace!
''' # never send the objects as a first argument
        #we will count out the floats that are points zero
        if isinstance(num,float):
           #count out the floats that ar point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

Item.instantiated_from_csv()
print(Item.is_integer(7.0))

print(Item.all)
#for instances in Item.all:
    #print(instances.name)
 