import requests
import json

api_key = 'c35ae2e7a1c547ed5b27d4aed249a2db'

locations = [
    {'keyword': '昆明长水机场', 'city': '昆明', 'key': 'kunming_airport'},
    {'keyword': '昆明站', 'city': '昆明', 'key': 'kunming_station'},
    {'keyword': '篆新农贸市场', 'city': '昆明', 'key': 'zhuanxin_market'},
    {'keyword': '大理古城', 'city': '大理', 'key': 'dali_old_town'},
    {'keyword': '洱海', 'city': '大理', 'key': 'erhai_lake'},
    {'keyword': '丽江古城', 'city': '丽江', 'key': 'lijiang_old_town'},
    {'keyword': '玉龙雪山', 'city': '丽江', 'key': 'yulong_snow_mountain'},
    {'keyword': '虎跳峡', 'city': '丽江', 'key': 'tiger_leaping_gorge'},
    {'keyword': '白水台', 'city': '迪庆', 'key': 'baishuitai'},
    {'keyword': '独克宗古城', 'city': '迪庆', 'key': 'dukezong_old_town'},
    {'keyword': '松赞林寺', 'city': '迪庆', 'key': 'songzanlin_temple'},
    {'keyword': '纳帕海', 'city': '迪庆', 'key': 'napa_sea'},
    {'keyword': '甘海子', 'city': '丽江', 'key': 'ganhaizi'},
    {'keyword': '云杉坪', 'city': '丽江', 'key': 'yunshanping'},
    {'keyword': '蓝月谷', 'city': '丽江', 'key': 'blue_moon_valley'},
    {'keyword': '白沙古镇', 'city': '丽江', 'key': 'baisha_old_town'},
    {'keyword': '束河古镇', 'city': '丽江', 'key': 'shuhe_old_town'},
    {'keyword': '忠义市场', 'city': '丽江', 'key': 'zhongyi_market'},
    {'keyword': '拉姆央措湖', 'city': '迪庆', 'key': 'lamuyangcuo_lake'},
    {'keyword': '丽江三义机场', 'city': '丽江', 'key': 'lijiang_airport'}
]

results = {}

for loc in locations:
    try:
        keyword = loc['keyword']
        city = loc['city']
        key = loc['key']
        url = f'https://restapi.amap.com/v3/place/text?key={api_key}&keywords={keyword}&city={city}&output=json'
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('status') == '1' and data.get('pois'):
            poi = data['pois'][0]
            location = poi.get('location', '').split(',')
            if len(location) == 2:
                results[key] = {
                    'name': poi.get('name', keyword),
                    'lng': float(location[0]),
                    'lat': float(location[1]),
                    'address': poi.get('address', '')
                }
                print(f'[OK] {keyword}: {location[0]}, {location[1]}')
            else:
                print(f'[ERROR] {keyword}: 坐标格式错误')
        else:
            print(f'[ERROR] {keyword}: {data.get("info", "未知错误")}')
    except Exception as e:
        print(f'[ERROR] {keyword}: {str(e)}')

print('\n=== 坐标搜索结果 ===')
print(json.dumps(results, indent=2, ensure_ascii=False))
