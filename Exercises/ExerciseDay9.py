# Exercise 1
user_password = input("Enter your password: ")

if len(user_password) > 7:
    print("Great password there!")
if len(user_password) <= 7:
    print("Your password is weak.")

# Exercise 2
if len(user_password) > 7:
    print("Great password there!")
if len(user_password) == 7:
    print("Password is OK, but not too strong.")
else:
    print("Your password is weak.")
