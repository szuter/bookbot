def get_book_text(file_path):    
    with open(file_path) as f:
        return f.read()
    
def get_number_of_words(text):
    words_list = text.split() 
    return len(words_list)

def get_chars_dict(text):
    char_dict = {}
    lowered_text =text.lower()
    for c in lowered_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

    
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_number_of_words(text)
    char_dict = get_chars_dict(text)
    print(char_dict)
            
main()