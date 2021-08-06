import sys
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
import os
import shutil
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '5.0.0'
COMPONENT = 'about'
LOCALE = 'de'
Config_files = 'only_online.yml'

class Test_da:
    def restart_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        if not os.path.exists(sub_path):
             os.makedirs(sub_path)
        else:
            shutil.rmtree(sub_path)
            os.makedirs(sub_path)

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
    def setup_class(self):
        print("------->cache:online mode")
        self.prepare_sub_path(self,'log')
        I18N.add_config_file('only_online.yml')

    def teardown_class(self):
        print("------->teardown_cache:online mode")

    def setup(self):
        print("------->setup_method")


    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.cache1
    def test_l1(self):
        print("cache expired and update")
        I18N.set_current_locale(LOCALE)
        current = I18N.get_current_locale()
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        print(tran1)
        assert tran1 == "test__de_value"
        os.system(r'E:\test_pythoncode\online_bat\ModifyString_de.bat')

        time.sleep(35)
        tran2 = translation.get_string("about", "about.message")
        assert tran2 == "test__de_value"
        time.sleep(10)
        tran3 = translation.get_string("about", "about.message")
        assert tran3 == "test__de_value_change"
        os.system(r'E:\test_pythoncode\online_bat\RevertString_de.bat')

    # @pytest.mark.cache1
    # def test_l13(self):
    #     print("cache expired and update")
    #     I18N.set_current_locale(LOCALE)
    #     current = I18N.get_current_locale()
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     time.sleep(5)
    #     tran1 = translation.get_string("about","about.message")
    #     print(tran1)
    #     time.sleep(3)
    #     tran1 = translation.get_string("about", "about.message")
    #     print(tran1)
    #     #assert tran1 == "test__de_value"
    #     #os.system(r'E:\test_pythoncode\online_bat\ModifyString_de.bat')

    @pytest.mark.cache1
    def test_l2(self):
        print("cache not expired and update")
        I18N.set_current_locale("fr")
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        #print(tran1)
        assert tran1 =="test_fr_value"
        os.system(r'E:\test_pythoncode\online_bat\ModifyString_fr.bat')
        time.sleep(15)
        tran2 = translation.get_string("about", "about.message")
        #print(tran2)
        assert tran2 =="test_fr_value"
        time.sleep(10)
        tran3 = translation.get_string("about", "about.message")
        #print(tran3)
        assert tran3 =="test_fr_value"
        os.system(r'E:\test_pythoncode\online_bat\RevertString_fr.bat')

    @pytest.mark.cache1
    def test_l3(self):
        print("cache expired and string not update")
        I18N.set_current_locale("ja")
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        assert tran1 =="test ja key"
        time.sleep(35)
        tran2 = translation.get_string("about", "about.message")
        assert tran2 =="test ja key"
        time.sleep(10)
        tran3 = translation.get_string("about", "about.message")
        assert tran3 =="test ja key"

    @pytest.mark.cache2
    def test_l4(self):
        print("cache expired and update locale")
        I18N.set_current_locale("pl")
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        assert tran1 == "Your application description page."
        os.system(r'E:\test_pythoncode\online_bat\ModifyString_pl.bat')
        time.sleep(35)
        tran3 = translation.get_string("about", "about.message")
        assert tran3 == "Your application description page."
        time.sleep(10)
        tran4 = translation.get_string("about", "about.message")
        #assert tran4 == "test_pl_value_change"
        print("translation %s" % tran4)
        time.sleep(10)
        tran5 = translation.get_string("about", "about.message")
        #assert tran4 == "test_pl_value_change"
        print("translation5 %s" % tran5)
        #os.system(r'E:\test_pythoncode\online_bat\RevertString_pl.bat')


    @pytest.mark.cache2
    def test_l6(self):
        print("cache expired and update locale")
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.addkey",locale= "de")
        print("translation %s" % tran1)
        #os.system(r'E:\python_client\test_pythoncode\online_bat\addkey_en.bat')
        os.system(r'E:\python_client\test_pythoncode\online_bat\addkey_en.bat')
        os.system(r'E:\python_client\test_pythoncode\online_bat\addkey_de.bat')
        time.sleep(40)
        tran2 = translation.get_string("about", "about.addkey",locale= "de")
        tran3 = translation.get_string("about", "about.addkey", locale="en")
        print("translationen 1 %s" % tran3)
        print("translationde 1 %s" % tran2)
        time.sleep(3)
        tran3 = translation.get_string("about", "about.addkey",locale= "de")
        print("translationde 2 %s" % tran3)
        tran3 = translation.get_string("about", "about.addkey", locale="en")
        print("translationen 2 %s" % tran3)
        # time.sleep(31)
        # tran4 = translation.get_string("about", "about.addkey",locale= "de")
        # print("translationde 3 %s" % tran4)
        # time.sleep(3)
        # tran5 = translation.get_string("about", "about.addkey",locale= "en")
        # print("translation en %s" % tran5)
        #os.system(r'E:\python_client\test_pythoncode\online_bat\addkey_de.bat')
        #assert tran3 == "Your application description page."
        # time.sleep(3)
        # tran3 = translation.get_string("about", "about.addkey")
        # print("translation %s" % tran3)
        # time.sleep(30)
        # tran4 = translation.get_string("about", "about.addkey")
        # print("translation %s" % tran4)
        # time.sleep(3)
        # tran5 = translation.get_string("about", "about.addkey")
        # print("translation %s" % tran5)
        # tran4 = translation.get_string("about", "about.message")
        # #assert tran4 == "test_pl_value_change"
        # print("translation %s" % tran4)
        # time.sleep(10)
        # tran5 = translation.get_string("about", "about.message")
        # #assert tran4 == "test_pl_value_change"
        # print("translation5 %s" % tran5)


    # def test_l41(self):
    #     print("cache expired and update locale")
    #     self.prepare_sub_path('log')
    #     self.prepare_sub_path('singleton')
    #     I18N.add_config_file('only_online.yml')
    #     I18N.set_current_locale("pl")
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     tran1 = translation.get_string("about","about.message")
    #     print(tran1)
    @pytest.mark.cache2
    def test_l5(self):
        print("cache expired and update conpomtent -- bug 1019")
        I18N.set_current_locale("fr")
        # tran = I18N.get_release(PRODUCT, VERSION).get_translation().get_string("aadcomponent","about.message")
        # print(tran)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        # tran1 = translation.get_string("about","about.message")
        # print(tran1)
        #assert tran1 == "about.message"
        tran2 = translation.get_string("aadcomponent","about.message")
        #assert tran2 == "about.message"
        print(tran2)
        # tran3 = translation.get_string("contact","contact.message")
        # #assert tran2 == "about.message"
        # print(tran3)
        # os.system(r'E:\python_client\test_pythoncode\online_bat\Addcomponenten.bat')
        # os.system(r'E:\test_pythoncode\online_bat\Addcomponent.bat')
        os.system(r'E:\python_client\test_pythoncode\online_bat\Addcomponenten.bat')
        os.system(r'E:\python_client\test_pythoncode\online_bat\Addcomponent.bat')
        time.sleep(15)
        tran2 = translation.get_string("addcomponent", "about.message")
        assert tran2 == "about.message"
        time.sleep(10)
        tran3 = translation.get_string("addcomponent", "about.message")
        print(tran3)
        time.sleep(10)
        tran3 = translation.get_string("addcomponent", "about.message")
        print(tran3)
        #assert tran3 =="test_value_change123"
        time.sleep(10)
        tran4 = translation.get_string("addcomponent", "about.message")
        assert tran4 == "test_value_change123"



    ##test
    # def test_l6(self):
    #     print("cache expired and update conpomtent")
    #     self.prepare_sub_path('log')
    #     self.prepare_sub_path('singleton')
    #     I18N.add_config_file('only_online.yml')
    #     I18N.set_current_locale("fr")
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     tran1 = translation.get_string("about","about.message")
    #     print(tran1)
    #     time.sleep(10)
    #     tran2 = translation.get_string("addcomxponent", "about.message")
    #     print(tran2)
    #     time.sleep(35)
    #     tran3= translation.get_string("about", "about.message")
    #     print(tran3)
    #     time.sleep(10)
    #     tran5 = translation.get_string("addcompxonent", "about.message")
    #     print(tran5)
    #     time.sleep(10)
    #     tran4 = translation.get_string("contact", "about.message")
    #     print(tran4)
    #     time.sleep(10)
    #     tran6 = translation.get_string("addcompxonent", "about.message")
    #     print(tran6)
    # def test_l6(self):
    #     print("cache expired and update conpomtent")
    #     self.prepare_sub_path('log')
    #     self.prepare_sub_path('singleton')
    #     I18N.add_config_file('only_online.yml')
    #     I18N.set_current_locale("fr")
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     tran1 = translation.get_string("addcomponent","about.message")
    #     print(tran1)