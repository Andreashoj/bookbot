import sys
from stats import get_word_count, get_character_appearance

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    path = sys.argv[1]
    content = get_book_text(path)
    words_count = get_word_count(content)
    character_appearances = get_character_appearance(content)

    print_report(path, words_count, character_appearances)


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
         file_contents = f.read()

    return file_contents

def print_report(path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char}: {char_count[char]}")



main()
