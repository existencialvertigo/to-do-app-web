# Exercise 1
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]

print(names)

# Exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]

print(usernames)

# Exercise 3
user_entries = ['10', '19.1', '20']
user_entries = [float(user_entry) for user_entry in user_entries]

print(user_entries)

# Exercise 4
user_entries = ['10', '19.1', '20']
user_entries = [float(user_entry) for user_entry in user_entries]

print(sum(user_entries))
