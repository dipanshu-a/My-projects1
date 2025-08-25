

# Project Tip calculator

print("welcome to the tip calculator!")

bill = float(input("what is the total bill?"))

tip = int(input("which persentage? 0 ,10 ,20, 30,100 "))

people = int(input("how many people split the bil?"))

tip_as_percentage = tip/100

total_tip_amount = bill * tip_as_percentage

total_bill = bill + total_tip_amount

bill_per_person = total_bill/people

final_amount = round(bill_per_person,2)

print(f"each person should pay {final_amount}")