import unittest
from db import DataBase

class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = DataBase('../data/zhuyin.tbl')
        self.testword = '丁'
        self.testpinyin = ['ㄉㄧㄥ', 'ㄓㄥ'] 
        self.testsentence = '我愛丁丁'
        self.testsentence2 = '我愛丁丁。'
        self.testsentencepinyin = ['ㄨㄛˇ', 'ㄞˋ', 'ㄉㄧㄥ', 'ㄉㄧㄥ'] 
        self.testsentencepinyin2 = ['ㄨㄛˇ', 'ㄞˋ', 'ㄉㄧㄥ', 'ㄉㄧㄥ', '。'] 

    def test_corresponding(self):
        self.assertEqual(self.db.mapping[self.testword], self.testpinyin)

    def test_word_count(self):
        self.assertEqual(len(self.db.mapping), 13053)

    def test_pin_word(self):
        pinyin = self.db.pinAWord(self.testword)
        self.assertEqual(pinyin, self.testpinyin[0])

        pinyin = self.db.pinAWord(self.testword, multi_pinyin=True)
        self.assertEqual(pinyin, self.testpinyin)

    def test_pin_sentence(self):
        pinyin = self.db.pinASentence(self.testsentence)
        self.assertEqual(pinyin, self.testsentencepinyin)

        pinyin = self.db.pinASentence(self.testsentence2)
        self.assertEqual(pinyin, self.testsentencepinyin2)

if __name__ == '__main__':
    unittest.main()
