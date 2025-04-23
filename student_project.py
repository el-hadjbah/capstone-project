"""
Lists
Student Project
Project Title:
Password Manager
"""
#### ---- SETUP ---- ####

passwords = ["xnoMy$X", "d0ghater98", "bownu.m12", "g1an78"]

# Show user their passwords

print("Here are your saved passwords: ")
for password in passwords:
    print(password)
print()

# Ask if they want to remove any

choice = input("Would you like to remove any from this list?(y/n) ")

# If yes, remove their choice
# If no, don't remove any

if choice == "y":
    removed = input("Which would you like to remove? ")
    # If they don't choose a password on the list, ask again
    while removed not in passwords:
        removed = input("Please choose a password from your list ")
    else:
        # Remove the passowrd they chose
        passwords.remove(removed)
        print()
else:
    print()

# Show the remaining passwords

for password in passwords:
    print(password)
print()
    
# Ask if they want to sort it alphabetically

sort_choice = input("Would you like to sort them by alphabetical order?(y/n) ")

# If yes, sort it
# If no, don't sort

if sort_choice == "y":
    # Alphabetically sort it
    passwords.sort()
    print()
else:
    print()

# Show the remaining passwords

for password in passwords:
    print(password)
print()

# Ask if they want to reverse the passwords

reverse_choice = input("Would you like to reverse them?(y/n) ")
print()

# If yes, reverse it
# If no, don't reverse

if reverse_choice == "y":
    for password in passwords:
        # Reverse the passwords
        r = password[::-1]
        print(r)
else:
    print()
    # Show the passwords
    for password in passwords:
        print(password)