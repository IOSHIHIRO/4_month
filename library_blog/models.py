from django.db import models

class library_model(models.Model):
    GENRE = (
            ('Фэнтези','Фэнтези'),
            ('Романтика','Романтика'),
            ('Приключения','Приключения'),
            ('Комедия','Комедия'),
            ('Гарем','Гарем')
    )
    image = models.ImageField(upload_to = 'library/', verbose_name='Загрузите фото фильма')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Укажите цену книги', default=100)
    data = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE)
    email_director = models.EmailField(max_length=100,verbose_name='Укажите почту автора', blank=True, null=True)
    director = models.CharField(max_length=100, verbose_name='Укажите автора книги')
    advertising = models.URLField(verbose_name='Укажите ссылку на рекламу', null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title