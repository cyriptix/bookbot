def count_words_in_text(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count

def count_letters_in_text(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in alphabet:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        else:
            pass
    return letters

def sort_on(item):
    return item["num"]

def generate_sorted_list(letters):
    new_list = []
    for i in letters:
        new_list.append({"char": i, "num": letters[i]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
