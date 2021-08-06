import sys
#sys.path.append('../../')
#from sgtn_client import I18N,Release,Config,Translation
from sgtnclient import I18N
#sys.path.append('../..')
#from sgtn_client import I18N,Release,Config,Translation
import os
import time
import json
import pytest

PRODUCT = 'PythonClient'
VERSION = '3'
COMPONENT = 'about'
LOCALE = 'fr'
Config_files = 'sample_offline_remote.yml'

class Test_da3:
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
        self.prepare_sub_path(self, 'log')
        I18N.add_config_file('sample_offline_remote.yml')

    def teardown_class(self):
        print("------->complete")

    def setup(self):
        print("------->setup_method")
    def teardown(self):
        print("-------->teardown_method")

    @pytest.mark.ci1
    def test_l1(self):
        print("offline_remote:add_configlfile")
        I18N.set_current_locale('fr')
        currentlocale = I18N.get_current_locale()
        print(currentlocale)
        assert currentlocale == 'fr'
        self.rel = I18N.get_release(PRODUCT, VERSION)
        conf =self.rel.get_config()
        config_data = conf.get_config_data()
        config_info = conf.get_info()
        #self.show('config', 'info', self.dict2string(config_info))
        data2 = {
  "product": "PythonClient",
  "version": "3",
  "remote": None ,
  "source_locale": "en-US",
  "default_locale": "de",
  "local": "http://127.0.0.1:8094/l10ntest/PythonClient/3"
}
        assert config_info == data2

    @pytest.mark.ci1
    def test_l2(self):
        print("offline_remote:component and key")
        I18N.set_current_locale(LOCALE)
        current = I18N.get_current_locale()
        #I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        conf =self.rel.get_config()
        translation = self.rel.get_translation()
        tran1 = translation.get_string("about","about.message", locale ="fr")
        assert tran1 == "test fr 12 343343456 key"
        tran2 = translation.get_string("about", "about.message", locale = 'ja')
        assert tran2 == "test ja key"

    @pytest.mark.ci1
    def test_l3(self):
        print("offline_remote:component and key and locale")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        #trans3 = translation1.get_string("about", "about.message", locale="zh-Hans")
        #print(trans3)
        trans1 = translation1.get_string("about","about.message",locale = "zh-Hans-CN")
        assert trans1 == "صفحة وصف التطبيق الخاص بك."

    @pytest.mark.ci1
    def test_l4(self):
        print("offline_remote:component and key and source and locale")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.", locale = "ja")
        assert trans1 == "test ja key"

    @pytest.mark.ci1
    def test_l5(self):
        print("offline_remote:nocomponent and key")
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
    def test_l6(self):
        print("offline_remote:component and nokey")
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
    def test_l7(self):
        print("offline_remote:nocomponent and nokey")
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
    def test_l8(self):
        print("offline_remote:component and key and source")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "Your application description page.")
        assert trans1 == "test fr 12 343343456 key"

    @pytest.mark.ci1
    def test_l9(self):
        print("offline_remote:component and key and nolocale or nosource")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message",source = "123")
        assert trans1 == "123"
        trans2 = translation1.get_string("about","about.message",source = None)
        assert trans2 == "test fr 12 343343456 key"
        trans3 = translation1.get_string("about","about.message",locale = "da")
        assert trans3 == "test de key"
        trans4 = translation1.get_string("about","about.message",locale = None)
        assert trans4 == "test fr 12 343343456 key"
        trans5 = translation1.get_string("1","about.message",source = "123")
        assert trans5 == "about.message"

    @pytest.mark.ci1
    def test_l10(self):
        print("offline_remote:format_items -- bug 789")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        try:
            trans1 = translation1.get_string("about", "about.test", format_items=["11", "22"])
        except IndexError as Argument:
            print("error:%s" % Argument)
            assert str(Argument) == "tuple index out of range"
        else:
            raise AssertionError

    @pytest.mark.ci1
    def test_l11(self):
        print("offline_remote:format_items")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans2 = translation1.get_string("contact","contact.title", format_items={'x':'11', 'y' : '22', 'z':'33'}, locale = 'ko')
        assert trans2 == "연락처change 22 add 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33"], locale= 'fr')
        assert trans1 == "test fr the 22 to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", locale= 'ja')
        assert trans1 == "test the {1} to {0} and {2}"
        trans2 = translation1.get_string("contact", "contact.title", format_items={'x': '11', 'y': '22', 'z': '33'},locale='ko')
        assert trans2 == "연락처change 22 add 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11","22","33","44"])
        assert trans1 == "test fr the 22 to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = ["11",None,"33"])
        assert trans1 == "test fr the None to 11 and 33"
        trans1 = translation1.get_string("about", "about.test", format_items = None)
        assert trans1 == "test fr the {1} to {0} and {2}"

    @pytest.mark.ci2
    def test_l12(self):
        print("offline_remote:get_locale_strings")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        #translation1 = self.rel.get_translation()
        translation1 = self.rel.get_translation()
        trans19 = translation1.get_string("about", "about.message")
        trans1 = translation1.get_locale_strings(LOCALE, False)
        # data = {
        #   "about": {
        #     "about.description": "Utilisez cette zone pour fournir des informations supplémentaires",
        #     "about.message": "test fr 12 343343456 key",
        #     "about.title": "Sur",
        #     "about.test": "test fr the {1} to {0} and {2}"
        #   },
        #   "contact": {
        #     "contact.marketing": "マーケティング：",
        #     "contact.applicationname": "Singleton サンプル Web アプリケーション",
        #     "contact.address": "1つのマイクロソフトの方法 <br/> レドモンド、WA 98052-6399 <br/> < 略称タイトル = \"電話\" > P: </abbr> 425.555.0100",
        #     "contact.support": "サポート：",
        #     "contact.message": "お客様の連絡先ページ。",
        #     "contact.title": "連絡先",
        #     "contact.test": "change ja {0}"
        #   },
        #   "common": {}
        # }
        print(self.dict2string(trans1))
        #assert trans1 == data
        trans1 = translation1.get_locale_strings("da",False)
        result = "about" in trans1.keys()
        assert result == False
        trans1 = translation1.get_locale_strings("zh-Hans", False)
        result = "about" in trans1.keys()
        assert result == False
#        trans1 = translation1.get_locale_strings(None)
#        print(trans1)
    @pytest.mark.ci1
    def test_l13(self):
        print("offline_remote:get_locale_supported")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        data1 = translation1.get_locale_supported("da")
        assert data1 == "da"
        data1 = translation1.get_locale_supported("zh-Hans")
        assert data1 == "zh-Hans"
        data1 = translation1.get_locale_supported("fr-FR")
        assert data1 == "fr"
        data1 = translation1.get_locale_supported("en")
        assert data1 == "en"
        data1 = translation1.get_locale_supported("123")
        assert data1 == "123"
        data1 = translation1.get_locale_supported("")
        assert data1 == ""
#        data1 = translation1.get_locale_supported(None)
#        print(data1)


    @pytest.mark.ci1
    def test_l14(self):
        print("offline_remote:component and key and nolocale or nosource------bug: 1165")
        I18N.set_current_locale(LOCALE)
        self.rel = I18N.get_release(PRODUCT, VERSION)
        translation1 = self.rel.get_translation()
        trans1 = translation1.get_string("about","about.message")
        #assert trans1 == "123"
        print(trans1)
        trans2 = translation1.get_string("contact","about.message")
        #assert trans2 == "test fr key"
        print(trans2)








