#Write an app which asks users for the input and then prints the factorial for that number.
print(f"Please enter a number to find its factorial")
number = int(input("Please enter a number: "))
#array = [number]
#for index in range(0, number + 1):
#    print(array[index])
factorial = 1
for x in range(1, number + 1):
    factorial *= x
print(f"This factorial for this number is {factorial}")