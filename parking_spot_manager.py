class parking_spot:
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {}
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        return self.__item[keyword]
    

def str_list_to_class_list(str_list):
    class_list = []
    for string in str_list:
        _, name, city, district, ptype, longitude, latitude = string.split(',')
        class_list.append(parking_spot(name, city, district, ptype, longitude, latitude))
    return class_list

def print_spots(spots):
    print(f'---print elements({len(spots)})---')
    for spot in spots:
        print(spot)

def filter_by_name(spots, name):
    return[spot for spot in spots if name in spot.get('name')]
     
def filter_by_city(spots, city):
    return[spot for spot in spots if city in spot.get('city')]

def filter_by_district(spots, district):
    return[spot for spot in spots if district in spot.get('district')]

def filter_by_ptype(spots, ptype):
    return[spot for spot in spots if ptype in spot.get('ptype')]

def filter_by_location(spots, locations):
    min_lat, max_lat, min_long, max_long = locations
    return[spot for spot in spots if spot.get('latitude') > min_lat and spot.get('latitude') < max_lat 
           and spot.get('longitude') > min_long and spot.get('longitude') < max_long] 

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)