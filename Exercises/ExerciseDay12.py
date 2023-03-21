# Exercise 1
def convert_to_cubic(liter):
    cubic = liter / 1000
    return cubic


print(convert_to_cubic(3000))
# Exercise 2


def length(password_arg):
    if len(password_arg) >= 8:
        result_length = True
    else:
        result_length = False
    return result_length


def digit(password_arg):
    digit_local = False
    for i in password_arg:
        if i.isdigit():
            digit_local = True
    return digit_local


def uppercase(password_arg):
    uppercase_local = False
    for i in password_arg:
        if i.isupper():
            uppercase_local = True
    return uppercase_local


password = input("Enter new password: ")

results = {"length": length(password), "digit": digit(password), "upper-case": uppercase(password)}

print(results)
print(results.values())

if all(results.values()):
    print("Strong Password")
else:
    print("Weak Password")
