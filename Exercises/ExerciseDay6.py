# Exercise1
file = open("essay.txt", "r")
content = file.read()
print(content.title())
file.close()

# Exercise2
file = open("essay.txt", "r")
content = file.read()
print(len(content))

# Exercise3
file = open("members.txt", "r")
members = file.readlines()
file.close()


file = open("members.txt", "w")
new_member = input("Add a new member: ") + "\n"
members.append(new_member)
file.writelines(members)
file.close()

file = open("members.txt", "r")
members = file.readlines()
for member in members:
    print(member)

# Exercise4
filenames = ["file1.txt", "file2.txt", "file3.txt"]

for filename in filenames:
    file = open(filename, "w")
    file.write("Hello")
    file.close()
    file.close()

# Exercise5
filenames = ["a.txt", "b.txt", "c.txt"]
for filename in filenames:
    file = open(filename, "r")
    print(file.read())
    file.close()
