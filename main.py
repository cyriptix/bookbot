from stats import count_words_in_text, count_letters_in_text, generate_sorted_list
import sys

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def generate_report(book, wc, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    wc = count_words_in_text(text)
    lc = count_letters_in_text(text)
    sorted_list = generate_sorted_list(lc)
    generate_report(book, wc, sorted_list)
main()
