from django.db import models
from books_tags.models import Book

class BasketModel(models.Model):
    CHECKING = (
        ('✅','✅'),
        ('❌','❌'),
    )
    name = models.CharField(max_length=100, verbose_name='Укажите ваше Имя')
    email = models.EmailField(max_length=100,verbose_name='Укажите почту')
    phone_number = models.FloatField(verbose_name='Укажите номер телефона', default='+996')
    book = models.URLField(verbose_name='Укажите ссылку на книгу')
    library = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    choice_check = models.CharField(max_length=10, choices=CHECKING, null=True)

    def __str__(self):
        return self.name

