# Command-Line Unit Converter
# Williams Nwachi

while True:
  print("1. Temperature")
  print("2. Distance")
  print("3. Weight")
  print("4. Quit")

  choice = input("Choose an option: ")
  if choice == "1":
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    temp_choice = input("Choose direction: ")
    if temp_choice == "1":
      try:
        c = float(input("Enter the value: "))
        f = (c * 9/5) + 32
        print(f"Temperature converted to: {f}")
      except ValueError:
        print("That's not a valid number, try again")
    elif temp_choice == "2":
        try:
          f = float(input("Enter the value: "))
          c = (f - 32) * 5/9
          print(f"Temperature converted to: {c}")
        except ValueError:
          print("That's not a valid number, try again")
    else:
      print("invalid direction, try again")
  elif choice == "2":
    print("1. kilometers to Miles ")
    print("2. Miles to Kilometers ")
    choose_direction = input("Choose the direction: ")
    if choose_direction == "1":
      try:
        k = float(input("Enter the Kilometer value: "))
        m = k * 0.621
        print(f"Kilometers to miles: {m}")
      except ValueError:
        print("That's not a valid number, try again")
    elif choose_direction == "2":
      try:
        m = float(input("Enter the Mile value: "))
        k = m * 1.609
        print(f"Miles is converted to: {k}")
      except ValueError:
        print("That's not a valid number, try again")
    else:
        print("Invalid direction, try again")

  elif choice == "3":
    print("1. kilograms(kg) to Pounds (ibs) ")
    print("2. Pounds (ibs) to Kilograms(kg) ")
    choose_weight = input("Choose direction: ")
    if choose_weight == "1":
      try:
        k = float(input("Enter the Kilogram value: "))
        p = k * 2.2046
        print(f"Kilograms converted to: {p}")
      except ValueError:
        print("That's not a valid number, try again")
    elif choose_weight == "2":
      try:
        p = float(input("Enter the pound value: "))
        k = p * 0.4536
        print(f"Pounds is converted to: {k}")
      except ValueError:
        print("That's not a valid number, try again")
    else:
        print("Invalid direction, try again")
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("invalid option")