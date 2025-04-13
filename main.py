import sys
from stats import get_book_word_count, get_character_count, get_sorted_list_letter_counts
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    char_cnts = get_character_count(get_book_text(book_path))
    word_cnts = get_book_word_count(get_book_text(book_path))
    sort_char_cnts = get_sorted_list_letter_counts(char_cnts)
    
    header = f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ---------- """
    
    print(f"""{header} \n{word_cnts} \n--------- Character Count ------- \n""")
    [print(f"{k}: {v}") for i in sort_char_cnts for k,v in i.items() if k.isalpha() == True]
    print("============ END ===============")

main()
