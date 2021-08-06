import sys
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
import os
import shutil
import time
import json
import pytest
import urllib.parse
import urllib.request

PRODUCT = 'PythonClient'
VERSION = '1.0.1'
COMPONENT = 'about'
LOCALE = 'da'
Config_files = 'only_online_default.yml'

class Test_da1:
    def prepare_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)

    def delete_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        shutil.rmtree(sub_path)

    def restart_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        if not os.path.exists(sub_path):
             os.makedirs(sub_path)
        else:
            shutil.rmtree(sub_path)
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
    def setup_class(self):
        print("------>Test default locale")
        self.prepare_sub_path(self, 'log')
        self.prepare_sub_path(self, 'singleton')

    def teardown_class(self):
        print("------->complete")
        # os.remove('E:\\python_client\\test_pythoncode\\Translation\\log\\PythonClient_1.0.0.log')
        # # file = open('E:\\python_client\\test_pythoncode\\Translation\\log\\PythonClient_1.0.0.log')
        # # file.close()
        # self.delete_sub_path(self,'log')
        # self.restart_sub_path(self,'singleton')

    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("-------->teardown_method")
    @pytest.mark.ci1
    def test_l1(self):
        print("online:test default locale")
        I18N.add_config_file('only_online_default.yml')
        self.rel = I18N.get_release(PRODUCT, VERSION)
        conf =self.rel.get_config()
        req = "http://localhost:8091/i18n/api/v2/translation/products/PythonClient/versions/1.0.1/localelist"
        response = urllib.request.urlopen(req)
        print(response.status)
        the_page = response.read()
        print(the_page.decode("unicode_escape"))
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message",locale = LOCALE)
        assert tran1 == "test de key"

    @pytest.mark.ci1
    def test_l12(self):
        print("offline:test default locale ")
        I18N.add_config_file('sample_offline_disk_default.yml')
        self.rel = I18N.get_release(PRODUCT, '2.0.1')
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about", "about.message", locale = "da")
        assert trans1 == "test de key"

    @pytest.mark.ci1
    def test_l13(self):
        print("offline_remote:test default locale ")
        I18N.add_config_file('sample_offline_remote_default.yml')
        self.rel = I18N.get_release(PRODUCT, '3.0.1')
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about", "about.message", locale ='da')
        assert trans1 == "应用程序说明页。"

    @pytest.mark.ci1
    def test_l14(self):
        print("online_localsource:test default locale ")
        I18N.add_config_file('sample_online_localsource_default.yml')
        self.rel = I18N.get_release(PRODUCT, '4.0.1')
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about", "about.message", locale = "da")
        assert trans1 == "test ja key"













