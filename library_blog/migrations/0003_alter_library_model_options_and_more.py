# Generated by Django 5.1.3 on 2024-12-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0002_library_model_advertising'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library_model',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='library_model',
            name='time_watch',
        ),
        migrations.AddField(
            model_name='library_model',
            name='email_director',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Укажите почту автора'),
        ),
    ]
