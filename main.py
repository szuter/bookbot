def get_book_text(file_path):    
    with open(file_path) as f:
        return f.read()
    
def get_number_of_words(text):
    words_list = text.split() 
    return len(words_list)

    
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_number_of_words(text)
    print(num_words)
            
main()