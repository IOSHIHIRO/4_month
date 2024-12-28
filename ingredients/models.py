from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CHOICES = (
        ('g', 'граммы'),
        ('kg', 'килограммы'),
        ('ml', 'миллилитры'),
        ('l', 'литры'),
        ('шт', 'штуки'),
    )
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=10)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='шт')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f'{self.name}-{self.unit}'
