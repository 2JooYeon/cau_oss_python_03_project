'''
menu_selector 모듈은 parking_spot_manager 모듈에 구현된 함수를 이용하여 
주차장 데이터를 출력하거나, 필터링 또는 정렬 후 데이터를 확인할 수 있습니다. 
'''
import file_manager
import parking_spot_manager

def start_process(path):
    ''' path를 입력받아 파일로부터 데이터를 가공하여 주차장 데이터를 출력 및 필터링 또는 정렬할 수 있습니다. 
    Args:
        path (str): 주차장 정보가 포함된 파일 경로
    '''
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))

        # 주차장 정보 출력 
        if select == 1:
            parking_spot_manager.print_spots(spots)

        # 주차장 정보 필터링 
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            # 자원명을 기준으로 필터링 하는 경우
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            # 시도를 기준으로 필터링 하는 경우
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            # 시군구를 기준으로 필터링 하는 경우
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            # 주차장 유형을 기준으로 필터링 하는 경우
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            # 위도와 경도를 기준으로 필터링 하는 경우
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_long = float(input('type min long:'))
                max_long = float(input('type max long:'))
                locations = (min_lat, max_lat, min_long, max_long)
                spots = parking_spot_manager.filter_by_location(spots, locations)
            else:
                print("invalid input")
        
        # 주차장 정보 정렬
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            # keyword가 지원목록에 있는 경우
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            # keyword가 지원목록에 없는 경우
            else: print("invalid input")

        # 반복을 종료 
        elif select == 4: 
            print("Exit")
            break

        # 잘못된 입력일 경우 
        else:
            print("invalid input")