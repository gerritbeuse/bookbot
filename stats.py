def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()

    char_dict = {}
    
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    char_list = []

    for key, value in char_dict.items():
        char_dict_item = {"char":key, "num":value}
        char_list.append(char_dict_item)

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list