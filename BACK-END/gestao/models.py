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
    sinopse = models.TextField(max_length=200)
    poster_url = models.CharField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=RATINGS)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    runtime = models.IntegerField()
    likeability = models.JSONField(default=dict, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.likeability:
            self.likeability = {'unlike': [], 'like': [], 'verylike': []}  
        super().save(*args, **kwargs)
    
    def addunlike(self, profile):
        if profile not in self.likeability['unlike']:
            self.likeability['unlike'].append(profile)
            self.save()

    def addlike(self, profile):
        if profile not in self.likeability['like']:
            self.likeability['like'].append(profile)
            self.save()
    
    def addverylike(self, profile):
        if profile not in self.likeability['verylike']:
            self.likeability['verylike'].append(profile)
            self.save()

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
    sinopse = models.TextField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=RATINGS)
    poster_url = models.CharField(max_length=200)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    episodes = models.IntegerField()
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
    favorites = models.ManyToManyField(Movies, related_name='favorites', blank=True)
    favorites_series = models.ManyToManyField(Series, related_name='favorites_series', blank=True)
    watchlist = models.ManyToManyField(Movies, related_name='watchlist', blank=True)
    watchlist_series = models.ManyToManyField(Series, related_name='watchlist_series', blank=True)
    likeability = models.JSONField(default=dict, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.likeability:
            self.likeability = {
                'movies': {'unlike': [], 'like': [], 'verylike': []},
                'series': {'unlike': [], 'like': [], 'verylike': []}
                }  
        super().save(*args, **kwargs)
    
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
    
    def __str__(self):
        return self.username


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
     
    def __str__(self):
        return '{self.username} - {self.plans}'