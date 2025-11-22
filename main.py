def get_book_text(book):
        with open(book) as f:
            read_data = f.read()
            return read_data        
        
        
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()