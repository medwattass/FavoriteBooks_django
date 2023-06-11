from django.db import models
from log_reg_app.models import User


class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if Book.objects.filter(title=postData['title']).exists():
            errors["title"] = "This title have been already used"
        if len(postData['title']) < 5:
            errors["title_2"] = "The title should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "The descriptions should be at least 10 characters"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books", on_delete = models.CASCADE)
    books = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()