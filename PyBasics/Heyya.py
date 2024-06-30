#Data Types

a = 10 #int
b = 10.0 #float
c = 10.00 #double
boo = True #boolean
n = 10 + 2j #complex number

#Data Structures

l = [a,b,c] #list
# append, insert, index, remove, sort, reverse, pop, slices, extend

d = {1:a, 2:b, 3:c} #dictonary
s = set("hello") #set(will only have dictinct values and is unordered)
string = "hello" #string has functions- len, upper, lower, concat, fin, replace, split, join
t = () #immutable and values inside can't be changed

#operators
# in, not in, and, or, not
l2 = [1,2,3,4]
print(5 not int l2)

#class (class is a blueprint and won't do anything until you make an object)
""" class ClassName: # ClassName starts with Capital letters 
        statements """

class Student:
    name = "Niz"
    rank = 1

    def show(self):
        print(self.name)
        print(self.rank)

#object of a class
student1 = Student()
#now it can use functions inside class like this->
student1.show()

# contructors
"""In Python, a constructor is a special method called when an object is created. 
Its purpose is to assign values to the data members within the class when 
an object is initialized. The name of the constructor method 
is always __init__."""

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show(self):
        print(self.name)
        print(self.price)

bmw = Car("BMW", 3000000)
bmw.show()

# Inheritance

class Employee():
    def __init__(self, empname, emproll):
        self.empname = empname
        self.emproll = emproll

    def getdetails(self):
        print(self.empname)
        print(self.emproll)

## creating chold class

class QA(Employee):
    def __init__(self, dept, empname, emproll):
        self.dept = dept
        Employee.__init__(self, empname, emproll)

    def getdept(self):
        print(self.dept)

#creating object for this
obj = QA("Automation", "Ram", 1)
obj.getdetails()


# Now Head Back to PyBasics/ReadMe.md