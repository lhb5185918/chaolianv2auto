import pytest

from util.requestutil import Request

from util.reacase import Case_operation

from common.casesuper import Test_method

from config.pathdta import case_path

from util.logutil import logger

class TestIndustry(Test_method):

    res =Case_operation().get_case(case_path,'zcysearch')


    @pytest.mark.parametrize('case',res)

    def test_industry(self,case,get_token):
        result = TestIndustry.reaDcase(case)
        res = Request().send(url = result['url'],
                             method=result['method'],
                             data=result['data'],
                             header = get_token)

        logger.info("{}{}{},".format(result['number'], result['title'], res))

        assert res['code']==200

        Case_operation().write_result(xulie=0,res = result['title'])


    res_jc = Case_operation().get_case(case_path,'zcyjc')

    @pytest.mark.parametrize('case',res_jc)

    def test_jc(self,case,get_token):
        result = TestIndustry.reaDcase(case)
        res = Request().send(url = result['url'],
                             method=result['method'],
                             data=result['data'],
                             header = get_token)

        logger.info("{}{}{},".format(result['number'], result['title'], res))

        assert res['code']==200

        Case_operation().write_result(xulie=1,res = result['title'])


    delete_jc = Case_operation().get_case(case_path,'deletejc')

    @pytest.mark.parametrize('case',delete_jc)
    def test_delete(self, case, get_token,get_industryids):
        result = TestIndustry.reaDcase(case)
        res = Request().send(url=result['url']+get_industryids,
                             method=result['method'],
                             data=result['data'],
                             header=get_token)

        logger.info("{}{}{},".format(result['number'], result['title'], res))

        assert res['code'] == 200

        Case_operation().write_result(xulie=2,res = result['title'])






