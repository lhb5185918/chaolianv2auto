import  requests
from config.pathdta import entup_path

login_url = 'https://chaolian-base-web.lingxitest.com/api/lingxi-auth/oauth/token?grant_type=sms&scope=all&sms_phone=18660282391&sms_id=&sms_value=123456'
login_header = {"Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0"}
login = requests.post(url = login_url,headers = login_header).json()['access_token']

hedaers = {"Authorization":"Basic bGluZ3hpX3NhYXM6bGluZ3hpX3NhYXNfc2VjcmV0","Lingxi-Auth":"bearer "+login}

up_url = "https://chaolian-base-web.lingxitest.com/api/lingxi-govent-connect/GovernmentConnect/importUpload"

files = {str("entListFile"): (str("upladent.xlsx"), open(str(entup_path), 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
data = {"entListFile":"(binary)"}
res = requests.post(url = up_url,files=files,headers = hedaers,data = data )
print(res.json())
