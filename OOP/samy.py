import oop

samy_car = oop.Car("Fiat 128", 100, 60)

samy = oop.Employee("Samy", 35, 5000, "Neutral", 90, 201, samy_car, "samy@iti.com", 7000, 20)

iti_office = oop.Office("ITI Smart Village Office")

iti_office.hire(samy)

samy.introduce()

samy.drive(20)

print(f"Fuel level after driving: {samy.car.fuelRate}%")

lateness_status = oop.Office.calculate_lateness(9, 8, 20, samy.car.velocity)
print(f"Samy's lateness status: {lateness_status}")

if lateness_status == "Late":
    samy.salary -= 100
    print("Samy was late! 100 L.E deducted from salary.")
else:
    print("Samy was on time.")

print(f"Samy's salary after lateness check: {samy.salary} L.E")

if samy.car.fuelRate < 50:
    print("\nRefueling Samy's car...")
    samy.refuel(50)
    print(f"Fuel level after refueling: {samy.car.fuelRate}%")

