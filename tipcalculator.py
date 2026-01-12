print("Wlecome to the tip calculator")
bill=float(input("Enter the amount in the bill"))
tip=int(input("What precentage of tip would you like to give?"))
people =int(input("How many people to split the bill?"))
bill_with_tip = bill*(tip/100)
total_tip = bill_with_tip/people
print(total_tip)
