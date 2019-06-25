#Create an app which takes two numbers as input from the user and then prints out the results of addition on the screen. 
x= int(input("Enter in a number: "))
y= int(input("Enter in another number: "))

def add_two(x, y):
    result = x + y
    return result

result = add_two(x,y)

print(f"The two numbers you've entered add up to {result}")