print("Welcome to the tip calculator!")
total_bill = float(input("What was your total bill? "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip = float(tip_amount / 100)
split_number = int(input("How many people to split the bill? "))

each_split = round((total_bill / split_number) * tip, 2)
print(type(each_split))

print(f"Each person should pay: ${each_split}")
