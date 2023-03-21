# Exercise 1
def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value = max(grades)
    return max_value


value = get_max()
print(value)


# Exercise 2
def get_max_min():
    grades = [9.6, 9.2, 9.7]
    max_value = max(grades)
    min_value = min(grades)
    max_min = f"Max: {max_value}, Min: {min_value}"
    return max_min


value = get_max_min()
print(value)
