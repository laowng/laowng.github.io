import requests
import re
import socket
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import json
###########在此补充用户名和密码###############################
account = ""
password = ""
##########################################################
accessKeyId = ""
accessSecret = ""
#########################################################
headers = {
        'Proxy-Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://202.117.144.205:8602',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://202.117.144.205:8602/snnuportal/login.jsp',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    }
def login_snnu():
    data = {
                'account': account,
                'password': password,
                'method': 'getUserInfo'
            }

    response = requests.post('http://202.117.144.205:8601/snnuportal/bind', headers=headers, data=data,
                             verify=False)
    data = {
        'sourceurl': 'null',
        'account': account,
        'password': password,
        'yys': '',
        'issave': ''
    }
    response=requests.post('http://202.117.144.205:8601/snnuportal/login', headers=headers, data=data,
                  verify=False)

def get_ip():
    try:
        response = requests.get('http://202.117.144.205:8601/snnuportal/login', headers=headers).text
        Pattern=re.compile("当前IP[:：](.*?)[^0123456789.]")
        ip=Pattern.search(response).group(1)
        return ip
    except:
        return None
def islogin():
    def socketTest(url):
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            resp=s.connect(("www.baidu.com",80))
            request_url = 'GET /s?wd=1 HTTP/1.0\r\nHost: {}\r\n\r\n'.format(url)
            s.send(request_url.encode())
            resp=s.recv(1024)
            s.close()
            if resp.decode("utf8").find("HTTP/1.1 302")>=0:
                return False
            return True
        except:
            s.close()
            return False
    urls=["www.baidu.com","www.sogou.com","www.weibo.com"]
    for url in urls:
        if socketTest(url):
            return True
    return False

def aliyun_updateDominRecord(recordID,ip):
    # !/usr/bin/env python
    # coding=utf-8


    client = AcsClient(accessKeyId, accessSecret, 'cn-xian')

    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')

    request.set_RecordId(recordID)
    request.set_RR("3312")
    request.set_Type("A")
    request.set_Value(ip)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))
def getRecorderList_3312recorderid():
    client = AcsClient(accessKeyId, accessSecret, 'cn-xian')

    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_DomainName("funcube.top")

    response = client.do_action_with_exception(request)
    recoderlist=json.loads(response)['DomainRecords']['Record']
    for recoder in recoderlist:
        if recoder["RR"]=="3312":
            return recoder['RecordId']
    return None

def update3312Recoder():
    try:
        if not islogin():
            login_snnu()
        recorderID_3312=getRecorderList_3312recorderid()
        ip_3312=get_ip()
        aliyun_updateDominRecord(recorderID_3312,ip_3312)
    except:
        pass
if __name__ == '__main__':
    print(getRecorderList_3312recorderid())
