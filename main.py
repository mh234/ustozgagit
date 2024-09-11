# 1.1
# Konsepsii OOP
# Classi i obekti , inkapsulyatsiya, nasledovaniye,polimorfizm


# 1.3
# Inkapsulyatsiya v oop eto tip kotoriy privatniy i k nemu dostup ogranichen.



# 1.4
# Nasledovaniye - pozvolyaet sozdavat noviye klassi na osnove sushestvuyushix

2.1
is_even = input("Give me number :")
if is_even %2 == 0:
    print("True")
else:
    print("False")

2.2
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(make,model,year):
        return year,model,make
   
print(Car.display_info("China","Toyota sss", "1900"))

2.3 
numbers = int(input("Give me numbers     "))

if numbers>0:
    print(numbers)
else:
    print("False")


2.4
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(name, age):
        print(f"Hello my name is {name}, im {age} years old")
print(Person.greet('Ismoil','19'))




3.1
S = input("give me word")
A = S [::-1]
if S == A:
    print("Polindrom")
else:
    print("False")



3.2
Balance = 1000
class BankAccount:
    def __init__(self,deposit,withdraw,get_balance):
        self.popolneniye = deposit
        self.obnolichit = withdraw
        self.balanc = get_balance

Bank  = input("balance or obnolichit or popolneniye    ")
if Bank == 'balance':
    print(Balance)
if Bank == "obnolichit":
    A = int(input("skolko hotite obnolichit    "))
    print(Balance - A)    
if Bank == 'popolnenie':
    B = int(input("na skolko popolnite"))
    print(Balance - B)# 1.1
# Konsepsii OOP
# Classi i obekti , inkapsulyatsiya, nasledovaniye,polimorfizm


# 1.3
# Inkapsulyatsiya v oop eto tip kotoriy privatniy i k nemu dostup ogranichen.



# 1.4
# Nasledovaniye - pozvolyaet sozdavat noviye klassi na osnove sushestvuyushix

2.1
is_even = input("Give me number :")
if is_even %2 == 0:
    print("True")
else:
    print("False")

2.2
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(make,model,year):
        return year,model,make
   
print(Car.display_info("China","Toyota sss", "1900"))

2.3 
numbers = int(input("Give me numbers     "))

if numbers>0:
    print(numbers)
else:
    print("False")


2.4
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(name, age):
        print(f"Hello my name is {name}, im {age} years old")
print(Person.greet('Ismoil','19'))




3.1
S = input("give me word")
A = S [::-1]
if S == A:
    print("Polindrom")
else:
    print("False")



3.2
Balance = 1000
class BankAccount:
    def __init__(self,deposit,withdraw,get_balance):
        self.popolneniye = deposit
        self.obnolichit = withdraw
        self.balanc = get_balance

Bank  = input("balance or obnolichit or popolneniye    ")
if Bank == 'balance':
    print(Balance)
if Bank == "obnolichit":
    A = int(input("skolko hotite obnolichit    "))
    print(Balance - A)    
if Bank == 'popolnenie':
    B = int(input("na skolko popolnite"))
    print(Balance - B)