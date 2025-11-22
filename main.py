def get_book_text(input):
        with open(input) as f:
            read_data = f.read()
            return read_data        

def count_words(input):
        word_count = len(input.split())
        return word_count
        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")

main()