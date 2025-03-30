from rest_framework import routers
from django.urls import path
from .views import ApiMoviesViewSet, ApiSeriesViewSet, UserAccountsViewSet, UserProfilesViewSet, FavoritesViewSet, WatchingViewSet, PlansUpdaterViewSet, MoviesViewSet, SeriesViewSet

router = routers.DefaultRouter() # Router vai criar rotas padrões para Viewsets, criando rota de objeto, rota de delete, rota de update, rota de get, rota de list tudo de maneira padrão

router.register(r'apimovies',ApiMoviesViewSet, basename='apimovies')
router.register(r'apiseries', ApiSeriesViewSet, basename='apiseries')
router.register(r'users', UserAccountsViewSet, basename='users')
router.register(r'profiles', UserProfilesViewSet, basename='profiles')
router.register(r'favorite', FavoritesViewSet, basename='favorite')
router.register(r'watching', WatchingViewSet, basename='watching')
router.register(r'plansupdater', PlansUpdaterViewSet, basename='plansupdater')
router.register(r'movies', MoviesViewSet, basename='movies')
router.register(r'series', SeriesViewSet, basename='series')

urlpatterns = router.urls
