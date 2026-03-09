from datetime import datetime
from typing import List, Optional

class Note:
    def __init__(self, text: str, page: int, date: datetime) -> None:
        self.text = text
        self.page = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"
class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED
        self.notes = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:

        if page > self.pages:
            return False

        note = Note(text, page, date)
        self.notes.append(note)

        return True