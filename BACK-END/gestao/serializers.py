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
        fields = ['name', 'image']

    def create(self, validated_data):
        request = self.context.get('request') 
        user = request.user
        validated_data['account'] = user.id
        if validated_data.get('image') is None:
            validated_data['image'] = 'profile_pics/default.jpg'
        profile = UserProfiles(**validated_data)
        profile.save() 
        user.addprofile(profile) 
        return profile
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if instance.account != user:
            raise serializers.ValidationError('You do not have permission to update this profile')
        instance = super().update(instance, validated_data)
        return instance
    
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ['add','type', 'movieorseries_id']

    add = serializers.BooleanField(write_only=True)
    type = serializers.CharField(write_only=True)
    movieorseries_id = serializers.IntegerField(write_only=True)

    def save(self, **kwargs):
        movieorseries_id = self.validated_data['movieorseries_id']
        instance = self.instance
        if self.validated_data['add'] == True:
            if self.validated_data['type'] == 'movie':
                instance.addfavoritemovie(movieorseries_id)
            elif self.validated_data['type'] == 'series':
                instance.addfavoriteserie(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
        elif self.validated_data['add'] == False:
            if self.validated_data['type'] == 'movie':
                instance.unfavoritemovie(movieorseries_id)
            elif self.validated_data['type'] == 'series':
                instance.unfavoriteserie(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
        else:
            raise serializers.ValidationError('Invalid add value')
        return instance
    
class WatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ['add','type', 'movieorseries_id']
    add = serializers.BooleanField(write_only=True)
    type = serializers.CharField(write_only=True)
    movieorseries_id = serializers.IntegerField(write_only=True)

    def save(self, **kwargs):
        movieorseries_id = self.validated_data['movieorseries_id']
        instance = self.instance
        if self.validated_data['add'] == True:
            if self.validated_data['type'] == 'movie':
                instance.addwatchingmovie(movieorseries_id)
            elif self.validated_data['type'] == 'series':
                instance.addwatchingserie(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
            return instance
        elif self.validated_data['add'] == False:
            if self.validated_data['type'] == 'movie':
                instance.unaddwatchingmovie(movieorseries_id)
            elif self.validated_data['type'] == 'series':
                instance.unaddwatchingserie(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
            return instance
        else:
            raise serializers.ValidationError('Invalid add value')
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ['add','type', 'movieorseries_id']
    add = serializers.BooleanField(write_only=True)
    type = serializers.CharField(write_only=True)
    movieorseries_id = serializers.IntegerField(write_only=True)

    def save(self, **kwargs):
        movieorseries_id = self.validated_data['movieorseries_id']
        instance = self.instance
        if self.validated_data['add'] == True:
            if self.validated_data['type'] == 'like':
                instance.addlikemovie(movieorseries_id)
            elif self.validated_data['type'] == 'unlike':
                instance.addunlikeserie(movieorseries_id)
            elif self.validated_data['type'] == 'verylike':
                instance.addverylikemovie(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
        elif self.validated_data['add'] == False:
            if self.validated_data['type'] == 'like':
                instance.unaddunlikemovie(movieorseries_id)
            elif self.validated_data['type'] == 'unlike':
                instance.unaddunlike(movieorseries_id)
            elif self.validated_data['type'] == 'verylike':
                instance.unaddveryunlike(movieorseries_id)
            else:
                raise serializers.ValidationError('Invalid type')
        else:
            raise serializers.ValidationError('Invalid add value')


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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['profiles'] = [{'id': profile.id, 'name': profile.name} for profile in instance.profiles.all()]
        representation['plans'] = instance.plans
        representation.pop('password', None)
        return representation

    
    








