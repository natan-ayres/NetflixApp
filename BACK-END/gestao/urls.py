from rest_framework import routers
from django.urls import path
from .views import ApiMoviesViewSet, ApiSeriesViewSet

urlpatterns = [
    path('movie/', ApiMoviesViewSet.as_view({'post': 'create'}), name='apimovie-create'),
    path('series/', ApiSeriesViewSet.as_view({'post': 'create'}), name='apiseries-create'),
]
