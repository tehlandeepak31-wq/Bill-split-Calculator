print("Bill Split Calculator")

bill_amount = float(input("Enter Bill Amount: "))
tip_percentage = float(input("Enter Tip Percentage: "))

tip_amount = (tip_percentage / 100 ) * bill_amount

total_amount = (bill_amount + tip_amount)
print(f"Total (including tip): {total_amount}")

who_payment = int(input("How many people want to Contri.: "))
bill_split = (total_amount / who_payment)
print(f"Each person pays: {bill_split}")

