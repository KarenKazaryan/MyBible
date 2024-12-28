import peewee

database = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Book(BaseModel):
    name = peewee.CharField(unique=True)
    author = peewee.CharField()
    year_writing = peewee.DateField()
    description = peewee.TextField()


class Chapter(BaseModel):
    id_book = peewee.ForeignKeyField(Book, backref='book')


class Poew(BaseModel):
    id_chapter = peewee.ForeignKeyField(Chapter, backref='chapter')
    id_book = peewee.ForeignKeyField(Book, backref='books')

database.create_tables([
    Book,
    Chapter,
    Poew
])
