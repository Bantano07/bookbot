from stats import get_word_count, get_char_count

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

book_contents = get_book_text("books/frankenstein.txt")

print(get_word_count(book_contents))
print(get_char_count(book_contents))                                                            