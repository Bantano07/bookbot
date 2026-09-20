  Book text
                   ↓
          ┌─────────────────┐
          │ get_word_count  │
          │ Counts the words│
          └─────────────────┘
                   ↓
              Word count
                   
                   ↓
          ┌─────────────────┐
          │ get_char_count  │
          │ Counts each     │
          │ character       │
          └─────────────────┘
                   ↓
          Character dictionary
                   ↓
      ┌─────────────────────────┐
      │ chars_dict_to_sorted_list│
      │ Converts dictionary to   │
      │ a sorted list            │
      └─────────────────────────┘
                   ↓
             Sorted list
                   ↑
          ┌─────────────────┐
          │    sort_on      │
          │ Sorts by the    │
          │ character count │
          └─────────────────┘