# Library Management System

A command-line interface (CLI) application for managing a library's book inventory and lending operations, implemented in Python.

## Overview

This Library Management System allows librarians to efficiently manage their book collection, track lending activities, and maintain an up-to-date inventory. The system is designed with a focus on simplicity and functionality, making it easy to use for library staff.

## Key Features

- Add new books to the library inventory
- View all books in the collection
- Search for books by title, ISBN, or author
- Remove books from the inventory
- Lend books to borrowers
- Track lent books and borrowers
- Return books and update inventory
- Automatic data persistence using JSON file storage

## Project Structure

- `main.py`: Entry point of the application
- `library.py`: Contains the Library class with core functionality
- `book.py`: Defines the Book class
- `file_handler.py`: Handles saving and loading data
- `utils.py`: Utility functions for input handling

## Technical Details

- Implemented in Python 3.x
- Uses object-oriented programming principles
- Data persistence through JSON file storage
- No external dependencies required

## Future Enhancements

- Implement a graphical user interface (GUI)
- Add user authentication for librarians
- Generate reports on library usage and popular books
- Integrate with an external database for improved scalability

This project serves as a practical example of a Python-based management system and can be used as a starting point for more complex library management solutions.
