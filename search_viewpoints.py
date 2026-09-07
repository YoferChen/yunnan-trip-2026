import requests
import json

api_key = '6c6d950dcb926b5ffba63f5b8daaefad'

viewpoints = [
    {'keyword': '手擎双虹观景台', 'city': '丽江', 'key': 'shuanghong_viewpoint'},
    {'keyword': '望天瀑观景台', 'city': '丽江', 'key': 'wangtianfall_viewpoint'},
    {'keyword': '下虎跳观景台', 'city': '丽江', 'key': 'lower_tiger_viewpoint'},
    {'keyword': '哈巴雪山观景台', 'city': '丽江', 'key': 'haba_snow_viewpoint'},
    {'keyword': '九仙峰观景台', 'city': '丽江', 'key': 'jiuxianfeng_viewpoint'}
]

results = {}

for loc in viewpoints:
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
            print(f'[ERROR] {keyword}: {data.get("info", "未找到")}')
    except Exception as e:
        print(f'[ERROR] {keyword}: {str(e)}')

print('\n=== 观景台坐标搜索结果 ===')
print(json.dumps(results, indent=2, ensure_ascii=False))
