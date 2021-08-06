from sgtn_client import I18n,Release,Config,Translation
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

    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("-------->teardown_method")

    def test_l1(self):
        print("test local 1")
        self.prepare_sub_path('log')
        self.prepare_sub_path('singleton')

        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        current = I18n.get_current_locale()
        print(current)
        #I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        conf =self.rel.get_config()
        xx = conf.get_info()
        print(xx)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        print(tran1)
    def test_l2(self):
        print("test local 2")
        I18n.add_config_file('only_online.yml')
        # I18n.set_current_locale(LOCALE)
        #current = I18n.get_current_locale()
        #print(current)
        #I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        data1 = translation1.get_locale_strings("de")
        print(data1)
        data2 = translation1.get_locale_supported("en-US")
        print(data2)
    def test_l3(self):
        print("test local 3")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.", locale = "ja")
        print(trans1)
    def test_l4(self):
        print("test local 4")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.")
        print(trans1)
    def test_l5(self):
        print("test local 5")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page")
        print(trans1)
    def test_l6(self):
        print("test local 6")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page")
        print(trans1)
    def test_l7(self):
        print("test local 7")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        #trans1 = translation1.get_string("about", "about.message", format_items = ["11","22"])
        trans1 = translation1.get_string("about", "about.message", x= "1", y= "2")
        print(trans1)

    def test_l8(self):
        print("test local 8")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        #trans1 = translation1.get_string("about", "about.message", format_items = ["11","22"])
        #trans1 = translation1.get_string("abo", "about.message", x= "1", y= "2")
        #trans1 = translation1.get_string("abo", None)
        trans1 = translation1.get_string(None, "1",source = "About")
        print(trans1)

    def test_l9(self):
        print("test local 9")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        #trans1 = translation1.get_string("about", "about.message", format_items = ["11","22"])
        #trans1 = translation1.get_string("abo", "about.message", x= "1", y= "2")
        #trans1 = translation1.get_string("abo", None)
        trans1 = translation1.get_string(None, "1",source = "About")
        print(trans1)

    def test_l10(self):
        print("test local 10")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about", "about.message", format_items = ["11","22"])
        # trans1 = translation1.get_string("abo", "about.message", x= "1", y= "2")
        # trans1 = translation1.get_string("abo", None)
        trans1 = translation1.get_string(None, "1", source="About")
        print(trans1)

    def test_l11(self):
        print("test local 11")
        I18n.add_config_file('only_online.yml')
        I18n.set_current_locale(LOCALE)
        self.rel = I18n.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about", "about.message", format_items = ["11","22"])
        # trans1 = translation1.get_string("abo", "about.message", x= "1", y= "2")
        # trans1 = translation1.get_string("abo", None)
        trans1 = translation1.get_string(None, "about.message")
        print(trans1)



