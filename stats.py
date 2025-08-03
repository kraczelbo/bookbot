def get_book_text(book):
    with open(book) as f:
        file_content = f.read()
        return file_content

def get_word_count(string):
    words = string.split()
    return len(words)

def count_characters(string):
    letter_count = {}
    for words in string:
        lower_case = words.lower()
        if words.isalpha():
            if lower_case in letter_count:
                letter_count[lower_case] += 1
            else:
                letter_count[lower_case] = 1
    return sorted(letter_count.items(), key=lambda item: item[1], reverse=True)


#def sorted_letters_count(letters):
    #return sorted(letters.items(), key=lambda item: item[1], reverse=True)

    
        



    