from django.db import models
# from books.models import Book
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.TextField()

    def __str__(self):
        return self.last_name + ", " + self.first_name

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + " " + self.last_name
        super(Author, self).save(*args, **kwargs)

    # def authored_books(self):
    #     books = Book.objects.filter()