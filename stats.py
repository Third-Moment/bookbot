def get_character_count(book_text):
    cc = {}
    for word in book_text.lower():
        for letter in word: 
            if letter in cc:
                cc[letter] += 1
            else:
                cc[letter] = 1
    return cc

def get_book_word_count(book_text):
    wc = sum([1 for w in book_text.split()])
    return f"Found {wc} total words"


def get_sorted_list_letter_counts(letter_counts): 
    order = list(letter_counts.items())
    order.sort(reverse=True, key=lambda c: c[1])
    return [{i[0]:i[1]} for i in order]