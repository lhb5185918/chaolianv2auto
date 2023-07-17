import json



class Test_method:  # 用例数据处理


    @staticmethod
    def reaDcase(case):
        number = case['number']
        title = case['title']
        method = case['method']
        url = case['url']
        data = case['data']
        if data !=None and data!='':
            data = json.loads(case['data'])
        else:
            data = None
        dict_result = {'number': number,
                       'title': title,
                       'method': method,
                       'url': url,
                       'data': data}
        return dict_result