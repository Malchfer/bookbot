import sys
from stats import count_words,count_characters, dict_sort

def get_book_text(path):
    with open(path) as f:
        read_data = f.read()
        return read_data        

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for character in dict_sort(count_characters(book_text)):
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

main()
