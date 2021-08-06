import sys
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
import os
import shutil
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '0.0.00.1'
COMPONENT = 'about'
LOCALE = 'fr'
Config_files = 'sample_online_localsource.yml'

class Test_da5:
    def setup_class(self):
        print("------>online with localsource")
        self.prepare_sub_path(self,'log')
        self.prepare_sub_path(self,'singleton')
        # self.restart_sub_path(self,'log')
        # self.restart_sub_path(self,'singleton')
        # time.sleep(1)
        I18N.add_config_file('sample_online_localsource.yml')
    def teardown_class(self):
        print("------->complete")
    def prepare_sub_path(self, sub):
        current_path = os.path.dirname(__file__)
        sub_path = os.path.join(current_path, sub)
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)

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

    def setup(self):
        print("------->setup_method")
        # self.restart_sub_path('log')
        # self.restart_sub_path('singleton')
        # I18N.add_config_file('sample_online_localsource.yml')

    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.ci1
    def test_l1(self):
        print("the key only in offline")
        I18N.set_current_locale(LOCALE)
        current = I18N.get_current_locale()
        print(current)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("intest","intest.offline")
        assert tran1 == "Contact1 offline"
        tran2 = translation.get_string("intest","intest.offline", locale = "ja")
        assert tran2 == "Contact1 offline"

    # @pytest.mark.citest
    # def test_l4(self):
    #     print("the key both exist in online and offline: source error")
    #     I18N.set_current_locale(LOCALE)
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     trans2 = translation.get_string("intest","intest.home", locale = "ja")
    #     # assert trans2 == "Homexxxx1"
    #     print(trans2)
    #     time.sleep(3)
    #     trans3 = translation.get_string("intest","intest.home", locale = "ja")
    #     ## assert trans3 == "Homexxxx"
    #     print(trans3)
    #
    @pytest.mark.ci1
    def test_l2(self):
        print("the key only in online")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        #tran1 = translation.get_string("intest","intest.online",source = "Contact1 online")
        tran1 = translation.get_string("intest", "intest.online")
        assert tran1 == "Contact1 fr online"

    @pytest.mark.ci1
    def test_l3(self):
        print("the key both exist in online and offline ")
        I18N.set_current_locale(LOCALE)

        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about", "about.message")
        # assert trans1 == "test fr key"
        # trans3 = translation1.get_string("about", "about.message", locale ='en')
        # assert trans3 == "Your application description page."
        tran2 = translation1.get_string("about", "about.message", locale = 'ja')
        assert tran2 == "test ja key"
        #assert trans1 == "About1 fr"



    @pytest.mark.citest
    def test_l4(self):
        print("the key both exist in online and offline: source error")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("intest","intest.about",source = "About123", locale = "ja")
        # assert trans1 == "About1"
        tran1 = translation1.get_string("intest","intest.offline",locale = "ja")
        assert tran1 == "Contact1 offline"
        trans2 = translation1.get_string("intest","intest.home", locale = "ja")
        # assert trans2 == "Homexxxx1"
        print(trans2)
        time.sleep(0.1)
        trans3 = translation1.get_string("intest","intest.home", locale = "ja")
        # assert trans3 == "Homexxxx"
        print(trans3)

    @pytest.mark.bug
    def test_l5(self):
        print("the key both exist in online and offline ")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        #trans1 = translation1.get_string("intest","intest.about",source = "About12")
        # trans1 = translation1.get_string("intest", "intest.about")
        # assert trans1 == "About1 fr"
        trans2 = translation1.get_string("intest","intest.about", source = "About1", locale = "ja")
        assert trans2 == "About1 ja"
        trans3 = translation1.get_string("intest", "intest.about", source="About1")
        assert trans3 == "About1 fr"
        trans4 = translation1.get_string("intest", "intest.about", source="About1", locale="ja")
        assert trans4 == "About1 ja"

    @pytest.mark.ci1
    def test_l6(self):
        print("the component only in offline")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("common","common.about")
        #print(trans1)
        assert trans1 == "About"

    @pytest.mark.ci1
    def test_l7(self):
        print("the component only in online")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("index","index.title")
        assert trans1 == "Home Page fr"

    @pytest.mark.ci1
    def test_l8(self):
        print("the locale only in online")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("contact","contact.support",source= "Support:", locale ="ko")
        assert trans1 == "サポート：ko"
        trans1 = translation1.get_string("contact","contact.support", locale ="ko")
        assert trans1 == "サポート：ko"

    @pytest.mark.ci1
    def test_l9(self):
        print("the locale only in online")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # data1 = translation1.get_locale_supported("ko")
        # print(data1)
        trans1 = translation1.get_string("contact","contact.support",source= "Support:", locale ="ja")
        #print(trans1)
        assert trans1 == "サポート："
        trans2 = translation1.get_string("contact","contact.support", locale ="ja")
        assert trans2 == "サポート："

    @pytest.mark.ci1
    def test_l10(self):
        print("the locale only in offline")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("contact","contact.title", locale ="pt")
        #source= "Contact",
        assert trans1 == "Contact"

    @pytest.mark.ci2
    def test_l11(self):
        print("online:get_locale_strings")
        #self.restart_sub_path('singleton')
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans19 = translation1.get_string("about", "about.message")
        print("translation 123 %s" % trans19)
        data = {
                "about": {
                    "about.description": "Utilisez cette zone pour fournir des informations supplémentaires",
                    "about.message": "test fr key",
                    "about.title": "Sur",
                    "about.test": "test fr the {1} to {0} and {2}"
                  }
                }
        trans1 = translation1.get_locale_strings(LOCALE,False)
        print(json.dumps(trans1,ensure_ascii = False, indent=2))
        assert trans1 == data
        trans1 = translation1.get_locale_strings("de",False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("da",False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("zh-Hans",False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("pt",False)
        result = "about" in trans1.keys()
        assert result == False
        #trans1 = translation1.get_locale_strings(None)
        #print(trans1)

    @pytest.mark.ci1
    def test_l12(self):
        print("online:format_items")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about", "about.test", x= "1", y= "2")
        assert trans1 == "test fr the {1} to {0} and {2}"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33"])
        assert trans1 == "test fr the 22 to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33","44"])
        assert trans1 == "test fr the 22 to 11 and 33"
        trans2 = translation1.get_string("contact", "contact.title", format_items={'x':'11', 'y' : '22', 'z':'33'}, locale = 'ko')
        assert trans2 == "연락처change 22 add 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11",None,"33"])
        assert trans1 == "test fr the None to 11 and 33"


    @pytest.mark.ci1
    def test_l13(self):
        print("online_with_local:component and key and nolocale or nosource------bug: 1165")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message")
        #assert trans1 == "123"
        print(trans1)
        trans2 = translation1.get_string("contact","about.message")
        #assert trans2 == "test fr key"
        print(trans2)