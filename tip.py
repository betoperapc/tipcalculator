print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
peeps = int(input("How many people to split the bill? "))
tip_per = tip /100
bill_tip = total * tip_per
total_bill = total + bill_tip
bill_per_person = total_bill / peeps
final = round(bill_per_person, 2)
print(f"The total is ${total_bill}. Each person should pay: ${final}" )
