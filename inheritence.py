class parent():
    def values(self):
        print("Total cost is 5 crore")

class son():
    def values(self):
        print("Son has his own property ")

class Daughter():
    def values(self):
        print("Daughter is settled abroad ")

p1 = parent()
p2 = son()
p3 = Daughter()

p1.values()
p2.values()
p3.values()


class parent():
    def property(self):
        print("Total cost is 5 crore")

class son(parent):
    def values(self):
        print("Son has his own property ")

class Daughter(parent):
    def values(self):
        print("Daughter is settled abroad ")

p1 = parent()
p2 = son()
p3 = Daughter()

p1.property()
p2.values()
p3.values()


