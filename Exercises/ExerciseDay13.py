# Exercise 1
def age_calculator(year_of_birth, current_year=2023):
    age = (current_year - year_of_birth)
    return age


# Exercise 2
user_age = age_calculator(int(input("What is your year of birth? ")))
print(user_age)

# Exercise 3
if user_age > 120:
    print("Wow! You lived a whole lot!")
else:
    print(user_age)

# Exercise 4


def get_names(names):
    new_names = names.split(",")
    number = len(new_names)
    return number


user_names = input("Enter names separated by commas (no spaces):")
print(get_names(user_names))

