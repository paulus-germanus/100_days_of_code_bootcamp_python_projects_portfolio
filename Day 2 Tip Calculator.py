print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))

people_number = int(input("How many people to split the bill? "))

per_person = (total + total * tip/100) / people_number

print(f"Each person should pay: {round(per_person, 2)}")