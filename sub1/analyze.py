from parse import load_dataframes
import pandas as pd
import shutil


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
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
    # 20개 뽑기 - 평가가 30개 이상인것만
    # reset_index() 사용해야 그룹핑 기준이 된 열들도 컬럼 취급 받게 됨
    return score_decs[score_decs.review_cnt >= min_reviews].head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    stores = dataframes["stores"]
    # 정렬
    store_decs = stores.sort_values(by=["review_cnt"], ascending=False)

    return store_decs.head(n=n).reset_index()


def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    users = dataframes["reviews"]
    # 유저 아이디로 그룹 바이
    users_group = users.groupby(["user"])
    # 개수 카운트
    users_count = users_group.count() 
    # 정렬
    users_decs = users_count.sort_values(by=["id"], ascending=False)

    return users_decs.head(n=n).reset_index()


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    stores_most_scored = sort_stores_by_score(data)

    print("[최고 평점 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_scored.iterrows():
        print(
            "{rank}위: {store}({score}점, 리뷰: {reviews}개)".format(
                rank=i + 1, store=store.store_name, score=store.score, reviews=int(store.review_cnt)
            )
        )
    print(f"\n{separater}\n\n")

    stores_most_reviewed = get_most_reviewed_stores(data)

    print("[리뷰순 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_reviewed.iterrows():
        print(
            "{rank}위: {store}(리뷰: {reviews}개)".format(
                rank=i + 1, store=store.store_name, reviews=int(store.review_cnt)
            )
        )
    print(f"\n{separater}\n\n")

    most_active_users = get_most_active_users(data)

    print("[리뷰 많이 남긴 이용자]")
    print(f"{separater}\n")
    for i, user in most_active_users.iterrows():
        print(
            "{rank}위: {user}(리뷰: {reviews}개)".format(
                rank=i + 1, user=user.user, reviews=int(user.id)
            )
        )
    print(f"\n{separater}\n\n")

if __name__ == "__main__":
    main()
