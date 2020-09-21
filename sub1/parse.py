import json
import pandas as pd
import os
import shutil

DATA_DIR = "../data"
DATA_FILE = os.path.join(DATA_DIR, "all_webtoon.json")
DUMP_FILE = os.path.join(DATA_DIR, "dump.pkl")


webtoon_columns = (
    "origin_id",  # 웹툰 고유번호
    "title",  # 웹툰 제목
    "description",  # 웹툰 설명
    "genres",  # 웹툰 장르
    "artists",  # 작가
    "rating",  # 평점
    "link",  # 웹툰 주소
    "thumb_img",  # 썸네일 이미지 주소
    "distinct", # 플랫폼 번호( 1: 네이버, 2: 카카오, 3: 다음)
)

genre_columns = (
    "pk", # 고유번호
    "name", # 장르 이름
)

artist_columns = (
    "pk", # 고유번호
    "name", # 작가 이름
)

def import_data(data_path=DATA_FILE):
    try:
        with open(data_path, encoding="utf-8-sig") as f:
            data = json.loads(f.read())
    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)

    webtoon = []  # 웹툰 테이블
    genre = [] # 장르
    artist = [] # 작가


    # 번호 넣어주려고
    gen_cnt = 1
    art_cnt = 1

    for d in data:
        # 평점 소수점 줄이기
        rating = d["rating"]
        if type(rating) == int:
            rating = float(rating)
        rating = round(rating,3)

        # 장르바꿔치기
        for gen in range(len(d["genres"])):
            if d["genres"][gen] == "액션무협":
                d["genres"].append("액션")
                d["genres"].append("무협")
                d["genres"].remove("액션무협")
            if d["genres"][gen] == "코믹":
                d["genres"][gen] = "개그"
            if d["genres"][gen] == "순정":
                d["genres"][gen] = "로맨스"


        # 장르 테이블
        for gen in range(len(d["genres"])) :
            for gen2 in genre:
                if d["genres"][gen] == gen2[1]:
                    break
            else:
                genre.append(
                    [
                        gen_cnt,
                        d["genres"][gen],
                    ]
                )
                gen_cnt += 1

        # 작가 테이블 
        for art in range(len(d["artists"])) :
            for art2 in artist:
                if d["artists"][art] == art2[1]:
                    break
            else:
                artist.append(
                    [
                        art_cnt,
                        d["artists"][art],
                    ]
                )
                art_cnt += 1

        # 장르 전부 숫자로 바꿔주기
        for gen in range(len(d["genres"])):
            for gen2 in genre:
                if d["genres"][gen] == gen2[1]:
                    d["genres"][gen] = gen2[0]

        # 작가 전부 숫자로 바꿔주기
        for art in range(len(d["artists"])):
            for art2 in artist:
                if d["artists"][art] == art2[1]:
                    d["artists"][art] = art2[0]

        webtoon.append(
            [
                int(d["origin_id"]),
                d["title"],
                d["description"],
                d["genres"],
                d["artists"],
                rating,
                d["link"],
                d["thumb_img"],
                int(d["distinct"]),

            ]
        )

    webtoon_frame = pd.DataFrame(data=webtoon, columns=webtoon_columns)
    genre_frame = pd.DataFrame(data=genre, columns=genre_columns)
    artist_frame = pd.DataFrame(data=artist, columns=artist_columns)

    return {"webtoon": webtoon_frame, "genre": genre_frame, "artist": artist_frame}



def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[웹툰]")
    print(f"{separater}\n")
    print(data["webtoon"].head())
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()