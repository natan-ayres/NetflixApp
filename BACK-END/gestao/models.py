from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator

class Movies(models.Model):
    CLASSIFICACOES_CHOICES = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('NC-17', 'NC-17'),
    ]

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    sinopse = models.TextField(max_length=200)
    poster_url = models.CharField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=CLASSIFICACOES_CHOICES)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    runtime = models.IntegerField()
    stars = models.FloatField(default=0)
    user_reviews = models.ManyToManyField(User, through='ReviewsMovies')

    def get_avg_stars(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            avg_stars = reviews.aggregate(Avg('rating'))['stars__avg']
            self.stars = avg_stars
        else:
            self.stars = None

    def __str__(self):
        return '{self.name}({launch_date})'
    
class Series(models.Model):
    CLASSIFICACOES_CHOICES = [
    ('TV-Y', 'TV-Y'),
    ('TV-Y7', 'TV-Y7'),
    ('TV-Y7-FV', 'TV-Y7-FV'),
    ('TV-G', 'TV-G'),
    ('TV-PG', 'TV-PG'),
    ('TV-14', 'TV-14'),
    ('TV-MA', 'TV-MA'),
] 
    
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100, blank=True, null=True)
    writer = models.TextField(max_length=200, blank=True, null=True)
    actors = models.TextField(max_length=200, blank=True, null=True)
    sinopse = models.TextField(max_length=200)
    rated = models.CharField(blank=True, null=True, max_length=20, choices=CLASSIFICACOES_CHOICES)
    poster_url = models.CharField(max_length=200)
    launch_date = models.CharField(blank=True, null=True, max_length=20)
    episodes = models.IntegerField()
    seasons = models.IntegerField(blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    user_reviews = models.ManyToManyField(User, through='ReviewsSeries')


    def get_avg_stars(self):
        reviews = self.reviews.all() 
        if reviews.exists():
            avg_stars = reviews.aggregate(Avg('rating'))['stars__avg']
            self.stars = avg_stars
        else:
            self.stars = None

    def __str__(self):
        return '{self.name}({launch_date})'

class ReviewsMovies(models.Model):
    class Meta:
        verbose_name = 'Review - Movie'
        verbose_name_plural = 'Reviews - Movies'

    movie = models.ForeignKey(Movies, related_name='reviews', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    rating = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    show = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsMovies, self).save(*args, **kwargs)
        self.movie.get_avg_rating()
        self.movie.save()

    def __str__(self):
        return f"{self.movie.name} Review - {self.rating}"
    
class ReviewsSeries(models.Model):
    class Meta:
        verbose_name = 'Review - Series'
        verbose_name_plural = 'Reviews - Series'

    series = models.ForeignKey(Series, related_name='reviews', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    review = models.TextField(max_length=250)
    rating = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    show = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def save(self, *args, **kwargs):
        super(ReviewsSeries, self).save(*args, **kwargs)
        self.series.get_avg_stars()
        self.series.save()

    def __str__(self):
        return f"{self.series.name} Review - {self.rating}"