from stats import count_words,count_characters

def get_book_text(input):
    with open(input) as f:
        read_data = f.read()
        return read_data        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")
    print(count_characters(book_text))

main()