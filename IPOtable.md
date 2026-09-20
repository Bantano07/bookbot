| **Input**                            | **Process**                                                               | **Output**                  |
| ------------------------------------ | ------------------------------------------------------------------------- | --------------------------- |
| Book file path entered by the user   | `sys.argv` gets the file path                                             | Selected book file          |
| Book `.txt` file                     | `get_book_text()` reads the file                                          | Book contents               |
| Book contents                        | `get_word_count()` counts the words                                       | Total word count            |
| Book contents                        | `get_char_count()` counts each character                                  | Character count dictionary  |
| Character count dictionary           | `chars_dict_to_sorted_list()` sorts characters by their count             | Sorted character list       |
| Word count and sorted character list | `print_report()` displays the results and skips non-alphabetic characters | Final report in the console |
