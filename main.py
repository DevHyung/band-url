import requests
import datetime
import json
import time
from openpyxl import Workbook
if __name__=="__main__":
    base_url = 'https://band.us/band/'
    keyword = input(">>> 키워드를 입력하세요::")
    delay = float(input(">>> 페이지당 딜레이를 입력하세요::"))
    ts = str(int(datetime.datetime.now().timestamp()*1000))
    html = requests.get('https://api.band.us/v1.1.0/find_bands_with_keyword?client_info=%7B"language"%3A"ko"%2C"country"%3A"KR"%2C"version"%3A1%2C"agent_type"%3A"web"%2C"agent_version"%3A"3.3.1"%2C"resolution_type"%3A100%7D&language=ko&country=KR&version=1&akey=bbc59b0b5f7a1c6efe950f6236ccda35&DEVICE-TIME-ZONE-ID=Asia%2FSeoul&DEVICE-TIME-ZONE-MS-OFFSET=32400000&md=YPEmkkEkYxA5Jas%2BlH5z6vlS1LiS5isYc%2FLi4FnjZXk%3D&ts='+ts+'&after=1&limit=3&_=1520414839099&query='+keyword)
    data = json.loads(html.text)

    total = str(data['result_data']['total'])
    print(">>> 검색 개수 :: ",total )
    page = 1
    after = 1
    limit = 50
    datalist = []
    datalist.clear()
    while True:
        print("\t>>> ",page,'페이지 추출중 ... ')
        ts = str(int(datetime.datetime.now().timestamp() * 1000))
        html = requests.get(
            'https://api.band.us/v1.1.0/find_bands_with_keyword?client_info=%7B"language"%3A"ko"%2C"country"%3A"KR"%2C"version"%3A1%2C"agent_type"%3A"web"%2C"agent_version"%3A"3.3.1"%2C"resolution_type"%3A100%7D&language=ko&country=KR&version=1&akey=bbc59b0b5f7a1c6efe950f6236ccda35&DEVICE-TIME-ZONE-ID=Asia%2FSeoul&DEVICE-TIME-ZONE-MS-OFFSET=32400000&md=YPEmkkEkYxA5Jas%2BlH5z6vlS1LiS5isYc%2FLi4FnjZXk%3D&ts=' + ts + '&after='+str(after)+'&limit=50&_=1520414839099&query=' + keyword)
        data = json.loads(html.text)
        for item in data['result_data']['items']:
            datalist.append([item['name'], base_url + str(item['band_no']), item['member_count']])
        after += limit
        page += 1
        time.sleep(delay)
        if after >= int(total):
            break
    header1 = ['이름', 'URL', 'member_count']
    wb = Workbook()
    ws1 = wb.worksheets[0]
    ws1.column_dimensions['A'].width = 30
    ws1.column_dimensions['B'].width = 50
    ws1.column_dimensions['C'].width = 20
    ws1.append(header1)
    # 데이터 삽입
    # itemlist 가 [품명,최저가,링크] 이런식으로 온걸
    # openpyxl 객체 ws1 에 append 시키면 들어감
    for itemlist in datalist:
        ws1.append(itemlist)
    wb.save(keyword + ".xlsx")
    print(">>> 파일저장완료")
    input("엔터키나 아무키를 누르시면 종료됩니다. ")


