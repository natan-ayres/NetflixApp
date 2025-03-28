from rest_framework import routers
from django.urls import path
from .views import ApiMoviesViewSet, ApiSeriesViewSet, UserAccountsViewSet, UserProfilesViewSet

urlpatterns = [
    path('movie/', ApiMoviesViewSet.as_view({'post': 'create'}), name='apimovie-create'),
    path('series/', ApiSeriesViewSet.as_view({'post': 'create'}), name='apiseries-create'),
    path('user/', UserAccountsViewSet.as_view({'post': 'create', 'get': 'list'}), name='useraccounts-create-update-delete'),
    path('profile/', UserProfilesViewSet.as_view({'post': 'create', 'get': 'list'}), name='userprofiles-create-update-delete'),

]
