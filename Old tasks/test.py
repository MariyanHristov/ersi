# ersiAge = 24
# ersiGender = 'male'
# ersiStatus = 'online'
# ersiName = 'Ersin'

class Person :
    def __init__(self , age, gender, status, name, money): #self - текущ обект
        self._age = age 
        self._gender = gender
        self._status = status
        self._name = name
        self._money = money

    def eat(self):
        print(f"I am {self._name} and I just ate 10 kg of fin carré chocolate :)")

    def giveMoney(self, person, money):
        if person._status == 'online':
            self._money -= money
            person._money +=money
        else:
            print(f"{person._name} is not online, transaction declined :(")

class Employee(Person): #is-a взаимоотношение (Employee is a Person)
    def otpuska():
        print("I am in otpuska.")


class Pilot(Employee):
    def fly():
        print("I am flyingggg :).")


class Doctor(Employee):
    def operate():
        print("I am operatinggg :))))).") 

#input(a, b, c, d, e)
Ersi = Person(24, 'male', 'online', 'Ersin', 1000)
Mari = Person(21, 'male', 'offline', 'Mari', 500)
Bari = Employee(21, 'male', 'offline', 'Mari', 500)

# print(f"Before giving money, Ersi money: {Ersi._money} | Mari money: {Mari._money}")
# Ersi.giveMoney(Mari, 20)
# print(f"After giving money, Ersi money: {Ersi._money} | Mari money: {Mari._money}")
Bari.otpuska()
Bari.giveMoney(Mari, 30)
################################################################################################################################

# class Engine:
#     pass

# class Tires:
#     pass

# class Car: #has-a 
#     def __init__(self, engine, tires):




