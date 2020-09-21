## TOONDOM REST API ver2.0



#### rest-auth/ 아래 api들

| 리소스  | POST                       | GET  | PUT  | DELETE |
| ------- | -------------------------- | ---- | ---- | ------ |
| /signup | 회원가입<br />반환값: 토큰 | X    | X    | X      |
| /login  | 로그인<br />반환값: 토큰   | X    | X    | X      |
| /logout | 로그아웃                   | X    | X    | X      |



#### api/ 아래 api들

| 리소스                           | POST              | GET                                                          | PUT                          | DELETE                        |
| -------------------------------- | ----------------- | ------------------------------------------------------------ | ---------------------------- | ----------------------------- |
| /rankings                        | X                 | 3개 플랫폼별 웹툰 실시간 순위 전체                           | X                            | X                             |
| /rankings?distinct=1             | X                 | 순위를 플랫폼으로 필터링<br />1: 네이버<br />2: 카카오<br />3: 다음 | X                            | X                             |
| /webtoons                        | X                 | 모든 웹툰 검색                                               | X                            | X                             |
| /webtoons/1                      | X                 | 웹툰 1에 대한 세부 정보 검색                                 | X                            | X                             |
| /webtoons?distinct=1             | X                 | 플랫폼으로 필터링<br />1: 네이버<br />2: 카카오<br />3: 다음 | X                            | X                             |
| /webtoons?genres_rels__name=개그 | X                 | 웹툰 장르별 필터링                                           | X                            | X                             |
| /webtoons?search=일기            | X                 | 웹툰 제목, 작가 이름으로 검색                                | X                            | X                             |
| /webtoons/1/stars                | 웹툰 1 평가       | 유저의 웹툰 1 평가 기록 조회                                 | 유저의 웹툰 1 평가 기록 변경 | 유저의 웹툰 1 평가 기록 삭제  |
| /webtoons/1/ratings              | X                 | 웹툰 평가 목록 전체                                          | X                            | X                             |
| /webtoons/1/wishes               | 웹툰 1 보고싶어요 | 유저의 웹툰 1 보고싶어요 여부 조회                           | X                            | 유저의 웹툰 1 보고싶어요 삭제 |
| /user/1                          | X                 | 유저 1 기본 정보 조회                                        | X                            | X                             |
| /users/1/stars                   | X                 | 유저 1의 평가 목록 조회                                      | X                            | X                             |
| /users/1/wishes                  | X                 | 유저 1의 보고싶어요 목록 조회                                | X                            | X                             |
| /genres                          | X                 | 장르 목록 조회                                               | X                            | X                             |



#### 각 api 입력값, 반환값

- /rankings?distinct=1

  ![image-20200918180621312](REST%20API%20ver2.0.assets/image-20200918180621312.png)



- /webtoons?search=일기

  ![image-20200918175840239](REST%20API%20ver2.0.assets/image-20200918175840239.png)



- /webtoons?genres_rels__name=개그

  ![image-20200918175558057](REST%20API%20ver2.0.assets/image-20200918175558057.png)



- /webtoons/1/stars 

  - get 요청 (headers에서 토큰값 필요) - 기록 있을 때 

  ![image-20200918180923193](REST%20API%20ver2.0.assets/image-20200918180923193.png)

  - get 요청 (headers에서 토큰값 필요) - 기록 없을 때

    ![image-20200918181701579](REST%20API%20ver2.0.assets/image-20200918181701579.png)

  - post, put 요청 (headers에서 토큰값 필요)  - content 필수 x, 방금 남긴 평가 반환

    ![image-20200918184302990](REST%20API%20ver2.0.assets/image-20200918184302990.png)



- /webtoons/1/ratings

  ![image-20200918232440276](REST%20API%20ver2.0.assets/image-20200918232440276.png)



- /webtoons/1/wishes

  - get 요청 (headers에서 토큰값 필요) - 기록 없을 때

    ![image-20200918215015364](REST%20API%20ver2.0.assets/image-20200918215015364.png)

  - post 요청 (headers에서 토큰값 필요) - 방금 보고싶어요 누른 것 반환

    ![image-20200918214657102](REST%20API%20ver2.0.assets/image-20200918214657102.png)



- /users/1/stars

  ![image-20200918235356153](REST%20API%20ver2.0.assets/image-20200918235356153.png)
  
  ![image-20200919001101681](REST%20API%20ver2.0.assets/image-20200919001101681.png)



- /users/1/wishes

  ![image-20200919000948141](REST%20API%20ver2.0.assets/image-20200919000948141.png)



- /genres

  ![image-20200918220449830](REST%20API%20ver2.0.assets/image-20200918220449830.png)
