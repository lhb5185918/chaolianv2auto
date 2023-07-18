import pytest

from config.projectconfig import loginurl

import requests


@pytest.fixture(scope='function')

def get_token():
    url =loginurl
    headers = {"Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
    res = requests.post(url = url,headers=headers).json()
    token  = {"Lingxi-Auth":"bearer "+res["access_token"],"Content-Type":"application/json;charset=UTF-8","Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
    return token


@pytest.fixture(scope='function')
def get_industryids(get_token):
    url = 'https://chaolian-base-web.lingxitest.com/api/lingxi-system/monitor/list?name='
    res = requests.get(url=url,headers = get_token).json()['data']['id']
    return res