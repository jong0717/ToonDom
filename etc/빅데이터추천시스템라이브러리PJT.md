## 빅데이터 추천시스템 라이브러리

#### 1 REST

##### 장고REST프레임워크

- [공식문서](https://www.django-rest-framework.org/)
- [공식문서 튜토리얼](https://www.django-rest-framework.org/tutorial/quickstart/)

- REST는 웹의 장점을 최대한으로 활용할 수 있는 네트워크 기반의 아키텍쳐

- RESTful하게 개발을 하면 쉽고, 기존 웹(HTTP)을 그대로 따라가면서도 의미적으로 구조가 잘 잡힌 URI를 만들 수 있음

  - RESTful URI로 URI를 통해 자원(resource)가 /게시판들 중 첫번째 게시판의 글들 중 406번째 글임을 쉽게 알 수 있다.

  ```
  http://class.net/boards/1/posts/406
  ```

- **URI**를 이용해 명시된 자원(resource)에 접근하고,
  자원(resource)에 어떠한 조작(CRUD)을 할 지 **HTTP 메서드**로 나타내는 방법

| HTTP Method | CRUD   | 기능 |
| ----------- | ------ | ---- |
| POST        | CREATE | 생성 |
| GET         | READ   | 조회 |
| PUT         | UPDATE | 갱신 |
| DELETE      | DELETE | 삭제 |





#### 2 :handshake: **빅데이터 추천 알고리즘**

- 빅데이터 추천 알고리즘 방법/시스템 :협업필터링, 컨텐츠기반필터링, 앙상블 기법, 유사도 등...

  - 협업필터링 CF, Collaborative Filtering : 너무나 비슷한 너와 나, 내가 좋아하는 이건 넌 어때?
    - 유저기반, 누적된 정보가 필요함. 비교를 위한 항목들도 결정해야 함
  - 컨텐츠기반필터링 CB, Contents Based Filtering : 무언가를 좋아한다면, 혹시 이것도 좋아해? 
    - 아이템 끼리 연관성을 토대로 추천. 
  - 앙상블 : 
  - 유사도 계산 : 코사인Cosine유사도, 피어슨Pearson, 내적Inner Product, 유클리디안Euclideam거리함수 (협업, 컨텐츠 무시가능)

- Python 추천 시스템 특화 라이브러리  : LigthFM, Surprise, PySpark

  - LigthFM : 기본 및 하이브리드 추천, 데이터가 충분하지 않아도 추천 

    - [공식문서](https://making.lyst.com/lightfm/docs/index.html)
    - [예시](https://towardsdatascience.com/recommendation-system-in-python-lightfm-61c85010ce17)

  - Surprise : 협업필터링 위한 알고리즘 제공 라이브러리

    - [공식홈페이지](http://surpriselib.com/)

      ```
      $ pip install numpy
      $ pip install scikit-surprise
      ```

    - [공식문서](https://surprise.readthedocs.io/en/stable/) -함수사용법

    - [튜토리얼](https://blog.cambridgespark.com/tutorial-practical-introduction-to-recommender-systems-dbe22848392b) -numpy 와 surprise 사용 추천시스템 구현

  - PySpark : 대용량 처리 속도 면 이점, 스타크는 분산 클러스터 용도, 머신러닝 알고리즘 포함

    - [공식문서] http://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#module-pyspark.mllib.recommendation
    - ALS 알고리즘 사용 튜토리얼 https://www.youtube.com/watch?v=FgGjc5oabrA
    - 번개장터 추천시스템 도입 클러스터 구성  https://www.theteams.kr/teams/7937/post/70673