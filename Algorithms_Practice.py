#WRITE A PROGRAM THAT WILL REMOVE DUPLICATES FROM THE ARRAY
#AFTER THE DUPLICATES ARE REMOVED IT SHOULD BE 
#names = ["Alex","John","Mary","Steve"]

#initilizing array named names
names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
numbers = [23,4,6,8,3,9,23,534,6,7467,858567]
nine_ints = [0,1,2,3,4,5,6,8,9]
duplicate_array = [1,2,3,4,5]
new_duplicate_array = []
height = int(input("Please input the height of your pyramid!"))

#defining function called names checked that takes one argument, names
def names_checker(names):
    #declared new array with value equal to names[0]
    clean_names = [names[0]]
    #loop through each name in names array
    for name2 in names:
        #declare variable that is equal to False used to determine if clean names includes current name
        clean_includes_name2 = False
        #loop through each name in clean_names
        for name in clean_names:
            #check if current name from clean names is equal to name2, and if it is, change clean_includes_name2 to True
            if name == name2:
                clean_includes_name2 = True
        #If clean_names does not include name2
        if clean_includes_name2 == False:
            clean_names.append(name2)
    #print clean_names
    print(f"\nThe original array consisted of: \n {names}.\n\nAfter removing the duplicate indexes, the new array consists of: \n {clean_names}")

#PRINT LARGEST NUMBER IN AN ARRAY
def largest_find(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    print(f"\nThe largest number in the array is:\n {max}")

#PRINT SMALLEST NUMBER IN AN ARRAY
def smallest_find(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    print(f"\nThe smallest number in the array is:\n {min}")

#DETERMINE THE MISSING ELEMENT IN THE ARRAY
def missing_find(nine_ints):
    for i in range(0, len(nine_ints)):
        for num in nine_ints:
            if i == num:
                break
    else:
        print(f"\nThe missing number in the array is:\n {i}")


#DUPLICATE THE GIVEN ARRAY AND ADD IT TO THE EXISTING ARRAY
def duplicate(new_duplicate_array,duplicate_array):
    new_duplicate_array += duplicate_array * 2
    print(f"\nThe duplicated array looks like {new_duplicate_array}\n")

#HARD ASSIGNMENT - DISPLAY A PYRAMID
def pyramid(height):
    bottom_row = (height * 2) + 1
    for i in range(0, height):
        row_length = i * 2 + 1
        spaces = int((bottom_row - row_length) / 2)
        print(" " * spaces + "*" * row_length + " " * spaces)
        
names_checker(names)
largest_find(numbers)
smallest_find(numbers)
missing_find(nine_ints)
duplicate(new_duplicate_array, duplicate_array)
pyramid(height)