import requests
import re
import time
###########在此补充用户名和密码###############################
account = ""
password = ""
#########################################################


def test():
    if not account or not password:
        print("请补充用户名和密码")
        return
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
    cho=["unicom"]
    pattern=re.compile(r"<td bgcolor=\"#FFFFFF\"><iframe align=\"middle\" frameborder=\"0\" width=\"100%\" height=\"200\" scrolling=\"yes\" src=\"(.*?)\"")
    for i in range(500):
        print(i)
        requests.get('http://202.117.144.205:8601/snnuportal/logoff', headers=headers, verify=False)
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
        url = pattern.search(response.text).group(1)
        table=requests.get(url, headers=headers, verify=False)
        if table.text.find("78:44:fd:83:95:e9")<0:
            print("success")
            break
if __name__ == '__main__':
    test()