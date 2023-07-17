import pytest

from util.requestutil import Request

from util.reacase import Case_operation

from common.casesuper import Test_method

from config.pathdta import case_path

from util.logutil import logger

class TestIndustry(Test_method):

    res =Case_operation().get_case(case_path,'zcy')


    @pytest.mark.parametrize('case',res)

    def test_highselect(self,case,get_token):
        result = TestIndustry.reaDcase(case)
        res = Request().send(url = result['url'],
                             method=result['method'],
                             data=result['data'],
                             header = get_token)

        logger.info("{}{}{},".format(result['number'], result['title'], res))

        assert res['code']==200

        assert res['body']['msg']=='操作成功'


        Case_operation().write_result(xulie=0)




