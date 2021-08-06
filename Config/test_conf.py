from sgtnclient import I18N
import os
import time
import json
import sys
import pytest


PRODUCT = 'PythonClient'
VERSION = '1.0.0'
COMPONENT = 'about'
LOCALE = 'fr'
Config_files = 'only_online.yml'

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

    def test_l1(self):
        self.prepare_sub_path('log')
        self.prepare_sub_path('singleton')

        I18N.add_config_file('only_online.yml')
        I18N.set_current_locale(LOCALE)
        I18N.set_current_locale(LOCALE)
        rel = I18N.get_release(PRODUCT, VERSION)
        conf =rel.get_config()
        xx = conf.get_info()
        print(xx)
        yy = conf.get_config_data()
        print(yy)

    def test_l2(self):
        self.prepare_sub_path('./log')
        self.prepare_sub_path('./singleton')
        #I18N.add_config("E:\test_pythoncode\Config\only_online.yml", default_locale = "de")
        Ixx= I18N.add_config('E:\\python_client\\test_pythoncode', {'product':'PythonClient','l10n_version':'1.0.0','online_service_url': 'http://localhost:8091', 'log_path': './Config/log/', 'try_delay': 10, 'cache_expired_time': 60})
        xx = Ixx.get_info()
        print(xx)
        #I18N.add_config_file('only_online.yml')
        #I18N.add_config("E:\test_pythoncode\Config\only_online.yml","default_locale: de")
        I18N.set_current_locale(LOCALE)
        # I18N.set_current_locale(LOCALE)
        rel = I18N.get_release(PRODUCT, VERSION)
        conf = rel.get_config()
        xx = conf.get_info()
        print(xx)
        yy = conf.get_config_data()
        print(yy)
        # self.prepare_sub_path('log')
        # self.prepare_sub_path('singleton')
        #
        # I18N.add_config_file('only_online.yml')
        #
        # start = time.time()
        # I18N.set_current_locale(LOCALE)
        # I18N.set_current_locale(LOCALE)
        # current = I18N.get_current_locale()
        # print('--- current --- %s ---' % current)
        # #self.assertEqual(current, 'de')
        #
        # rel = I18N.get_release(PRODUCT, VERSION)
        # cfg = rel.get_config()
        # cfg_info = cfg.get_info()
        # self.show('config', 'info', self.dict2string(cfg_info))