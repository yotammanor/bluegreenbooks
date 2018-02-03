from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    has_leather_binding = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.name}, "
                f"{'in leather' if self.has_leather_binding else 'regular'}")
