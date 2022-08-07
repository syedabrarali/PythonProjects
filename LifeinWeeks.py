age = input("What is your current age?")
age_left = 90 - int(age)
days = age_left * 365
week = age_left * 52
months = age_left * 12 
print(f"You have {days} days, {week} weeks, and {months} months left")
