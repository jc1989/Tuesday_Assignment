#Write an app which separatly takes first name and last name of the user. Once the name is taken print out the following message:
#Hello, My name is FirstName, LastName

def greet(first_name,last_name):
  print(f"Hello, my name is {first_name}, {last_name}")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greet(first_name,last_name)