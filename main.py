def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = num_words(text)
    num_letters = count_letters(text)
    print_report(book_path, num_letters, num_of_words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    dictionary = {}
    for letter in text:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))
 
def print_report(path,num_letters,num_words):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document") 
    print("")
    for key, value in num_letters.items():
        print(f"The {key} character was found {value} times")
    print("--- End report ---")
main()