from recipes.models import (
    Recipe,
    Ingredient
)
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'amount', 'recipe', 'measurement')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'steps', 'servings', 'ingredients')
