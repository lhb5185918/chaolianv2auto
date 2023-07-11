import requests


class Request:

    def api_run(self, url, method, data=None, header=None, cookie=None, file=None, filename=None,
                file_path=None):
        if method == 'post':

            if file != None:
                files = {str(file): (str(filename), open(str(file_path), 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
                res = requests.post(url = url ,headers=header,json=data,files=files)

            else:
                res = requests.post(url = url ,headers=header,json=data)

        else:
            res = requests.get(url=url,headers = header)

        code = res.status_code
        cookies = res.cookies.get_dict()
        dict1 = dict()  # 创建空列表
        try:
            body = res.json()  # 接收返回json格式的响应
        except:
            body = res.text  # 接收返回text格式的响应报文
        dict1['code'] = code
        dict1['body'] = body
        dict1['cookies'] = cookies
        return dict1

    def send(self, url, method, **kwargs):
        return self.api_run(url=url, method=method, **kwargs)
