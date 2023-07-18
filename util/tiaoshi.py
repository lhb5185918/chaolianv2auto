from util.requestutil import Request

import requests

from util.reacase import Case_operation


from config.pathdta import case_path

loginurl = "https://chaolian-base-web.lingxitest.com/api/lingxi-auth/oauth/token?grant_type=sms&scope=all&sms_phone=18660282391&sms_id=&sms_value=123456"


def get_token():
    url =loginurl
    headers = {"Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
    res = requests.post(url = url,headers=headers).json()
    token  = {"Lingxi-Auth":"bearer "+res["access_token"],"Content-Type":"application/json;charset=UTF-8","Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
    return token


case = Case_operation().get_case(case_path,'zcysearch')
for i in case:
    if i['title']=='有对应数据的产业链名称搜索':
        print('ok')
