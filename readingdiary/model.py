from datetime import datetime
from typing import List, Optional

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self) -> str:
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
        self.rating: int = Book.UNRATED
        self.notes: List[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        self.notes.append(Note(text, page, date))
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in [Book.EXCELLENT, Book.GOOD, Book.BAD]:
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> List[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        page_count = {}
        for note in self.notes:
            page_count[note.page] = page_count.get(note.page, 0) + 1

        return max(page_count, key=page_count.get)

    def __str__(self) -> str:
        rating_str = {
            Book.EXCELLENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated"
        }[self.rating]

        return (
            f"ISBN: {self.isbn}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Rating: {rating_str}"
        )


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False
        self.books[isbn] = Book(isbn, title, author, pages)
        return True

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            return False
        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Optional[Book]:
        max_notes = -1
        best_book = None
        for book in self.books.values():
            note_count = len(book.notes)
            if note_count > max_notes:
                max_notes = note_count
                best_book = book
        return best_book if max_notes > 0 else None


