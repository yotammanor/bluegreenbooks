from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "green_book"

    def __str__(self):
        return f"{self.name}"
