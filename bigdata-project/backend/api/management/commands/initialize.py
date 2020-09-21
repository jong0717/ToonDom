from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from api import models


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent.parent / "data"
    DATA_FILE = str(DATA_DIR / "dump.pkl")

    def _load_dataframes(self):
        try:
            data = pd.read_pickle(Command.DATA_FILE)
        except:
            print(f"[-] Reading {Command.DATA_FILE} failed")
            exit(1)
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        dataframes = self._load_dataframes()

        print("[*] Initializing stores...")

        # Genre Initialize
        models.Genre.objects.all().delete()
        genres = dataframes["genre"]
        for genre in genres.itertuples():
            genre = models.Genre.objects.create(name=genre.name)
 

        # Artist Initialize
        models.Artist.objects.all().delete()
        artists = dataframes["artist"]
        artists_bulk = [
            models.Artist(
                name = artist.name,
            )
            for artist in artists.itertuples()
        ]
        models.Artist.objects.bulk_create(artists_bulk)


        # Webtoon Initialize
        models.Webtoon.objects.all().delete()
        webtoons = dataframes["webtoon"]
        webtoons_bulk = [
            models.Webtoon(
                origin_id = webtoon.origin_id,
                title = webtoon.title,
                description = webtoon.description,
                genres = webtoon.genres,
                artists = webtoon.artists,
                rating = webtoon.rating,
                link = webtoon.link,
                thumb_img = webtoon.thumb_img,
                distinct = webtoon.distinct,

            )
            for webtoon in webtoons.itertuples()
        ]
        models.Webtoon.objects.bulk_create(webtoons_bulk)

        # Genre_Webtoon Initialize
        models.Genre_Webtoon.objects.all().delete()
        webtoons = dataframes["webtoon"]
        for webtoon in webtoons.itertuples():
            for gen in webtoon.genres:
                genre = models.Genre_Webtoon.objects.create(
                    webtoon_id = webtoon.Index + 1,
                    genre_id = gen
                )


        # Artist_Webtoon Initialize
        models.Artist_Webtoon.objects.all().delete()
        webtoons = dataframes["webtoon"]
        for webtoon in webtoons.itertuples():
            for gen in webtoon.artists:
                genre = models.Artist_Webtoon.objects.create(
                    webtoon_id = webtoon.Index + 1,
                    artist_id = gen
                )
        
        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()
