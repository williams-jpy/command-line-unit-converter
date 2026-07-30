from ast import arg
def create_profile(name, age, *args, **kwargs):
  print("\n------PROFILE-----")
  print(f"Nmae: {name}")
  print(f"Age: {age}")

  print("\nHobbies:")
  for hobby in args:
    print(f"-{hobby}")

  print("\nOther information:")
  for key, value in kwargs.items():
    print(f"{key.title()}: {value}")

# Get name
name = input("Enter your name: ").title()

#Get a valid age
while True:
  try:
    age = int(input("Enter your age: "))
    break
  except ValueError:
    print("Age must be a number. Please try again")


# Get hobbies
hobby1 = input("Enter your first hobby: ").title()
hobby2 = input("Enter your second hobby: ").title()

# Get other information
country = input("Enter your country: ").title()
occupation = input("Enter your occupation: ").title()


# Call the function
create_profile(name, age, hobby1, hobby2, country=country, occupation=occupation)
