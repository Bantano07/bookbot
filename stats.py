from main import book_contents

def get_word_count(book: str) -> int:
    words = len(book.split())
    print(f"Found {words} total words")

def get_char_count(book: str) -> dict[str, int]:
    book_chars = book.lower()
    char_count_dict = {"a": 0, "b": 0, "c":0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0,
                        "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for char in book_chars:
        char_count_dict[char]+1
        
    return char_count_dict