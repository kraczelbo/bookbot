def report(letters):
    formatted_lines = []
    for i, count in letters.items():
        formatted_lines.append(f"The '{i}' character was found {count} times")
    return "\n".join(formatted_lines)

def count_letters(words):
    letter_count = {}
    text = words.replace(" ", "").lower()
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    sorted_counts = dict(sorted(letter_count.items()))
    return sorted_counts

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
    letter_count = count_letters(read)
    letter_list = report(letter_count)
    print(read)
    print(f"{count} words found in the document")
    print(letter_list)
    

if __name__ == "__main__":
    main()  