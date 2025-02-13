from peewee import *

db = SqliteDatabase('nasb.db')


class BaseModel(Model):
    class Meta:
        database = db


class Translation(BaseModel):
    short_name = CharField(unique=True)  # Название перевода
    full_name = CharField(unique=False, null=True)

class Book(BaseModel):
    book_number = IntegerField(unique=True)  # Номер книги
    name = CharField()


class Chapter(BaseModel):
    book = ForeignKeyField(Book, backref='chapters')
    chapter_number = IntegerField()

    class Meta:
        indexes = (
            (('book', 'chapter_number'), True),
        )


class Verse(BaseModel):
    chapter = ForeignKeyField(Chapter, backref='verses')
    verse_number = IntegerField()
    text = TextField()

    class Meta:
        indexes = (
            (('chapter', 'verse_number'), True),
        )


def initialize_db():
    with db:
        db.create_tables([Translation, Book, Chapter, Verse])


initialize_db()
print("База данных создана и готова к использованию.")

