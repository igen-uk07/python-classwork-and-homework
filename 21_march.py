class A:
   # name = 'sandeep'
   # sap_id = 34234
    
    def __init__(self, x, y): # selg is used to refer class member 
      print("I am inside the init of class A")
      self.name =x
      self.sap_id = y
      self.emp = self.B()
    def showA(Self):
       print("inside show off A")

    def atrrib(self):
      print( self.name, self.sap_id)


    class B:
       def __init__(self):
          print("i am inside another class")
       def showB(self):
          print("inside show of B")

a1 = A("igen", 500123847)
a1.showA()
print(a1.name)
print(a1.sap_id)
a1.atrrib()
a1.B()
a1.emp.showB()
