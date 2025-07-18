from stats import count_words
from stats import count_characters
from stats import sort_char_dict
import sys


def get_book_text(path):
    with open(path) as p:
        return p.read()

def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        relative_path = sys.argv[1]

        text = get_book_text(relative_path)
        num_words = count_words(text)
        char_dict = count_characters(text)
        char_list_decending = sort_char_dict(char_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {relative_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for entry in char_list_decending:
            if entry["char"].isalpha():
                print(f"{entry["char"]}: {entry["num"]}")

        print("============= END ===============")

main() 