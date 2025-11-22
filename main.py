from stats import count_words,count_characters, dict_sort

def get_book_text(input):
    with open(input) as f:
        read_data = f.read()
        return read_data        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for character in dict_sort(count_characters(book_text)):
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()