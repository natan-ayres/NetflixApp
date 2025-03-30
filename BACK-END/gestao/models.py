from django.db import models
from django.contrib.auth.models import AbstractUser

class Movies(models.Model):
    class Meta:
        verbose_name = 'Movie'
    RATINGS = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('NC-17', 'NC-17'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    plot = models.TextField(max_length=200)
    poster_url = models.CharField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=RATINGS)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    runtime = models.CharField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.likeability:
            self.likeability = {'unlike': [], 'like': [], 'verylike': []}  
        super().save(*args, **kwargs)

    def __str__(self):
        return '{self.title}({launch_date})'
    
class Series(models.Model):
    class Meta:
        verbose_name_plural = 'Series'
    RATINGS = [
    ('TV-Y', 'TV-Y'),
    ('TV-Y7', 'TV-Y7'),
    ('TV-Y7-FV', 'TV-Y7-FV'),
    ('TV-G', 'TV-G'),
    ('TV-PG', 'TV-PG'),
    ('TV-14', 'TV-14'),
    ('TV-MA', 'TV-MA'),
] 
    
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    plot = models.TextField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=RATINGS)
    poster_url = models.CharField(max_length=200)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    seasons = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{self.title}({launch_date})'
    

class UserProfiles(models.Model):
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    account = models.IntegerField(default=0)
    favorites = models.JSONField(default=dict, blank=True, null=True)
    watching = models.JSONField(default=dict, blank=True, null=True)
    likeability = models.JSONField(default=dict, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.likeability:
            self.likeability = {
                'movies': {'unlike': [], 'like': [], 'verylike': []},
                'series': {'unlike': [], 'like': [], 'verylike': []}
                }  
        if not self.favorites:
            self.favorites = {
                'movies': [],
                'series': []
                }
        if not self.watching:
            self.watching = {
                'movies': [],
                'series': []
                }
        super().save(*args, **kwargs)

    def addwatchingmovie(self, movie):
        if movie not in self.watching['movies']:
            self.watching['movies'].append(movie)
            self.save()
    
    def addwatchingseries(self, series):
        if series not in self.watching['series']:
            self.watching['series'].append(series)
            self.save()

    def unaddwatchingmovie(self, movie):
        if movie in self.watching['movies']:
            self.watching['movies'].remove(movie)
            self.save()
    
    def unaddwatchingseries(self, series):
        if series in self.watching['series']:
            self.watching['series'].remove(series)
            self.save()

    def addfavoritemovie(self, movie):
        if movie not in self.favorites['movies']:
            self.favorites['movies'].append(movie)
            self.save()
    
    def addfavoriteserie(self, series):
        if series not in self.favorites['series']:
            self.favorites['series'].append(series)
            self.save()
    
    def unaddfavoritemovie(self, movie):
        if movie in self.favorites['movies']:
            self.favorites['movies'].remove(movie)
            self.save()

    def unaddfavoriteserie(self, series):
        if series in self.favorites['series']:
            self.favorites['series'].remove(series)
            self.save()
    
    def addunlikemovie(self, movie):
        if movie not in self.likeability['movies']['unlike']:
            self.likeability['movies']['unlike'].append(movie)
            self.save()

    def addlikemovie(self, movie):
        if movie not in self.likeability['movies']['like']:
            self.likeability['movies']['like'].append(movie)
            self.save()
    
    def addverylikemovie(self, movie):
        if movie not in self.likeability['movies']['verylike']:
            self.likeability['movies']['verylike'].append(movie)
            self.save()

    def addunlikeserie(self, series):
        if series not in self.likeability['series']['unlike']:
            self.likeability['series']['unlike'].append(series)
            self.save()

    def addlikeserie(self, series):
        if series not in self.likeability['series']['like']:
            self.likeability['series']['like'].append(series)
            self.save()
    
    def addverylikeserie(self, series):
        if series not in self.likeability['series']['verylike']:
            self.likeability['series']['verylike'].append(series)
            self.save()

    def unaddunlikemovie(self, movie):
        if movie in self.likeability['movies']['unlike']:
            self.likeability['movies']['unlike'].remove(movie)
            self.save()

    def unaddlikemovie(self, movie):
        if movie in self.likeability['movies']['like']:
            self.likeability['movies']['like'].remove(movie)
            self.save()

    def unaddverylikemovie(self, movie):
        if movie in self.likeability['movies']['verylike']:
            self.likeability['movies']['verylike'].remove(movie)
            self.save()

    def unaddunlikeserie(self, series):
        if series in self.likeability['series']['unlike']:
            self.likeability['series']['unlike'].remove(series)
            self.save()

    def unaddlikeserie(self, series):
        if series in self.likeability['series']['like']:
            self.likeability['series']['like'].remove(series)
            self.save()

    def unaddverylikeserie(self, series):
        if series in self.likeability['series']['verylike']:
            self.likeability['series']['verylike'].remove(series)
            self.save()
    
    def __str__(self):
        return self.name


class UserAccounts(AbstractUser):
    class Meta:
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts'
    PLANS = [
    ('BASIC', 'BASIC'),
    ('STANDARD', 'STANDARD'),
    ('PREMIUM', 'PREMIUM'),
    ]
    plans = models.CharField(blank=True, null=True, max_length=20, choices=PLANS, default='BASIC')
    profiles = models.ManyToManyField(UserProfiles, related_name='profiles', blank=True)

    def addprofile(self, profile):
        if profile not in self.profiles.all():
            self.profiles.add(profile)
            self.save()

    def __str__(self):
        return f'{self.username} - {self.plans}'
