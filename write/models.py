from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.SlugField(max_length=200,allow_unicode=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meaning = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.word
