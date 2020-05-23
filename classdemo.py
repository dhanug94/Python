class Circle():
    pi = 3.14
    
    def __init__(self,radius):
        
        self.radius = radius
        self.area = Circle.pi * radius * radius
    
    def getcircumference(self):
        return Circle.pi * self.radius * 2
 
my_circle = Circle(2)

print(my_circle.pi)        
print(my_circle.radius)
print(type(my_circle))
print(my_circle.getcircumference())
print(my_circle.area)



class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print("I am animal")
    
    def eat(self):
        print("I am eating") 
        
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a dog") 
    def eat(self):
        print("I am a dog and I am eating")
    def bark(self):
        print("WOOF!")
        
my_animal = Dog()

print(my_animal.who_am_i())
print(my_animal.__init__())
print(my_animal.eat())
print(my_animal.bark())                                  


#V=πr2h, A=2πrh+2πr2
class Cylinder():
    def __init__(self,height=1,radius=1):
        print("calculating volume and surface area of cylinder")
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.14 * self.radius * self.radius * self.height
    
    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius * self.radius)
    
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())    

#= p(x2 − x1)2 + (y2 − y1)2
from math import sqrt 
class Line():
    def __init__(self, cor1, cor2):
        
        self.cor1 = cor1
        self.cor2 = cor2
        
    def distance(self):
        (x1,y1) = self.cor1
        (x2,y2) = self.cor2
        result =  (x2 - x1)**2 + (y2 - y1)**2
        return sqrt(result)
    
    def slope(self):
        (x1,y1) = self.cor1
        (x2,y2) = self.cor2
        return (y2 - y1) / (x2 - x1)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)    

print(li.distance())
print(li.slope())



class BankAccount():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self,damount):
        
        self.balance = self.balance + damount
        print(f"{damount} amount is added to your account balance")
        print(f"Your current balance is {self.balance}")
        return self.balance
    
    def withdraw(self,wamount):
        
        if self.balance >= wamount:
            
            self.balance = self.balance - wamount
            print(f"{wamount} is withdrawn from your account")
            print(f"Your current balance is {self.balance}")
            return self.balance
        else:
            print("Insufficient funds")       
                        
account =   BankAccount('Dhanashri', 1000) 
print(account.owner)        
print(account.balance) 
print(account.deposit(500))          
print(account.withdraw(1500))  

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("TypeError:multiplication not possible on string characters")
else:
    print(i)
         
try:         
    x = 5
    y = 2
    z = x/y
except:
    print("ZeroDivisionError: Number can not be divisible by 0")
else:
    print(z)
finally:
    print("All Done")       
    
    
    
def ask():
    while True:
        try:
            user_int = int(input("Enter an integer:"))
            answer = user_int**2                  
        except:
            print("Oops! That is not an integer.Please enter an integer")
            continue
        else:
            print("Thank you for your input")
            print(answer)
            break
        finally:
            print("End")
ask()                    