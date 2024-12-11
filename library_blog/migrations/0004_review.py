# Generated by Django 5.1.3 on 2024-12-11 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0003_alter_library_model_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('text_review', models.TextField(verbose_name='Напишите отзыв')),
                ('start', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=100, verbose_name='Выберите отзыв')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library_blog.library_model')),
            ],
        ),
    ]
