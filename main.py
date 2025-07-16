from stats import count_words


def get_book_text(path):
    with open(path) as p:
        return p.read()

def main():

    relative_path = "./books/frankenstein.txt"

    text = get_book_text(relative_path)
    num_words = count_words(text)

    print(f"{num_words} words found in the document")

main()