import os

import time

local_path = os.path.abspath(__file__)

project_path = os.path.dirname(os.path.dirname(local_path))

common_path = project_path+os.sep+"common"

config_path = project_path+os.sep+"config"

log_path = project_path+os.sep+"log"

report_path =project_path+os.sep+"report"

setting_path =project_path+os.sep+"setting"

case_path =project_path+os.sep+"case"

data_path =project_path+os.sep+"data"

util_path =project_path+os.sep+"util"

entup_path = project_path+os.sep+"config"+os.sep+"upladent.xlsx"

testcase_path = project_path+os.sep+"config"+os.sep+"case.xlsx"

class getPath:

    @staticmethod
    def get_common():
        return common_path

    @staticmethod
    def get_config():
        return config_path

    @staticmethod
    def get_logging():
        return log_path

    @staticmethod
    def get_report():
        return report_path

    @staticmethod
    def get_setting():
        return setting_path

    @staticmethod
    def get_case():
        return case_path

    @staticmethod
    def get_data():
        return data_path

    @staticmethod
    def get_util():
        return util_path

    @staticmethod
    def get_upent():
        return entup_path

    @staticmethod
    def get_testcase():
        return testcase_path