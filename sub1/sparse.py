import itertools
from collections import Counter
from parse import load_dataframes
import pandas as pd


def show_sparse_user_store_scores(dataframes, n=20, min_reviews=30):
    """
    Req. 1-4-1 유저-음식점 행렬 생성
    
    """   
    # 가게와 가게별 평점 머지
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )

    print(stores_reviews.head(n=5))




# 메인
data = load_dataframes()
show_sparse_user_store_scores(data)



