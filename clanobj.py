class students:
# [assignment] skeleton class. Add your code here 

 def _init_(self, name, rollno, m1, m2):
    self.name = name
    self.rollno = rollno
    self.m1 = m1
    self.m2 = m2
    

def accept(self, Name, Rollno, marks1, marks2) :
    ob = Student(Name, Rollno, marks1, marks2)
    ls.append(ob)

def display(self, ob) :
    print("Name    : ", ob.name)
    print("RollNo  : ", ob.rollno)
    print("Marks1  : ", ob.m1)
    print("Marks2  : ", ob.m2)
    print("\n")

def search(self, rn):
    for i in range(ls._len_()):
        if(ls[i].rollno == rn):
            return i

def delete (self, rn):
    i = obj.search(rn)
    del ls[i]


def update(self, rn, No):
    i = obj.search(rn)
    roll = No
    ls[i].rollno = roll

print("\nOperations used, ")

obj.accept("A", 1, 80, 80)
obj.accept("B", 2, 70, 70)
obj.accept("C", 3, 85, 85)

print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])

obj.update(3, 2)
print(ls._len_())
print("List After updation")
for i in range(ls._len_()):
    obj.display(ls[i])

