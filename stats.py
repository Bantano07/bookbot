def get_word_count(book: str) -> int:
    words = len(book.split())
    return f"Found {words} total words"

def get_char_count(book: str) -> dict[str, int]:
    book_chars = book.lower()
    char_count_dict = {}
    for char in book_chars:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
        
    return char_count_dict

def sort_on(char_tuple: tuple[str, int]) -> int:
    return char_tuple[1]

def chars_dict_to_sorted_list(char_count_dict: dict[str, int]) -> list[tuple[str, int]]:
    unsorted_list = []
    for char in char_count_dict:
        unsorted_list.append((char, char_count_dict[char]))
    
    sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)
    return sorted_list