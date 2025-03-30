from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movies, Series, UserProfiles, UserAccounts
from .serializers import ApiMoviesSerializer, ApiSeriesSerializer, UserProfilesSerializer, UserAccountsSerializer, FavoritesSerializer, WatchingSerializer, LikeSerializer, PlansUpdaterSerializer, MoviesSerializer, SeriesSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.decorators import action
from netflix.local_settings import API_KEY

class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    def get_queryset(self):
        return Movies.objects.all()
    
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
   

class SeriesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    def get_queryset(self):
        return Series.objects.all()
    
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ApiMoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = ApiMoviesSerializer

    def create(self, request, *args, **kwargs):
        names = request.data.get('title', [])
        movies_created = []
        for name in names:
            response = requests.get(f'https://www.omdbapi.com/?t={name}&type=movie&apikey={API_KEY}')
            print(response)
            if response.status_code == 200:
                api_data = response.json()
                if api_data.get('Title') is None:
                    continue
                else:
                    obj = Movies(
                        title = api_data.get('Title'),
                        director = api_data.get('Director'),
                        genre = api_data.get('Genre'),
                        writer = api_data.get('Writer'),
                        actors = api_data.get('Actors'),
                        plot = api_data.get('Plot'),
                        rated = api_data.get('Rated'),
                        poster_url = api_data.get('Poster'),
                        launch_date = api_data.get('Released'),
                        runtime = api_data.get('Runtime'),
                    )
                    obj.save()
                    movies_created.append(obj)

        # Serializa os objetos criados
        serializer = self.get_serializer(movies_created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ApiSeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = ApiSeriesSerializer

    def create(self, request, *args, **kwargs):
        names = request.data.get('title', [])
        movies_created = []
        for name in names:
            response = requests.get(f'https://www.omdbapi.com/?t={name}&type=series&apikey={API_KEY}')
            print(response)
            if response.status_code == 200:
                api_data = response.json()
                if api_data.get('Title') is None:
                    continue
                else:
                    if api_data.get('totalSeasons') == 'N/A':
                        seasons = 0
                    else:
                        seasons = api_data.get('totalSeasons')
                    obj = Series(
                        title = api_data.get('Title'),
                        director = api_data.get('Director'),
                        genre = api_data.get('Genre'),
                        writer = api_data.get('Writer'),
                        actors = api_data.get('Actors'),
                        plot = api_data.get('Plot'),
                        rated = api_data.get('Rated'),
                        poster_url = api_data.get('Poster'),
                        launch_date = api_data.get('Released'),
                        seasons = seasons
                    )
                    obj.save()
                    movies_created.append(obj)

        # Serializa os objetos criados
        serializer = self.get_serializer(movies_created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserProfilesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfilesSerializer
    def get_queryset(self):
        user = self.request.user
        return UserProfiles.objects.filter(account=user.id)
    
class PlansUpdaterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlansUpdaterSerializer
    def get_queryset(self):
        try:
            user = self.request.user
            return UserAccounts.objects.filter(id=user.id)
        except:
            return "No Info about User"
    
class UserAccountsViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = UserAccountsSerializer
    def get_queryset(self):
        try:
            user = self.request.user
            return UserAccounts.objects.filter(id=user.id)
        except:
            return "No Info about User"

class FavoritesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoritesSerializer
    def get_queryset(self):
        user = self.request.user
        return UserProfiles.objects.filter(account=user.id)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class LikeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    def get_queryset(self):
        user = self.request.user
        return UserProfiles.objects.filter(account=user.id)
    
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class WatchingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = WatchingSerializer
    def get_queryset(self):
        user = self.request.user
        return UserProfiles.objects.filter(account=user.id)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
