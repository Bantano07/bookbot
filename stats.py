def get_word_count(book: str) -> int:
    # Count the number of words in the book
    words = len(book.split())
    
    # Return the word count
    if words == 1:
        return f"Found 1 total word"
    else: 
        return f"Found {words} total words"


def get_char_count(book: str) -> dict[str, int]:
    # Convert all characters to lowercase
    book_chars = book.lower()
    
    # Create a dictionary to store character counts
    char_count_dict = {}
    
    # Go through each character and count how often it appears
    for char in book_chars:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
        
    return char_count_dict


def sort_on(char_tuple: tuple[str, int]) -> int:
    # Use the character count for sorting
    return char_tuple[1]


def chars_dict_to_sorted_list(char_count_dict: dict[str, int]) -> list[tuple[str, int]]:
    # Create a list from the character dictionary
    unsorted_list = []
    
    for char in char_count_dict:
        unsorted_list.append((char, char_count_dict[char]))
    
    # Sort characters from highest to lowest count
    sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)
    
    return sorted_list