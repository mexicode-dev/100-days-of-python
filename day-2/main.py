print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip_to_give = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_amount = total_bill * (tip_to_give / 100)
split_the_bill = int(input("How many people to split the bill? "))
if split_the_bill == 0 :
    print("We don't divide by 0")
    split_the_bill = int(input("How many people to split the bill? "))

results_after_split = (total_bill + tip_amount) / split_the_bill
print(f"Each person should pay: ${round(results_after_split, 2)}")