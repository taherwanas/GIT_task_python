class Person:
    def __init__(self , name , age , money , mood , healthRate):
        self.name = name
        self.age = age
        self.money = money
        self.mood = mood
        self.healthRate = max(0 , min(healthRate , 100))

    def sleep(self , hours):
        if hours == 7 :
            self.mood = "happy"
        elif hours < 7 :
            self.mood = "tierd"
        elif hours > 7 :
            self.mood = "lazy"

    def eat(self , meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy (self , items):
        self.money -= items*10





class Employee(Person):
    def __init__(self, name, age, money, mood, healthRate , employee_id , car , email , salary , distanceToWork):
        super().__init__(name, age, money, mood, healthRate)
        self.employee_id = employee_id
        self.car = car
        self.email = email
        if salary > 0:
            self.salary = salary
        else:
            print("Invalid salary! salary will be = 0")  
            self.salary = 0
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours < 8:
            self.mood = "Lazy"
        else:
            self.mood = "Tired"

    def drive(self, distance):
        if self.car:
            self.car.run(distance, self.car.velocity)
        else:
            print(f"{self.name} doesn't have a car to drive!")

    def refuel(self, gasAmount=100):
        if self.car:
            self.car.refuel(gasAmount)
        else:
            print("This employee doesn't have a car!")

    def send_mail(self, to, subject, body):
        print(f"Sending Email to {to}\nSubject: {subject}\nBody: {body}")


    def introduce(self):
        name = self.name
        age = self.age
        email = self.email
        print(f"name : {name} , age : {age} , email : {email} , work at : {self.office.office_name}")





class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = max(0, min(fuelRate, 100))
        self.velocity = max(0, min(velocity, 200))

    def run(self, distance, velocity):
        if self.fuelRate <= 0:
            print(f"The car {self.name} has no fuel! It can't run.")
            self.stop()
            return
        
        self.velocity = max(0, min(velocity, 200))
        print(f"The car {self.name} is running {distance} km at {self.velocity} km/h")

        fuel_consumed = distance
        self.fuelRate = max(0, self.fuelRate - fuel_consumed)

        if self.fuelRate == 0:
            print(f"The car {self.name} ran out of fuel!")
            self.stop()

    def stop(self):
        self.velocity = 0
        print(f"The car {self.name} has stopped.")

    def refuel(self, gasAmount):
        self.fuelRate = min(100, self.fuelRate + gasAmount)
        print(f"The car {self.name} has been refueled to {self.fuelRate}%.")




class Office:
    employeesNum = 0  

    def __init__(self, office_name):
        self.office_name = office_name  
        self.employees = []  

    def hire(self, employee):
        if isinstance(employee, Employee):  
            self.employees.append(employee)
            Office.employeesNum += 1
            print(f"Employee {employee.name} hired at {self.office_name}")
        else:
            print("Invalid employee! Only Employee objects can be hired.")
        employee.office = self

    def fire(self, empId):
        employee = self.get_employee(empId)  
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1
            print(f"Employee {employee.name} fired from {self.office_name}")
        else:
            print("Employee not found!")

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.employee_id == empId:
                return emp  
        return None  

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrivalTime = moveHour + (distance / velocity)  
        return "Late" if arrivalTime > targetHour else "On Time"


