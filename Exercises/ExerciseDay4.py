# Exercise1
dollar_amount = int(input("How many dollars do you got?"))
print("The amount of euros is: " + str(dollar_amount * 0.95))

# Exercise2
ranking = ['John', 'Sen', 'Lisa']
number = int(input("Enter rank number: "))
print(ranking[number-1])

# Exercise3
ranking = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ")
rank = ranking.index(name) + 1
print(rank)