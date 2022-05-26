import requests
import xmltodict
import time

def animal():
    encodingKey = "7LL6m%2F9hLy1EGblVbDDPEBNdFCl6m9Ft%2Fmw2b5wuTaAq2IuINWejMUw46typtDua4NacB9UfALipcKcnoK4PJw%3D%3D"
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=" + encodingKey + "&bgnde=20220501&endde=20220526&state=notice&pageNo=1&numOfRows=10&neuter_yn=Y"

    req = requests.get(url).content
    xmlObject = xmltodict.parse(req)

    allData=xmlObject['response']['body']['items']['item']
    print(allData)

animal()