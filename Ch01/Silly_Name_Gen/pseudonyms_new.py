import sys, random

print('Welcome to the Psych "Sidekick Name Picker."')
print('A name just like Sean would pick for Gus:')

while True:
    
    firstName = random.choice(first)
    lastName = random.choice(last)

    print('\n')
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print('\n')
    
    try_again = input("Try again? (Press Enter to continue or 'n' to quit)")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")    
