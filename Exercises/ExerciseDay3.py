# Exercise1
country = input("Which country are you from?")

match country:
    case "USA":
        print("Hello!")
    case "India":
        print("Namaste!")
    case "Germany":
        print("Hallo!")
    case _:
        print("Please try again!")
# Exercise2
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for ingredient in ingredients:
    print(ingredient.title())
