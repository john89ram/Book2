def is_vowel(char):
    vowels = "AEIOUaeiou"
    return char in vowels

def pig_latin_translator(word):
    if word[0].isalpha() and is_vowel(word[0]):
        # If the word starts with a vowel, simply add "ay" to the end
        return word + "ay"
    
    # Find the index of the first vowel
    for index, letter in enumerate(word):
        if is_vowel(letter):
            break
    else:
        # If there are no vowels, return the original word
        return word

    # Move the consonant cluster to the end and add "ay"
    return word[index:] + word[:index] + "ay"

def translate_sentence(sentence):
    # Capitalize the first letter of the sentence
    capitalized_sentence = sentence.capitalize()

    # Split the sentence into words and special characters
    import re
    words_with_special_chars = re.findall(r"[\w']+|[.,!?;]", capitalized_sentence)

    # Translate each word and store the results in a list
    translated_words = [pig_latin_translator(word) for word in words_with_special_chars]

    # Join the translated words back into a sentence
    translated_sentence = " ".join(translated_words)

    return translated_sentence

# Get user input
user_input = input("Enter a sentence: ")

# Translate the sentence to Pig Latin
translated_sentence = translate_sentence(user_input)

# Print the result
print("Pig Latin translation:", translated_sentence)
