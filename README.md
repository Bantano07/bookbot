# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple Python program that analyses books and provides information about their text.

# Features
Counts the total number of words in a book.
Counts how many times each character appears.
Sorts characters by how often they appear.
Only displays alphabetic characters in the final report.
Allows different book files to be analysed using a command-line argument.

# How to Use

Run the program from the terminal by providing the path to a book:

python3 main.py books/frankenstein.txt

You can replace frankenstein.txt with another book file in the books folder.

### Example

The program will produce a report showing:

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============

# Project Structure
bookbot/
├── main.py
├── stats.py
├── books/
│   └── all your text files here
└── README.md

# Requirements
Python 3
A text file containing the book you want to analyse