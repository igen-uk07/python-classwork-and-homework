# '''class Rectangle:
#     length = 5 
#     breadth = 4
#     def area(self):
#         print(self.length*self.breath)'''

# #write a program to use a class to calculate area and volume of a cube 

class cube:  
     l=10
     b=10
     h=10
     def _int_(self,l,b,h):
        self.l=self.b=self.h
     def area(self):
       print(6 * (self.l*self.b))
     def volume(self):
        print(self.l*self.b*self.h)
c=cube()    
c.area()    
c.volume()

class factorial:
    def fact(n):
        fac = 1
    
        for i in range(1,n+1):
            fac = fac*i

        print(fac)

factorial.fact(4)


class table:
    def tab(n):
        
        for i in range(1,11):
            
        print(n)

table.tab(8)       