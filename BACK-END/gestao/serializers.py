from rest_framework import serializers
from .models import Movies, Series, UserProfiles, UserAccounts

class ApiMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title']

class ApiSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['title']

class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'

class UserAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ['username', 'email', 'password', 'password2']







