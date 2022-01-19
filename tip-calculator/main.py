print("Welcome to tip calculator")

total_bill = input("What was the total bill? $")
total_bill = float(total_bill)
no_of_split = input("How many people to split the bill?")
no_of_split = int(no_of_split)
percentage_of_tip = input("what percentage tip would you like to give? 10, 12 or 15? ")
percentage_of_tip = int(percentage_of_tip)
tip = (percentage_of_tip/100)*total_bill

each_split = (total_bill + tip)/no_of_split

print("Each person should pay: $"+str(round(each_split,1)))