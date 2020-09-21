import itertools
from collections import Counter
from parse import load_dataframes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 지도화
import folium


def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


def show_store_categories_graph(dataframes, n=30):
    """
    Tutorial: 전체 음식점의 상위 `n`개 카테고리 분포를 그래프로 나타냅니다.
    """

    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    # 2 차원 리스트 1차원으로
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)

    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )

    # 그래프로 나타냅니다
    chart = sns.barplot(x="category", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 카테고리 분포")
    plt.show()


def show_store_review_distribution_graph(dataframes):
    """
    Req. 1-3-1 전체 음식점의 리뷰 개수 분포를 그래프로 나타냅니다. 
    """

    stores = dataframes["stores"]
    
    # 2 차원 리스트 1차원으로
    reviews_cnt = stores.review_cnt
    reviews_count = Counter(list(reviews_cnt))

    # 정렬
    reviews_sorted = sorted(reviews_count.items())

    # 데이터프레임화
    df = pd.DataFrame(reviews_sorted, columns=["reviews", "count"])
    
    # 그래프
    chart = sns.barplot(x="reviews", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 리뷰 개수 분포")
    plt.show()


def show_store_average_ratings_graph(dataframes, n=20):
    """
    Req. 1-3-2 각 음식점의 평균 평점을 그래프로 나타냅니다.
    """
    # 가게와 가게별 평점 머지
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )

    # 가게 이름으로 그룹바이
    scores_group = stores_reviews.groupby(["store", "store_name"])
    # 가게 별 평점 평균 내기(이때 review_cnt는 원래 store 테이블에 있었기 때문에 mean해도 같음)
    scores = scores_group.mean() 
    # 정렬
    score_decs = scores.sort_values(by=["score"], ascending=False)
    # 상위 20개 뽑기 - 평가가 30개 이상인 것만
    score_result = score_decs[score_decs.review_cnt >= 30].head(n=n).reset_index()

    # 그래프
    chart = sns.barplot(x="store_name", y="score", data=score_result)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 평균 평점 분포")
    plt.show()


def show_user_review_distribution_graph(dataframes, n=20):
    """
    Req. 1-3-3 전체 유저의 리뷰 개수 분포를 그래프로 나타냅니다.
    """
    users = dataframes["reviews"]
    # 유저 아이디로 그룹 바이
    users_group = users.groupby(["user"])
    # 개수 카운트
    users_count = users_group.count() 
    # 정렬
    users_decs = users_count.sort_values(by=["id"], ascending=False)
    # 상위 20개 뽑기
    user_result = users_decs.head(n=n).reset_index()

    # 그래프
    chart = sns.barplot(x="user", y="content", data=user_result)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("사용자별 리뷰 개수 분포")
    plt.show()


def show_user_age_gender_distribution_graph(dataframes):
    """
    Req. 1-3-4 전체 유저의 성별/나이대 분포를 그래프로 나타냅니다.
    """
    users = dataframes["reviews"]

    # 성별로 그룹 바이
    users_group = users.groupby(["gender"])
    # 개수 카운트
    users_count = users_group.count().reset_index()

    # 그래프
    chart = sns.barplot(x="gender", y="user", data=users_count)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("사용자별 리뷰 개수 분포")
    plt.show()


def show_stores_distribution_graph(dataframes, n=20):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    stores = dataframes["stores"]
    # 정렬
    store_decs = stores.sort_values(by=["latitude"], ascending=False)
    # 상위 20개 뽑기
    store_result = store_decs.head(n=n).reset_index()

    # 지도화
    # 1. 지도의 중심 지정
    latitude_center = store_result['latitude'].astype(float).mean()
    longitude_center = store_result['longitude'].astype(float).mean()
    m = folium.Map([latitude_center,longitude_center],zoom_start=9)

    # 2. 식당 위치 찍기
    for i in store_result.index:
        sub_lat =  store_result.loc[i,'latitude']
        sub_long = store_result.loc[i,'longitude']
        title = store_result.loc[i,'store_name']

        folium.Marker([sub_lat,sub_long],tooltip = title).add_to(m)

    # 3. 파일로 저장
    m.save('result.html')


def main():
    set_config()
    data = load_dataframes()
    # 카테고리 순위
    show_store_categories_graph(data)
    # 음식점 리뷰 분포
    show_store_review_distribution_graph(data)
    # 음식점 별 평점 평균
    show_store_average_ratings_graph(data)
    # 유저별 리뷰 개수 
    show_user_review_distribution_graph(data)
    # 유저 성별 분포
    show_user_age_gender_distribution_graph(data)
    # 지도화
    show_stores_distribution_graph(data)


if __name__ == "__main__":
    main()
