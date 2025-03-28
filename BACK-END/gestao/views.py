from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movies, Series, UserProfiles, UserAccounts
from .serializers import ApiMoviesSerializer, ApiSeriesSerializer, UserProfilesSerializer, UserAccountsSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from netflix.local_settings import API_KEY


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
        return UserProfiles.objects.filter(account__in=user.id)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        obj = UserProfiles(
            name = data.get('name'),
            account = user.id,
            image = 'profile_pics/NatanAyres2_kNKp7hO.jpg'
        )
        obj.save()
        serializer = self.get_serializer(data=data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserAccountsViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = UserAccountsSerializer
    def get_queryset(self):
        try:
            user = self.request.user
            return UserAccounts.objects.filter(id=user.id)
        except:
            return "No Info about User"

