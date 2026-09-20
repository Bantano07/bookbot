              User
                ↓
        Command-line input
                ↓
          ┌───────────────┐
          │ get_book_text │
          │ Reads the     │
          │ book file     │
          └───────────────┘
                ↓
           Book contents
             ↙       ↘
            ↓         ↓
 ┌────────────────┐  ┌────────────────┐
 │ get_word_count │  │ get_char_count │
 │ Counts words   │  │ Counts each    │
 │ in the book    │  │ character      │
 └────────────────┘  └────────────────┘
            ↓                ↓
       Word count     Character dictionary
                              ↓
                   ┌─────────────────────────┐
                   │ chars_dict_to_sorted_list│
                   │ Sorts characters by     │
                   │ their count             │
                   └─────────────────────────┘
                              ↓
                       Sorted character list
                              ↓
                    ┌─────────────────┐
                    │  print_report   │
                    │ Displays the    │
                    │ final results   │
                    └─────────────────┘
                              ↓
                         Console output