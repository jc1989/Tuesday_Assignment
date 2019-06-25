#In this assignment you are going to ask the user for the two inputs as shown below: 
#- Enter the total amount 
#- Enter the tip percentage amount
#After the user has entered both inputs the application calculates the tip amount and displays it to the user. 

print("This app is a tip calculator")
total_amount = float(input("Enter the total amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
def tip_amount (total_amount, tip_percentage):
    return total_amount * tip_percentage/100
tip = tip_amount(total_amount, tip_percentage)
result = total_amount + tip
print(f"Your total amount is {result}")