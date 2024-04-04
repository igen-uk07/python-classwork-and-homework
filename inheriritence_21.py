class A:
    name = 'sandeep'  # ek self wale variable ki memory binded or ek inherit hoga top wala
    sap_id = 34234
    
    def __init__(self, x, y): # selg is used to refer class member 
      print("I am inside the init of class A")
      self.name =x
      self.sap_id = y
      
    def showA(Self):
       print("inside show off A")

    def atrrib(self):
      print(self.name, self.sap_id)
      print("nothing")

class B(A):
       def __init__(self):
          print("i am inside another class")
       def showB(self):
          print("inside show of B")

class C(B):  # multi level inheritence
   pass      # we can also access class A bby writing class(A,B)

a1 = A("igen", 500123847)
b1 = B()
b1.showA()
b1.showB()
b1.atrrib()

c1 = C()
c1.atrrib()
c1.showB()
c1.showA()
C()