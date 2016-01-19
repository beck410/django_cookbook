from django.conf.urls import url, patterns
from recipes.views import (
    RecipeList,
    RecipeDetail,
    IngredientList,
    IngredientDetail
)

urlpatterns = patterns('',
    url(r'^/recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^/recipes/(?P<pk>\d+)/$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^/ingredients/$', IngredientList.as_view(), name='ingredient-list'),
    url(r'^/ingredients/(?P<pk>\d+)/$', IngredientDetail.as_view(), name='ingredient-detail'),
)
