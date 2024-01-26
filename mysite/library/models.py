from django.db import models

class Book (models.Model):
    book_title = models.CharField("Book Title", max_length=200)
    author_lastname = models.CharField("Author Last Name", max_length=200)
    author_firstname = models.CharField("Author First Name", max_length=200)
    cover_img = models.ImageField("Cover Image", upload_to='')
    genre = models.CharField("Genre", max_length=200)
    description = models.TextField("Description")
    pub_date = models.DateField("Publication Date")
    isbn = models.BigIntegerField("ISBN")
    shelf_loc = models.SmallIntegerField("Shelf Location")
    num_available = models.SmallIntegerField("Number Available")

    def __str__(self):
        return self.book_title



    # id = Column(Integer, primary_key=True)
    # title = Column(String, nullable=False)
    # author = Column(String, nullable=False)
    # cover_image = Column(String, nullable=False)
    # genre = Column(String, nullable=False)
    # description = Column(String, nullable=False)
    # # publication_date = Column(Date, nullable=False)
    # isbn = Column(Integer, nullable=False)
    # shelf_location = Column(Integer, nullable=False)
    # num_available = Column(Integer, nullable=False)

    # def __repr__(self):
    #     return f'<Book Title {self.title}'
