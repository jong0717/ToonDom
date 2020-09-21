from django.utils import timezone
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator 


class Genre(models.Model):
    name = models.CharField(max_length=20)

class Artist(models.Model):
    name = models.CharField(max_length=20)


class Webtoon(models.Model):
    id = models.AutoField(primary_key=True) # 고유 번호
    origin_id = models.IntegerField(null=False) # 웹툰 번호(각 플랫폼마다 형식 다름)
    title = models.CharField(max_length=20)
    description = models.TextField()
    genres = models.CharField(max_length=50) 
    artists = models.CharField(max_length=50) 
    rating = models.FloatField(max_length=15, null=True) 
    link = models.TextField() # 해당 웹툰 링크
    thumb_img = models.TextField() 
    distinct = models.IntegerField(null=False) 
    genres_rels = models.ManyToManyField(Genre, through='Genre_Webtoon', through_fields=('webtoon', 'genre'))
    artists_rels = models.ManyToManyField(Artist, through='Artist_Webtoon', through_fields=('webtoon', 'artist'))
    wishes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Wish', related_name="wish_users", through_fields=('webtoon', 'user'))
    stars = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Star', related_name="star_users", through_fields=('webtoon', 'user'))


class Genre_Webtoon(models.Model):
    id = models.AutoField(primary_key=True) # 고유 번호
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, null=False)


class Artist_Webtoon(models.Model):
    id = models.AutoField(primary_key=True) # 고유 번호
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, null=False)


class Star(models.Model):
    id = models.AutoField(primary_key=True) # 고유 번호
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
     )
    content = models.TextField()


class Ranking(models.Model):
    origin_id = models.IntegerField(null=True) 
    distinct = models.IntegerField(null=True) 
    rank = models.IntegerField(null=True) 


class Wish(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, null=False)
