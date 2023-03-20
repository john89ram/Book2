import random, csv

filepath = "Ch01/Silly_Name_Gen/Names/silly_names.csv"

with open(filepath) as f:
    reader = csv.reader(f)
    names = list(reader)

print('Welcome to the Psych "Sidekick Name Picker."')
print('A name just like Sean would pick for Gus:')

while True:
    
    firstName = random.choice(names)[0]
    lastName = random.choice(names)[1]

    print('\n')
    print(f"{firstName} {lastName}")
    print('\n')
    
    try_again = input("Try again? (Press Enter to continue or 'n' to quit)")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")    
