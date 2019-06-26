#Assignment 3: Take input from the user and find out if that number is prime or not.

print("This programs determines whether your input is a prime number or not!")
#number = int(input("Please enter a number: "))

def user_input():
    number = int(input("Please enter a number: "))
    return number

def prime_checker(number):
    if number > 1:
        for x in range(2, number):
            if (number % x == 0):
                y = 1
                break
        else:
            y = 0
    else:
        y = 1
    return y

def print_prime(y, number):
    if y == 0:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

number1 = user_input()
checker = prime_checker(number1)
print_prime(checker,number1)


