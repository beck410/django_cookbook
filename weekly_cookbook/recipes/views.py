from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from recipes.models import (
    Recipe,
    Ingredient
)
from recipes.serializers import(
    RecipeSerializer,
    IngredientSerializer
)


class RecipeList(APIView):

    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):
    """
    API endpoint that returns single recipe
    """

    def _get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        recipe = self._get_object(pk)
        # ingredients = Ingredient.objects.filter(recipe=recipe)

        recipe_serializer = RecipeSerializer(recipe, context={'request': request})

        # ingredients_serializer = IngredientSerializer(ingredients, many=True)
        return Response({
            'recipe_details': recipe_serializer.data
        })

    def delete(self, request, pk, format=None):
        recipe = self._get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientList(APIView):
    def _get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetail(APIView):
    """
    API endpoint that returns single recipe
    """

    def _get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        ingredient = self._get_object(pk)
        ingredient_serializer = IngredientSerializer(ingredient, context={'request': request})
        return Response(ingredient_serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        ingredient = self._get_object(pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
