def print_upper_words(words):
    for word in words:
        print(word.upper())

print_upper_words(["Hello", "hi", "yo"])

def print_upper_e_words(words):
    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())

print_upper_e_words(["Good","Electric","eel", 'elementary', 'obfuscate'])

def print_upper_words_specific(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words_specific(["Good","Electric","eel", 'elementary', 'obfuscate'], "e")