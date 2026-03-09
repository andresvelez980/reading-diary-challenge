from datetime import datetime
from typing import List, Optional

class note:
    def __init__(self, text: str, page: int, date: datetime) -> None:
        self.text = text
        self.page = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"
