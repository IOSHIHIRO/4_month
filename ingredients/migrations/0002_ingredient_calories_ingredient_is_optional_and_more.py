# Generated by Django 5.1.3 on 2024-12-28 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_optional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='название ингредиента'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('граммы', 'граммы'), ('килограммы', 'килограммы'), ('миллилитры', 'миллилитры'), ('литры', 'литры'), ('штуки', 'штуки')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=100, verbose_name='описание рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.TextField(verbose_name='название рецепта'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipes', models.ManyToManyField(related_name='collections', to='ingredients.recipe')),
            ],
        ),
    ]