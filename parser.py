from bs4 import BeautifulSoup
import requests
from src.database.models import *
from src.database.books import books

BASE_URL: str = 'https://bible.by/'


def remove_digits(text: str) -> str:
    for digit in '0123456789':
        text = text.replace(digit, '')

    return text.strip(' ')

def parse_chapter(book_num: int, chapter_id: int, translation_id: str = 'syn') -> None:
    if Translation.get_or_none(short_name=translation_id) is None:
        Translation.create(short_name=translation_id)

    parser = BeautifulSoup(
        markup=requests.get(
            url=f'{BASE_URL}{translation_id}/{book_num}/{chapter_id}'
        ).text,
        features='html.parser'
    )

    verse_list = parser.find('div', class_='text en').find_all('div')
    for verse in verse_list:
        if 'id' in verse.attrs:
            if not verse.attrs['id'].isdigit():
                continue

            verse_num: int = int(verse.attrs['id'])
            verse_text: str = remove_digits(str(verse.text))

            Verse.get_or_create(
                chapter=Chapter.get(
                    Chapter.book == Book.get(Book.book_number == book_num),
                    Chapter.chapter_number == chapter_id
                ),
                verse_number=verse_num,
                text=verse_text
            )


def fill_bd() -> None:
    for book in books:
        new_book = Book.get_or_create(book_number=book, name=books[book][0])[0]

        for chapter in range(1, books[book][1]+1):
            Chapter.get_or_create(chapter_number=chapter, book=new_book)


if __name__ == '__main__':
    fill_bd()
    for book in books:
        for chapter in range(1, books[book][1]+1):
            parse_chapter(book, chapter, translation_id='nasb')