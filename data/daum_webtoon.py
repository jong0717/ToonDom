import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

webtoon_list_url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/sun?timeStamp=1599980322752"
webtoon_group = dict()

webtoon_req = requests.get( webtoon_list_url)
result = [] # result라는 이름으로 값 저장

if webtoon_req.status_code == 200:
    data = json.loads( webtoon_req.text )
    for i in range(len(data["data"])):
        Dict = dict()
        Dict["id"] = data["data"][i]["id"]
        Dict["title"] = data["data"][i]["title"]
        Dict["genres"] = []
        for j in range(len(data["data"][i]["cartoon"]["genres"])):
            Dict["genres"].append(data["data"][i]["cartoon"]["genres"][j]["name"])
        Dict["artists"] = []
        for j in range(len(data["data"][i]["cartoon"]["artists"])):
            Dict["artists"].append(data["data"][i]["cartoon"]["artists"][j]['name'])
        print(Dict["artists"])
        Dict["rating"] = data["data"][i]["averageScore"]
        Dict["link"] = 'http://webtoon.daum.net/webtoon/view/'+data["data"][i]["nickname"]
                
                
                
                
                
        
        
            
            
            
            
            
            
            
#     with open('C:\\Users\\multicampus\\Desktop\\Project2\Webtoon\\daum_webtoon.json', 'w', encoding='UTF-8-sig') as file:
#         file.write(json.dumps(result,ensure_ascii=False))
#         json.dump(result, make_file, indent="\t")
        
#     with open('C:\\Users\\multicampus\\Desktop\\Project2\Webtoon\\daum_webtoon.json', 'r',encoding="utf-8") as f:

#         json_data = json.load(f)

#     print(json.dumps(json_data, indent="\t") )