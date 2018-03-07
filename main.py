import requests
import datetime
import json
import csv
import time
if __name__=="__main__":
    base_url = 'https://band.us/band/'
    keyword = input(">>> 키워드를 입력하세요::")
    ts = str(int(datetime.datetime.now().timestamp()*1000))
    html = requests.get('https://api.band.us/v1.1.0/find_bands_with_keyword?client_info=%7B"language"%3A"ko"%2C"country"%3A"KR"%2C"version"%3A1%2C"agent_type"%3A"web"%2C"agent_version"%3A"3.3.1"%2C"resolution_type"%3A100%7D&language=ko&country=KR&version=1&akey=bbc59b0b5f7a1c6efe950f6236ccda35&DEVICE-TIME-ZONE-ID=Asia%2FSeoul&DEVICE-TIME-ZONE-MS-OFFSET=32400000&md=YPEmkkEkYxA5Jas%2BlH5z6vlS1LiS5isYc%2FLi4FnjZXk%3D&ts='+ts+'&after=1&limit=3&_=1520414839099&query='+keyword)
    data = json.loads(html.text)

    total = str(data['result_data']['total'])
    print(">>> 검색 개수 :: ",total )
    page = 1
    after = 1
    limit = 50
    while True:
        print("\t>>> ",page,'추출중 ... ')
        ts = str(int(datetime.datetime.now().timestamp() * 1000))
        html = requests.get(
            'https://api.band.us/v1.1.0/find_bands_with_keyword?client_info=%7B"language"%3A"ko"%2C"country"%3A"KR"%2C"version"%3A1%2C"agent_type"%3A"web"%2C"agent_version"%3A"3.3.1"%2C"resolution_type"%3A100%7D&language=ko&country=KR&version=1&akey=bbc59b0b5f7a1c6efe950f6236ccda35&DEVICE-TIME-ZONE-ID=Asia%2FSeoul&DEVICE-TIME-ZONE-MS-OFFSET=32400000&md=YPEmkkEkYxA5Jas%2BlH5z6vlS1LiS5isYc%2FLi4FnjZXk%3D&ts=' + ts + '&after='+str(after)+'&limit=50&_=1520414839099&query=' + keyword)
        data = json.loads(html.text)
        with open(keyword + '.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for item in data['result_data']['items']:
                spamwriter.writerow([item['name'], base_url + str(item['band_no']), item['member_count']])
        after += limit
        page += 1
        #time.sleep(2)
        if after >= int(total):
            break



