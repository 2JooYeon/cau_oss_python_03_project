'''
parking_spot_manager 모듈은 주차장에 관련된 함수 및 클래스를 제공하는 모듈입니다.
해당 클래스를 통해 주차장의 자원명, 시도, 시군구, 주차장 유형, 경도, 위도에 대해 접근할 수 있고
각 정보를 이용하여 필터링하거나 정렬하여 데이터를 확인할 수 있습니다. 
'''
class parking_spot:
    '''
    parking_spot 클래스는 주차장의 다양한 정보를 저장하는 클래스입니다. 
    주차장의 정보를 딕셔너리 형식으로 저장하는 __item필드가 존재합니다. 
    해당 변수는 생성자를 통해서만 생성 및 설정할 수 있으며, 생성 이후에는 수정이 불가능합니다. 
    '''
    def __init__(self, name, city, district, ptype, longitude, latitude):
        ''' 생성자를 통해 주차장의 정보(__item)를 설정합니다.
        Args:
            name (str): 자원명
            city (str): 시도
            district (str): 시군구
            ptype (str): 주차장 유형
            longitude (str): 경도
            latitude (str): 위도
        '''
        self.__item = {}
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    def __str__(self):
        ''' 주차장 정보를 출력하기 위해 문자열을 반환합니다.'''
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        '''keyword에 해당하는 주차장 정보를 반환합니다.
        Args:
            keyword (str): 주차장 객체에서 얻고 싶은 정보 유형
        '''
        return self.__item[keyword]
    

def str_list_to_class_list(str_list):
    ''' 문자열 리스트를 입력받아 parking_spot 클래스 객체 리스트로 변환 후 반환합니다.
    Args:
        str_list (list): 문자열 리스트
    Returns:
        (list): parking_spot 클래스 객체 리스트
    '''
    class_list = []
    for string in str_list:
        _, name, city, district, ptype, longitude, latitude = string.split(',')
        class_list.append(parking_spot(name, city, district, ptype, longitude, latitude))
    return class_list


def print_spots(spots):
    ''' parking_spot 클래스 객체 리스트를 입력받아 저장된 모든 객체 값을 출력합니다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
    '''
    print(f'---print elements({len(spots)})---')
    for spot in spots:
        print(spot)
    

def filter_by_name(spots, name):
    ''' parking_spot 클래스 객체 리스트에서 자원명에 name을 포함하고 있는 객체 리스트를 반환한다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        name (str): 필터링할 검색어
    Returns:
        (list): 필터링 된 parking_spot 클래스 객체 리스트
    '''
    return[spot for spot in spots if name in spot.get('name')]
     

def filter_by_city(spots, city):
    ''' parking_spot 클래스 객체 리스트에서 시도에 city를 포함하고 있는 객체 리스트를 반환한다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        city (str): 필터링할 검색어
    Returns:
        (list): 필터링 된 parking_spot 클래스 객체 리스트
    '''
    return[spot for spot in spots if city in spot.get('city')]

def filter_by_district(spots, district):
    ''' parking_spot 클래스 객체 리스트에서 시군구에 district를 포함하고 있는 객체 리스트를 반환한다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        district (str): 필터링할 검색어
    Returns:
        (list): 필터링 된 parking_spot 클래스 객체 리스트
    '''
    return[spot for spot in spots if district in spot.get('district')]


def filter_by_ptype(spots, ptype):
    ''' parking_spot 클래스 객체 리스트에서 주차장 유형에 ptype를 포함하고 있는 객체 리스트를 반환한다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        ptype (str): 필터링할 검색어
    Returns:
        (list): 필터링 된 parking_spot 클래스 객체 리스트
    '''
    return[spot for spot in spots if ptype in spot.get('ptype')]


def filter_by_location(spots, locations):
    ''' parking_spot 클래스 객체 리스트에서 위도가 최소위도보다 크고, 최대위도보다 작으며, 
        경도가 최소경도보다 크고, 최대경도보다 작은 객체 리스트를 반환한다.
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        locations (tuple): 최소위도, 최대위도, 최소경도, 최대경도
    Returns:
        (list): 필터링 된 parking_spot 클래스 객체 리스트
    '''
    min_lat, max_lat, min_long, max_long = locations
    return[spot for spot in spots if spot.get('latitude') > min_lat and spot.get('latitude') < max_lat 
           and spot.get('longitude') > min_long and spot.get('longitude') < max_long] 


def sort_by_keyword(spots, keyword):
    ''' parking_spot 클래스 객체 리스트에서 keyword를 기준으로 객체 리스트를 정렬하여 반환한다. 
    Args:
        spots (list): parking_spot 클래스 객체 리스트
        keyword (str): 정렬 기준
    Returns:
        (list): 정렬된 parking_spot 클래스 객체 리스트
    '''
    return sorted(spots, key = lambda x : x.get(keyword))


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