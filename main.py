from stats import *
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

argument1 = sys.argv[1]

def main():
    book_path = argument1
    read = get_book_text(book_path)
    word_count = get_word_count(read)
    characters = count_characters(read)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in characters:
        print(f"{key}: {value}")
    print("============= END ===============")


main()