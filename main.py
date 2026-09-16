def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

book_contents = get_book_text("books/frankenstein.txt")

def word_count(book: str) -> int:
    words = len(book.split())
    print(f"Found {words} total words")

word_count(book_contents)