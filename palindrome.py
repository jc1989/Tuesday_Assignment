#Create an app which detects if the input word is a palindrome or not. 
print(f"Please enter in a word to determine if it's a palindrome!")
pal_input = str(input("Please enter in a word: "))

reverse_input = ""

for y in range(len(pal_input) - 1, -1, -1):
    reverse_input = reverse_input + pal_input[y]

if pal_input == reverse_input:
    print(f"The word {pal_input} is a palindrome.")
else:
    print(f"This is not a palindrome.")
