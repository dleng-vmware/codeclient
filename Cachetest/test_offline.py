import sys
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
import os
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '8.0.0'
COMPONENT = 'about'
LOCALE = 'de'
Config_files = 'sample_offline_disk.yml'

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
    @pytest.mark.cache1
    def test_l1(self):
        print("test local 1")
        self.prepare_sub_path('log')
        I18N.add_config_file('sample_offline_disk.yml')
        I18N.set_current_locale('de')
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        assert tran1 == "test de key"
        os.system(r'E:\test_pythoncode\offline_bat\test.bat')
        time.sleep(35)
        tran2 = translation.get_string("about", "about.message")
        time.sleep(10)
        assert tran2 == "test de key"
        tran3 = translation.get_string("about", "about.message", locale = 'de')
        assert tran3 == "test de key"
        os.system(r'E:\test_pythoncode\offline_bat\test_re.bat')



