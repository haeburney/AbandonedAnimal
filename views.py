from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render,redirect
from common.forms import UserForm,FindPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import requests
import time
from urllib.parse import unquote
import xml.etree.ElementTree as el





def covid(request):

    serviceUrl = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic'
    serviceKey = '7LL6m%2F9hLy1EGblVbDDPEBNdFCl6m9Ft%2Fmw2b5wuTaAq2IuINWejMUw46typtDua4NacB9UfALipcKcnoK4PJw%3D%3D&upkind=417000&state=notice&pageNo=1&numOfRows=10&neuter_yn=Y'
    serviceKey_decode = unquote(serviceKey)

    pageNo = '2'
    numOfRows = '10'
    startCreateDt = '20200901'
    endCreateDt = time.strftime('%Y%m%d', time.localtime(time.time()))

    parameters = {"serviceKey": serviceKey_decode, "pageNo": pageNo, "numOfRows": numOfRows,
                  "startCreateDt": startCreateDt, "endCreateDt": endCreateDt}

    response = requests.get(serviceUrl, params=parameters)

    print(response.text)

    covidList=[]

    if response.status_code == 200:
        # print("응닫결과 : ",response.text)
        tree = el.fromstring(response.text)
        iter = tree.iter(tag="item")

        for element in iter:

            

            age = element.find('age')
            careNm = element.find('careNm')
            kindCd = element.find('kindCd')
            weight = element.find('weight')
            noticeEdt = element.find('noticeEdt')
            """
            createDt = element.find('createDt')  # 일시
            deathCnt = element.find('deathCnt')  # 사망자
            area = element.find('gubun')  # 지역
            inDec = element.find('incDec')  # 전일대비증감수
            defCnt = element.find('defCnt')  # 확진자수
            isolClearCnt = element.find('isolClearCnt')  # 격리해제수
            isolIngCnt = element.find('isolIngCnt')  # 격리중환자수
            localOccCnt = element.find('localOccCnt')  # 지역발생수
            overFlowCnt = element.find('overFlowCnt')  # 해외유입수
            qurRate = element.find('qurRate')  # 10만명당 발생률
            id = element.find('seq')  # 게시글번호(고유값)
            stdDay = element.find('stdDay')  # 기준일시
            updateDt  = element.find('updateDt ')  # 수정일시
            """
            
            data = {"age":age.text, "careNm":careNm.text, "kindCd":kindCd.text, "weight": weight.text,
            "noticeEdt":noticeEdt.text}
            covidList.append(data)

    context = {'covidList': covidList}
    print(covidList)
    return render(request,'protectedAnimal.html',context)