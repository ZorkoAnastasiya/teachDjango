from django.db import models


class Numbers(models.Model):
    objects = models.Manager()

    name = models.TextField(unique = True)
    number = models.BigIntegerField(default = 0)

    def __repr__(self):
        return f"{self.__class__.__name__}(id = {self.id}, name = {self.name}, number = {self.number})"
