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

    def __repr__(self):
        return  f"Item('{self.name}',{self.price}, {self.quantity})"
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
#for instances in Item.all:
    #print(instances.name)
 