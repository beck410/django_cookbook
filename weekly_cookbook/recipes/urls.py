from django.conf.urls import url, patterns
from recipes.views import (
    RecipeList,
    RecipeDetail,
    IngredientList
)

urlpatterns = patterns('',
    url(r'^/recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^/recipes/(?P<pk>[0-9])$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^/ingredients/$', IngredientList.as_view(), name='ingredient-list'),
)
