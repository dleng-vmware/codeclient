import sys
import os
#print(sys.path)
#sys.path.insert(0, 'E:\\python_client' )
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '1.0'
COMPONENT = 'about'
LOCALE = 'fr'
Config_files = 'only_online.yml'

class Test_da4:

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
        print("------>only online module support")
        self.prepare_sub_path(self,'log')
        outside_config = {"product":"PythonClient","online_service_url": "https://localhost:8090"}
        I18N.add_config_file('only_online.yml',outside_config)

    def teardown_class(self):
        print("------->complete")

    def setup(self):
        print("------->setup_method")
        # self.prepare_sub_path('log')
        # I18N.add_config_file('only_online.yml')

    #I18N.add_config_file('only_online.yml')

    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.ci1
    def test_l1(self):
        print("online:component and key")
        print(sys.path)
        #I18N.set_current_locale(LOCALE)
        #current = I18N.get_current_locale()
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        #conf =self.rel.get_config()
        translation = self.rel.get_translation()
        #tran1 = translation.get_string("about","about.message")
        #print(tran1)
        #assert tran1 == "test fr key"
        # tran1 = translation.get_string("about", "about.message", locale = 'en')
        # print(tran1)
        tran2 = translation.get_string("about", "about.message", locale = 'ja')
        assert tran2 == "test ja key"
    #
    @pytest.mark.ci1
    def test_l2(self):
        print("online:nocomponent and key")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("","about.message")
        assert tran1 == "about.message"
        tran2 = translation.get_string("123","about.message")
        assert tran2 == "about.message"
        tran3 = translation.get_string(None,"about.message")
        assert tran3 == "about.message"

    @pytest.mark.ci1
    def test_l3(self):
        print("online:component and nokey")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about", "")
        assert tran1 == ""
        tran2 = translation.get_string("about", "123")
        assert tran2 == "123"
        tran3 = translation.get_string("about", None)
        assert tran3 == None

    @pytest.mark.ci1
    def test_l4(self):
        print("online:nocomponent and nokey")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("", "")
        assert tran1 == ""
        tran2 = translation.get_string("456", "123")
        assert tran2 == "123"
        tran3 = translation.get_string(None, None)
        assert tran3 == None
        # data1 = translation1.get_locale_strings("de")
        # print(data1)
        # data2 = translation1.get_locale_supported("en-US")
        # print(data2)

    @pytest.mark.ci1
    def test_l5(self):
        print("online:component and key and source and locale ")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.", locale = "ja")
        #"Your application description page."
        assert trans1 == "test ja key"

    @pytest.mark.ci1
    def test_l6(self):
        print("online:component and key and source")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.")
        assert trans1 == "test fr key"

    @pytest.mark.ci1
    def test_l7(self):
        print("online:component and key and locale")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",locale = "zh-Hans-CN")
        assert trans1 == "صفحة وصف التطبيق الخاص بك."

    @pytest.mark.ci1
    def test_l8(self):
        print("online:component and key and nolocale or nosource------bug: 1036")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = '123')
        assert trans1 == "123"
        trans2 = translation1.get_string("about","about.message",source = None)
        assert trans2 == "test fr key"
        # trans3 = translation1.get_string("about","about.message",locale = "da")
        # assert trans3 == "Your application description page."
        trans4 = translation1.get_string("about","about.message",locale = "da")
        assert trans4 == "test fr key"
        trans5 = translation1.get_string("1","about.message",source = "123")
        assert trans5 == "about.message"

    @pytest.mark.ci1
    def test_l9(self):
        print("online:format_items -- bug789")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        try:
            trans1 = translation1.get_string("about", "about.test", format_items = ["11","22"])
        except IndexError as Argument:
            print("error:%s" % Argument)
            assert str(Argument) == "tuple index out of range"
        else:
            raise AssertionError

    @pytest.mark.ci1
    def test_l10(self):
        print("online:format_items")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about", "about.test","1","2")
        #  print(trans1)
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
        trans1 = translation1.get_string("about", "about.test", format_items=None)
        assert trans1 == "test fr the {1} to {0} and {2}"
        # trans1 = translation1.get_string("about", "about.test", format_items = [None])
        # print(trans1)
        # trans1 = translation1.get_string("about", "about.test", format_items = None)
        # print(trans1)

    # def test_l11(self):
    #     print("online:format_items")
    #     I18N.set_current_locale(LOCALE)
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation1 = self.rel.get_translation()
    #     trans1 = translation1.get_string("about", "about.test", format_items=None)
    #     print(trans1)
    @pytest.mark.ci2
    def test_l11(self):
        print("online:get_locale_strings")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans19 = translation1.get_string("about", "about.message")
        trans1 = translation1.get_locale_strings(LOCALE, False)
        data = {
                "about": {
                        "about.description": "Utilisez cette zone pour fournir des informations supplémentaires",
                        "about.message": "test fr key",
                        "about.title": "Sur",
                        "about.test": "test fr the {1} to {0} and {2}"
                        }
                }
        #print(trans1)
        assert trans1 == data
        result = "about" in trans1.keys()
        assert result == True
        trans1 = translation1.get_locale_strings("de", False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("da", False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("zh-Hans", False)
        result = "about" in trans1.keys()
        assert result == False
        # trans1 = translation1.get_locale_strings(None)
        # print(trans1)

    @pytest.mark.ci1
    def test_l12(self):
        print("online:get_locale_supported")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        data1 = translation1.get_locale_supported("da")
        assert data1 == "da"
        data1 = translation1.get_locale_supported("zh-Hans")
        assert data1 == "zh-Hans"
        data1 = translation1.get_locale_supported("fr-FR")
        assert data1 == "fr"
        data1 = translation1.get_locale_supported("fr-CA")
        assert data1 == "fr"
        data1 = translation1.get_locale_supported("en")
        assert data1 == "en"
        data1 = translation1.get_locale_supported("123")
        assert data1 == "123"
        data1 = translation1.get_locale_supported("")
        assert data1 == ""
        # data1 = translation1.get_locale_supported(None)
        # print(data1)

    # def test_l21(self):
    #     print("the key only in online")
    #     I18N.set_current_locale(LOCALE)
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation = self.rel.get_translation()
    #     tran1 = translation.get_string("intest","intest.online")
    #     print(tran1)
    #     assert tran1 == "Contact1 fr online"

    @pytest.mark.ci1
    def test_l13(self):
        print("online:component and key and nolocale or nosource------bug: 1165")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message")
        #assert trans1 == "123"
        print(trans1)
        trans2 = translation1.get_string("contact","about.message")
        #assert trans2 == "test fr key"
        print(trans2)
        # trans3 = translation1.get_string("about","about.message",locale = "da")
        # assert trans3 == "Your application description page."





