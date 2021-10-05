# -*- coding: utf-8 -*
import os
import sys
sys.path.append(os.path.dirname(__file__))
import requests
import socket
import Logger
logger = Logger.get_loger()
###########在此补充用户名和密码###############################
account = ""#学号
password = ""#密码
##########################################################

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
    if not account or not password:
        logger.error("请在auto_login.py文件指定位置补充学号和密码")
        return False
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
    if response.text.find("登录失败")>=0:
        logger.error("账号或密码错误")
        return False

    elif response.text.find("当前登录账号")>=0:
        logger.error("登陆成功")
        return True
    logger.error("网络连接错误")
    return False
def islogin():
    def socketTest(url):
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            resp=s.connect(("www.baidu.com",80))
            request_url = 'GET /s?wd=1 HTTP/1.0\r\nHost: {}\r\n\r\n'.format(url)
            s.send(request_url.encode())
            resp=s.recv(256)
            s.close()
            if resp.decode("utf8").find("10.196.0.242")>=0:#此ip为学校snnu服务器内网ip,若失效需更新
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

if __name__ == '__main__':
    try:
        if not islogin():
            login_snnu()
    except:
        logger.error("发生错误", exc_info=True)