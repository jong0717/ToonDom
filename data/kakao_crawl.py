import requests
import json
import os
import shutil
# 개발자도구 > 네트워크
# https://api2-page.kakao.com/api/v2/store/day_of_week_top/list?category=10&subcategory=0&page=0&day=1&bm=A
days = [1, 2, 3, 4, 5, 6, 7, 12]  # 월~일, 완결
result = []
for day in days:

    for page_num in range(0, 100):
        webtoon_list_url = "https://api2-page.kakao.com/api/v2/store/day_of_week_top/list?category=10&subcategory=0&page={}&bm=A&day={}".format(page_num, day)
        print("REQUEST {}".format(webtoon_list_url))
        webtoon_req = requests.get(webtoon_list_url)

        if webtoon_req.status_code == 200:
            data = json.loads(webtoon_req.text)

            for item in data["list"]:
                if item["rank"]:
                    parsed_item = dict()
                    # parsed_item["id"] = 'KAKAO{}'.format(item["series_id"])
                    parsed_item["origin_id"] = item["series_id"]
                    parsed_item["title"] = item["title"]
                    parsed_item['description'] = item.get('caption', '')
                    # parsed_item['caption'] = item.get('caption', '')
                    # parsed_item['description'] = item.get('description', '')
                    parsed_item["genres"] = [item['sub_category_title']]
                    parsed_item["artists"] = item['author'].split(',')
                    parsed_item["link"] = 'https://page.kakao.com/home?seriesId={}'.format(item["series_id"])
                    parsed_item["rating"] = item.get("rating", 0) # 값이 없는 경우가 있음. 이건 일단 0으로
                    # parsed_item["like_count"] = item.get('like_count', 0)  # 좋아요. 값이 없는 경우가 있음. 이건 일단 0으로

                    # 이미지 일단 제일 큰걸로 가져오기
                    parsed_item['thumb_img'] = "https://dn-img-page.kakao.com/download/resource?kid={}&filename=th1".format(item['land_thumb_img'])
#                     if not os.path.isfile(parsed_item['thumb_img']):
#                         #파일 없는 경우에만 다운로드
#                         dir_path = os.path.dirname(parsed_item['thumb_img'])
#                         os.makedirs(dir_path, exist_ok=True)
#                         download_url = "https://dn-img-page.kakao.com/download/resource?kid={}&filename=th1".format(item['land_thumb_img'])
#                         response = requests.get(download_url, stream=True)
#                         print("DOWNLOAD FILE : {}".format(download_url))
#                         with open(parsed_item['thumb_img'], 'wb') as out_file:
#                             shutil.copyfileobj(response.raw, out_file)
#                         del response
                    # 'distinct': 1:네이버, 2:카카오, 3:다음 
                    parsed_item["distinct"] = "2"
                    result.append(parsed_item)

            if data['is_end']:
                break

with open('kakao_webtoon.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(result, ensure_ascii=False))

# print(webtoon_list_url)