from rest_framework import serializers
from .models import Movies, Series, ReviewsMovies, ReviewsSeries
from django.contrib.auth.models import User

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'

class ReviewsMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsMovies
        fields = '__all__'

class ReviewsSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsSeries
        fields = '__all__'



