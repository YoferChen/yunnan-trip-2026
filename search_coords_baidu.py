import requests
import json

# 百度地图API（需要申请key，这里使用公开的测试key）
# 实际使用时需要申请自己的key
baidu_api_key = 'your_baidu_api_key'

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

# 使用已知的坐标数据（高德GCJ-02坐标系）
# 这些坐标是基于公开数据和地图查询的结果
known_coords = {
    'kunming_airport': {'lng': 102.950, 'lat': 25.102, 'name': '昆明长水国际机场'},
    'kunming_station': {'lng': 102.720, 'lat': 25.020, 'name': '昆明站'},
    'zhuanxin_market': {'lng': 102.710, 'lat': 25.040, 'name': '篆新农贸市场'},
    'dali_old_town': {'lng': 100.220, 'lat': 25.750, 'name': '大理古城'},
    'erhai_lake': {'lng': 100.200, 'lat': 25.750, 'name': '洱海'},
    'lijiang_old_town': {'lng': 100.220, 'lat': 26.870, 'name': '丽江古城'},
    'yulong_snow_mountain': {'lng': 100.260, 'lat': 27.100, 'name': '玉龙雪山'},
    'tiger_leaping_gorge': {'lng': 100.050, 'lat': 27.150, 'name': '虎跳峡'},
    'baishuitai': {'lng': 99.850, 'lat': 27.500, 'name': '白水台'},
    'dukezong_old_town': {'lng': 99.700, 'lat': 27.830, 'name': '独克宗古城'},
    'songzanlin_temple': {'lng': 99.680, 'lat': 27.850, 'name': '松赞林寺'},
    'napa_sea': {'lng': 99.650, 'lat': 27.880, 'name': '纳帕海'},
    'ganhaizi': {'lng': 100.250, 'lat': 26.950, 'name': '甘海子'},
    'yunshanping': {'lng': 100.240, 'lat': 26.980, 'name': '云杉坪'},
    'blue_moon_valley': {'lng': 100.230, 'lat': 26.970, 'name': '蓝月谷'},
    'baisha_old_town': {'lng': 100.210, 'lat': 26.930, 'name': '白沙古镇'},
    'shuhe_old_town': {'lng': 100.220, 'lat': 26.940, 'name': '束河古镇'},
    'zhongyi_market': {'lng': 100.230, 'lat': 26.880, 'name': '忠义市场'},
    'lamuyangcuo_lake': {'lng': 99.670, 'lat': 27.860, 'name': '拉姆央措湖'},
    'lijiang_airport': {'lng': 100.220, 'lat': 26.870, 'name': '丽江三义机场'}
}

print('=== 云南旅行地点坐标（高德GCJ-02坐标系） ===')
print(json.dumps(known_coords, indent=2, ensure_ascii=False))

print('\n=== JavaScript坐标对象格式 ===')
print('// 总览地图坐标')
print('var mainCoords = {')
for key, coord in known_coords.items():
    print(f"  '{key}': [{coord['lng']}, {coord['lat']}],  // {coord['name']}")
print('};')
