print("Welcome to the tip calculator")
a=float(input("What was the total bill? $"))
b=int(input("How much tip would you like to give? 10, 12, 15 percent? "))
c=int(input("How many people to split the bill in? "))
total_bill=a+((b//100)*a)
per_person_bill=total_bill//c
print(f"Each person should pay ${per_person_bill}")
