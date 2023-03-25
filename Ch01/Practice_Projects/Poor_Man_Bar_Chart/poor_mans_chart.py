import string

def count_letters(sentence):
    # Create an empty dictionary with all the letters of the alphabet
    letter_count = {letter: [] for letter in string.ascii_lowercase}

    # Split the sentence into a list of individual letters
    letters = list(sentence.lower())

    # Loop through each letter and append it to the corresponding list in the dictionary
    for letter in letters:
        if letter in letter_count:
            letter_count[letter].append(letter)

    # Print the results as a bar chart
    for letter, count in letter_count.items():
        bar = letter * len(count)
        print(f"{letter}: {bar}")

# Ask the user to input a sentence
analyze_text = input("Enter a sentence: ")

# Call the count_letters function with the input sentence
count_letters(analyze_text)