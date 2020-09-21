결과 REST API 문서

광주2반 C203팀 특화PJT (빅데이터) : ToonDom 통합웹툰추천

회원정보 

| HTTP Method | 리소스                   | 기능          | 매개변수                        |
| ----------- | ------------------------ | ------------- | ------------------------------- |
| POST        | /rest-auth/registration/ | 회원가입_생성 | username id password1 password2 |
| POST        | /rest-auth/login/        | 로그인        | id password Returns Token key   |
| POST        | /rest-auth/logout/       | 로그아웃      |                                 |
| DELETE      | /rest-auth/              | 회원탈퇴_제거 |                                 |


# 

| HTTP Method | 리소스                          | 기능                                         | 매개변수                                                     |
| ----------- | ------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| GET         | /rankings                       | 메인페이지_데이터 조회                       | distinct (1:네이버, 2:카카오, 3:다음)                        |
| GET         | /webtoons                       | 웹툰 조회                                    | page_size<br />size<br />search :검색어 - 옵셔널. 공백시 전체<br />genres_rels__name : 옵셔널, 장르 이름. 공백시 전체 |
| GET         | /webtoons/{webtoon_id}          | 웹툰의 상세페이지_조회                       | webtoon_id : 웹툰 ID                                         |
| 별점        |                                 |                                              |                                                              |
| POST        | /webtoons/{webtoon_id}/stars/   | 자기 자신의 웹툰 별점 평가                   | rating : 1~10 점 사이의 별점(정수)                           |
| GET         | /webtoons/{webtoon_id}/stars/   | 자기 자신의 웹툰 별점 조회                   | webtoon_id : 웹툰 ID                                         |
| PUT         | /webtoons/{webtoon_id}/stars/   | 자기 자신의 웹툰 별점 수정 및 코멘트 추가    | rating : 1~10점 사이의 별점(정수) - 값을 줄 경우에만 수정, 주지 않으면 수정하지 않음<br />content : 문자열 - 값을 줄 경우에만 수정, 주지않으면 수정하지 않음 |
| DELETE      | /webtoons/{webtoon_id}/stars/   | 자기 자신의 웹툰 별점, 코멘트 삭제           |                                                              |
| 보고픔      |                                 |                                              |                                                              |
| POST        | /webtoons/{webtoon_id}/wishes/  | 웹툰의 보고싶어요_작성                       | webtoon_id : 웹툰 ID                                         |
| GET         | /webtoons/{webtoon_id}/wishes/  | 해당 웹툰의 보고싶어요_조회                  |                                                              |
| DELETE      | /webtoons/{webtoon_id}/wishes/  | 웹툰의 보고싶어요(자기자신에 대한) 삭제/취소 |                                                              |
| 유저별      |                                 |                                              |                                                              |
| GET         | /user/{user_id or 'me'}         | 나(me) 또는 다른 유저의 데이터 조회          | 정수 타입의 user_id 또는 문자열 'me'<br />example: /users/me, /users/12345 |
| GET         | /users/{user_id or 'me'}/stars  | 유저별 별점평가한 목록_조회                  | page<br />size<br />                                         |
| GET         | /users/{user_id or 'me'}/wishes | 유저별 보고싶음 목록_조회                    | page<br />size<br />                                         |
| 장르        |                                 |                                              |                                                              |
| GET         | /genres                         | 장르 목록_조회                               | search : 장르이름 -옵셔널. 공백시 전체                       |
| GET         | /genres/{genres_id}             | 특정 장르_조회                               | genres_id : 장르 ID                                          |

| HTTP Method             | 리소스     | 기능                        | 매개변수                          |
| ----------------------- | ---------- | --------------------------- | --------------------------------- |
| GET                     | /          | 메인페이지_조회             |                                   |
| GET                     | /detail/   | 웹툰의 상세페이지_조회      | id(webtoon)                       |
| POST<br/>PUT<br/>DELETE | /star/     | 웹툰의 별점_평가,수정,취소  | id(webtoon), id(user), 점수, 댓글 |
| POST<br/>DELETE         | /wish/     | 웹툰의 보고싶어요_작성,삭제 | id(webtoon), id(user)             |
| GET                     | /user/     | 유저별 상세페이지_조회      | id(user)                          |
| GET                     | /starlist/ | 유저별 별점평가한 목록_조회 | id(user)                          |
| GET                     | /wishlist/ | 유저별 보고싶음 목록_조회   | id(user)                          |
| GET                     | /search/   | 웹툰이름으로 검색_조회      |                                   |




여기부터 결과 참고.

![image-20200917132127533](REST API.assets/image-20200917132127533.png)



![image-20200917132253756](REST API.assets/image-20200917132253756.png)

![image-20200917132358648](REST API.assets/image-20200917132358648.png)



![image-20200917132526114](REST API.assets/image-20200917132526114.png)

별점평가하기

![image-20200917132653553](REST API.assets/image-20200917132653553.png)



![image-20200917132835252](REST API.assets/image-20200917132835252.png)



![image-20200917132945658](REST API.assets/image-20200917132945658.png)

보고싶어요

![image-20200917133140324](REST API.assets/image-20200917133140324.png)



웹툰검색

![image-20200917133344777](REST API.assets/image-20200917133344777.png)



![image-20200917133432614](REST API.assets/image-20200917133432614.png)



![image-20200917133513680](REST API.assets/image-20200917133513680.png)