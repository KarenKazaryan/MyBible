import peewee

database = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = database

class ModuleBible(BaseModel):
    full_name = peewee.TextField()
    short_name = peewee.CharField()


class Book(BaseModel):
    id_module = peewee.ForeignKeyField(ModuleBible, backref='module')
    name = peewee.CharField(unique=True)
    author = peewee.CharField()
    year_writing = peewee.DateField()
    description = peewee.TextField()


class Chapter(BaseModel):
    id_book = peewee.ForeignKeyField(Book, backref='book')


class Poew(BaseModel):
    id_chapter = peewee.ForeignKeyField(Chapter, backref='chapter')
    id_book = peewee.ForeignKeyField(Book, backref='books')
    text = peewee.TextField()


database.create_tables([
    ModuleBible,
    Book,
    Chapter,
    Poew
])
