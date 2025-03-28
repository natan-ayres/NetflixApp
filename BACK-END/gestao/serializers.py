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
        fields = ['name']

class UserAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserAccounts(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance







