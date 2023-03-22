
def vowel_check(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return word[0].lower() in vowels

def pl_translation(sentence):
    """Function to translate each word into Pig Latin"""
    
    words = sentence.split()
    translated_words = []
    for word in words:
        if vowel_check(word):
            translated_word = word + "way"
        else:
            translated_word = word[1:] + word[0] + "ay"
        translated_words.append(translated_word)
    translated_sentence = " ".join(translated_words)
    return translated_sentence


sentence = input("Please type what you would like me to translate: ")
translated_sentence = pl_translation(sentence)
print(translated_sentence.lower())