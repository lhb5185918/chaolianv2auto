import pytest

from config.projectconfig import loginurl

import requests


@pytest.fixture(scope='function')

def get_token():
    url =loginurl
    headers = {"Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
    res = requests.post(url = url,headers=headers).json()
    token  = {"Lingxi-Auth":"bearer "+res["access_token"]}
    return token