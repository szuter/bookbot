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

def sort_on(dict):
    return dict["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for c in char_dict:
        if c.isalpha():
            sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(num_words,char_dict,file_path):
    sorted_list = char_dict_to_sorted_list(char_dict)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for c in sorted_list:
        print(f"The '{c['char']}' character was found {c['num']} times")
    print("--- End report ---") 
    
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_number_of_words(text)
    char_dict = get_chars_dict(text)
    print_report(num_words,char_dict,file_path)
            
main()