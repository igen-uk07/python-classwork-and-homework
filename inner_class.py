class employee:
    def __init__(self):
      self.name= "sandeep"
      self.sapid= 439843984
      self.AC =self.activity_coordinator()
    def info(self):
      print(self.name , self.sapid)

    class activity_coordinator:
        def info(self):
            print("i am the activity coordinator for  8 semester")

E1= employee()
E1.info()
E2 = E1.AC
E2.info()



class assistent_professor:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
        print(f"My name is :{ self.name }")
        print(f"My Id is  : { self.id }")

    class member:
        def show(self):
            print("i m board memeber also")
    
AP = assistent_professor.member()
AP.show()
Ap1 = assistent_professor('sandeep', 2321323)
Ap1.show()
Ap2 = Ap1.member()
Ap2.show()