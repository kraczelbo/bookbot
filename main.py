def count_words(book):
    words = book.split()
    for i in range(0, len(words)+1):
        number = i
    return number



def read_book(book):   
    with open(book) as f:
        return f.read()


def main():
    book_path = ("books/frankenstein.txt")
    read = read_book(book_path)
    count = count_words(read)
    print(read)
    print(count)
    

if __name__ == "__main__":
    main()  