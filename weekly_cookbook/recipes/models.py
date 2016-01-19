from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    steps = models.CharField(max_length=200)
    servings = models.PositiveIntegerField()


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    measurement = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', null=True)

    def __unicode__(self):
        return '%d %s %s' % (self.amount, self.measurement, self.name)
