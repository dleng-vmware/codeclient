import sys
#sys.path.append('../../')
from sgtnclient import I18N
#from sgtnclient import sgtn_util
#from sgtn_client import I18N,Release,Config,Translation
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
import os
import shutil
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '2.0.0'
COMPONENT = 'about'
LOCALE = 'fr'
Config_files = 'sample_offline_disk.yml'


# @pytest.mark.ci1
# def test_l7(self):
#     print("online:component and key and locale")
#     I18N.set_current_locale(LOCALE)
#     self.rel = I18N.get_release(PRODUCT, VERSION)
#     translation1 = self.rel.get_translation()
#     trans1 = translation1.get_string("about","about.message",locale = "ar")
#     assert trans1 == "صفحة وصف التطبيق الخاص بك."

class Test_da2:
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
        print("------>only offline module support")
        self.prepare_sub_path(self,'log')
        outside_config = {"product": "PythonClient"}
        I18N.add_config_file('sample_offline_disk.yml',outside_config)

    def teardown_class(self):
        print("------->complete")

    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.ci1
    def test_l1_1(self):
        print("offline:add_configlfile")
        I18N.set_current_locale('fr')
        currentlocale = I18N.get_current_locale()
        print(currentlocale)
        assert currentlocale == 'fr'
        self.rel = I18N.get_release(PRODUCT, VERSION)
        conf =self.rel.get_config()
        config_data = conf.get_config_data()
        config_info = conf.get_info()
        data2 = {
                    "product": "PythonClient",
                    "version": "2.0.0",
                    "remote": None,
                    "local": "d:/l10ntest/PythonClient/2.0.0"
                }
        #assert config_info ==data2
        self.show('config', 'info', self.dict2string(config_info))

    @pytest.mark.ci1
    def test_l1(self):
        print ("offline:component and key")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message")
        assert tran1 == "test fr offline key"
        # trans1 = translation.get_locale_strings("fr")
        # print(trans1)

    @pytest.mark.ci1
    def test_l2(self):
        print("offline:nocomponent and key")
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
        print("offline:component and nokey")
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
        print("offline:nocomponent and nokey")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation = self.rel.get_translation()
        tran1 = translation.get_string("", "")
        assert tran1 == ""
        tran2 = translation.get_string("456", "123")
        assert tran2 == "123"
        tran3 = translation.get_string(None, None)
        assert tran3 == None

    @pytest.mark.ci1
    def test_l5(self):
        print("offline:component and key and source and locale ")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about", "about.message", source="Your application description page.", locale = "ja")
        assert trans1 == "test ja  offline key"
    @pytest.mark.ci1
    def test_l6(self):
        print("offline:component and key and source")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source="Your application description page.")
        # trans1 = translation1.get_string("about","about.message",source = "test de key12")
        assert trans1 == "test fr offline key"

    @pytest.mark.ci1
    def test_l7(self):
        print("offline:component and key and locale")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans2 = translation1.get_string("about","about.message",locale = "zh-Hans-CN")
        print(trans2)
        assert trans2 == "应用程序说明页。"
        trans1 = translation1.get_string("about","about.message",locale = "ar")
        assert trans1 == "صفحة وصف التطبيق الخاص بك."

    @pytest.mark.bug
    def test_l8(self):
        print("offline:component and key and nolocale or nosource__bug1193")
        I18N.set_current_locale(LOCALE)
        #I18N.set_current_locale("ja")
        #xx = I18N.get_current_locale()
        #print(xx)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about","about.message")
        # assert trans1 == "123"
        trans2 = translation1.get_string("about","about.message",source = None)
        assert trans2 == "test fr offline key"
        trans3 = translation1.get_string("about","about.message",locale = "da")
        assert trans3 == "test de key"
        trans4 = translation1.get_string("about","about.message",locale = None)
        assert trans4 == "test fr offline key"
        trans5 = translation1.get_string("1","about.message",source = "123")
        assert trans5 == "about.message"

    @pytest.mark.ci1
    def test_l9(self):
        print("offline:format_items index out of range --bug 789")
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
        print("offline:format_items")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        # trans1 = translation1.get_string("about", "about.test", x= "d", y= "x")
        # assert trans1 == "test fr the {1} to {0} and {2}"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33"])
        assert trans1 == "test fr the 22 to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33","44"])
        assert trans1 == "test fr the 22 to 11 and 33"
        trans2 = translation1.get_string("contact", "contact.title", format_items={'x':'11', 'y' : '22', 'z':'33'}, locale = 'ko')
        assert trans2 == "연락처change 22 add 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11",None,"33"])
        assert trans1 == "test fr the None to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = None)
        assert trans1 == "test fr the {1} to {0} and {2}"

    ####get strings from cache
    @pytest.mark.ci2
    def test_l11(self):
        print("offline:get_locale_strings")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans19 = translation1.get_string("about", "about.message", locale="ar")
        trans1 = translation1.get_locale_strings("ar", False)
        data1 = {
                "about": {
                    "about.message": "صفحة وصف التطبيق الخاص بك.",
                    "about.title": "حول",
                    "about.description": "استخدم هذه المنطقة لتوفير معلومات إضافية"
                    }
                }
        assert trans1 == data1
        # trans2 = translation1.get_locale_strings("de", False)
        # assert trans2 == {}
        # trans3 = translation1.get_locale_strings("da", False)
        # assert trans3 == {}

    @pytest.mark.ci1
    def test_l12(self):
        print("offline:get_locale_supported")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        data1 = translation1.get_locale_supported("da")
        assert data1 == "da"
        data1 = translation1.get_locale_supported("zh-Hans")
        assert data1 == "zh-Hans"
        data1 = translation1.get_locale_supported("fr-CA")
        assert data1 == "fr"
        data1 = translation1.get_locale_supported("en")
        assert data1 == "en"
        data1 = translation1.get_locale_supported("123")
        assert data1 == "123"
        data1 = translation1.get_locale_supported("zh-tw")
        assert data1 == "zh-Hant"
#        data1 = translation1.get_locale_supported(None)
#        print(data1)
    #### use default.yml
    # def test_l14(self):
    #     print("offline:component and key and source and default locale ")
    #     I18N.add_config_file('sample_offline_disk_default.yml')
    #     I18N.set_current_locale(LOCALE)
    #     self.rel = I18N.get_release(PRODUCT, VERSION)
    #     translation1 = self.rel.get_translation()
    #     #trans1 = translation1.get_string("about","about.message",source = "Your application description page.", locale = "ja")
    #     #offline mode:在message_en-US中key"about.message"对应的value是"Your application description page."
    #     trans1 = translation1.get_string("about", "about.message", source="234", locale = "da")
    #     assert trans1 == "test de key"

    @pytest.mark.ci1
    def test_l13(self):
        print("offline:component and key and nolocale or nosource------bug: 1165")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message")
        #assert trans1 == "123"
        print(trans1)
        trans2 = translation1.get_string("contact","about.message",locale = "en")
        #assert trans2 == "test fr key"
        print(trans2)






