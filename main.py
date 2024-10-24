def main():
    book_path = 'books/frankenstein.txt'
    get_content = read_book(book_path)
    amount_words = count_words(get_content)
    char_count = count_chars(get_content.lower())
    
    print(f'Reporting information... found path... opening: {book_path}')
    print('============================================================')
    print(f'Amount of words: {amount_words}')
    for item in char_count:
            print(f'The character {item[0]} was found a total of {item[1]} times.')
    print('== End of report ==')
    

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    arr = text.split()
    words = len(arr)
    return words

def count_chars(text):
    chars =  {}
    for count in text:
        if count.isalpha():

            if count in chars:
                chars[count] += 1
            else:
                chars[count] = 1
    sorted_dict = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
main()
