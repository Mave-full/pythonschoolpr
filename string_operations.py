def split_into_words(s):
    words = s.split()
    return words

def count_word_occurrences(s, target_word):
    words = s.lower().split()
    return words.count(target_word.lower())

def add_exclamation(s):
    if not s.endswith("!"):
        return s + "!"
    return s
