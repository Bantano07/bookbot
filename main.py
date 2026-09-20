import sys
from stats import get_word_count, get_char_count, chars_dict_to_sorted_list
#Imports functions from stats.py file

if len(sys.argv) < 2:
    # CHecks if user input a file
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path_to_file: str) -> str:
    # File contents converted to a string
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path: str, word_count: int, sorted_char_count: list[tuple[str, int]]):
    # Final output logged to console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")

    if sorted_char_count == []:
        print("Found 0 total characters")

    for char in sorted_char_count:
        # Skips non-alphanumeric characters
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")

    print("============= END ===============")
   
book_contents = get_book_text(book_path)
word_count = get_word_count(book_contents)
char_count = get_char_count(book_contents)
sorted_char_count = chars_dict_to_sorted_list(char_count)

# Final function call
print_report(book_path, word_count, sorted_char_count)