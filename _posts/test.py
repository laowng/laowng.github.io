import requests
from requests import Session


if __name__ == '__main__':
    s=Session()
    s.headers={
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://cas.snnu.edu.cn',
    '$Referer': 'http://cas.snnu.edu.cn/uid/forget\\u0021forget4Reset',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    }
    response=s.get("http://yjssys.snnu.edu.cn/UserLogin.aspx")
    print(response.text)
    params = (
        ('ReturnUrl', '/Gstudent/loging.aspx?undefined'),
    )

    data = {
      '__EVENTTARGET': 'ctl00$contentParent$btLogin',
      '__EVENTARGUMENT': '',
      '__VIEWSTATE': '/wEPDwUKMTA4ODc5NDc0OA9kFgJmD2QWAgIDD2QWAgIDD2QWAgILD2QWAmYPZBYCAgEPDxYCHghJbWFnZVVybAUqfi9QdWJsaWMvVmFsaWRhdGVDb2RlLmFzcHg/aW1hZ2U9NzM1Mjg2OTI1ZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFIWN0bDAwJGNvbnRlbnRQYXJlbnQkVmFsaWRhdGVJbWFnZeeiiHYGyjoET06z1PMYICx02EqO',
      '__VIEWSTATEGENERATOR': '9B5C212B',
      '__EVENTVALIDATION': '/wEdAAY8IJkbojx2eA7pHtqhieH7cybtMhw0mn0LtKqAHeD/6LR/VkzxozH4tyiImdrtlAcUWWYub4JHktVQEGONTxqoRZzhTcnfFsWcwOVyhy6aT8GiwGHwM4Wl4obxma9ASlvYMwUeTGYtDsjbzWWPN8sDc6aVsQ==',
      'ctl00$contentParent$UserName': '182259',
      'ctl00$contentParent$PassWord': 'Caoqinghua123',
      'ctl00$contentParent$ValidateCode': '5309'
    }
    response=s.post('http://yjssys.snnu.edu.cn/gstudent/ReLogin.aspx', params=params, data=data,
          verify=False)
    print(response.text)
    data = {
      'needAlert': 'false',
      'needRedirect': 'true',
      'accountpwdstrength': '0',
      'accountpwd': 'Caoqinghua123',
      'checkpwd': 'Caoqinghua123'
    }
    response = s.post('http://cas.snnu.edu.cn/uid/forget_json/u0021forgetResetPwd', data=data, verify=False)