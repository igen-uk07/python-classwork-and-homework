'''class Employee:
    Name = "KRISHN"
    Dept = "CSE"
    def info(self):
        print(self.Name,self.Dept)

E1 = Employee
E2 =Employee
E1.info(E1)
E2.info(E2)'''

class Employee:
    N = "ram"
    D = "HR"
    def _int_(self, N, D):
        self.N=N
        self.D=D
        print(self.N,self.D)
    def address(self,city):
        print(city)

E1 = Employee()
E1._int_(E1)