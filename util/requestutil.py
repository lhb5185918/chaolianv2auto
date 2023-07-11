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
