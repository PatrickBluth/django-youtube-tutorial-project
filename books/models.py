from django.db import models
from django.urls import reverse


class Genre(models.Model):
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def title_to_url(self):
        return self.title.replace(' ', '-')

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={
            'genre': self.genre,
            'book_url': self.title_to_url()
        })
