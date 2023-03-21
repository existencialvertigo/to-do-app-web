# Exercise1
filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    print(f"{index+1}-{item.capitalize()}.txt")
# Exercise2
ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input("Enter the index of the IP you want:"))
print(f"You chose {ips[user_input]}")
