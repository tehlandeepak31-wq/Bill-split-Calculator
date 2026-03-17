print("Bill Split Calculator")
# This will take Bill Amount as Imput
bill_amount = float(input("Enter Bill Amount: "))
# This line of Code will take a float number from user as Tip Percentage
tip_percentage = float(input("Enter Tip Percentage: "))

tip_amount = (tip_percentage / 100 ) * bill_amount

total_amount = (bill_amount + tip_amount)
print(f"Total (including tip): {total_amount}")
# This will Split Bill Amount Amoung People
who_payment = int(input("How many people want to Contri.: "))

bill_split = (total_amount / who_payment)
# Finally ! This will print Bill Amoung People
print(f"Each person pays: {bill_split}")

