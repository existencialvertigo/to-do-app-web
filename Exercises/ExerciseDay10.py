# Exercise 1
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = (value * 100) / total_value
    print("That is " + str(percentage) + "%")
except ValueError:
    print("You need to enter a number. Run the program again.")

# Exercise 2
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = (value * 100) / total_value

    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")

# Bug-Fixing Exercise 1
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")
