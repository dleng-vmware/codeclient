import sys
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
import os
import time
import json
import sys
import pytest

PRODUCT = 'PythonClient'
VERSION = '7.0.0'
COMPONENT = 'about'
LOCALE = 'de'
Config_files = 'sample_offline_remote.yml'

class Test_da:
    def prepare_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)

    def show(self, text1, text2, value):
        print('--- %s --- %s --- %s ---' % (text1, text2, value))

    def check_locale(self, trans, locale):
        fallback_locale = trans.get_locale_supported(locale)
        self.show('locale', locale, fallback_locale)

    def dict2string(self, dict):
        return json.dumps(dict, ensure_ascii=False, indent=2)

    def need_wait(self, cfg_info):
        if (cfg_info.get('local') and cfg_info.get('remote')):
            return True
        return False

    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.cache2
    def test_l1(self):
        print("test local 1")
        self.prepare_sub_path('log')
        self.prepare_sub_path('singleton')
        I18N.add_config_file('sample_offline_remote.yml')
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about", "about.message")
        print(tran1)
        # tran2 = translation.get_string("aadcomponent","about.message")
        # print(tran2)
        assert tran1 == "test de key"
        os.system(r'E:\test_pythoncode\offline_remote_bat\test.bat')
        time.sleep(35)
        tran2 = translation.get_string("about", "about.message")
        assert tran2 == "test de key"
        time.sleep(10)
        tran3 = translation.get_string("about", "about.message")
        assert tran3 == "test de key"
        os.system(r'E:\test_pythoncode\offline_remote_bat\test_re.bat')



