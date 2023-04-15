


# words = 'hello', 'Hey', 'yO', 'YeS'

def print_upper_words(words):
    for word in words:
        print (word.upper())

def print_upper_words2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words3(words, starts_with):
    for word in words:
        for letters in starts_with:
            if word.startswith(letters):
                print (word.upper())