#Greeting to the user
print("Welcome to the tip calculator!")

#Ask the user to input the total bill, tip amount and number of people to split the bill between.
bill = float(input("What was the total bill?\n$"))

tip = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

people = int(input("How many people to split the bill? \n"))

#Convert tip for calculation
tip_float = (tip / 100) + 1

#Calculate total bill payment per person to two decimal places.
total_payment = "{:0.2f}".format((bill / people) * tip_float)

print(f"Each person should pay ${total_payment}")