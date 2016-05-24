from django.db import models
from django.utils.timezone import now

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField("Author", related_name="books")
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favourite = models.BooleanField(default=False, verbose_name="Favorite?")

    def __str__(self):
        return "{} by {}".format(self.title, self.list_authors())

    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all()])

    def save(self, *args, **kwargs):
        if (self.review and self.date_reviewed is None):
            self.date_reviewed = now()

class Author(models.Model):
    name = models.CharField(max_length=70, help_text="Use pen name, not real name", unique=True)

    def __str__(self):
        return self.name
