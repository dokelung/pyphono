import unittest
from db import DataBase

class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = DataBase('../data/zhuyin.tbl')
        self.testword = '丁'
        self.testpinyin = ['ㄉㄧㄥ', 'ㄓㄥ'] 

    def test_corresponding(self):
        self.assertEqual(self.db.mapping[self.testword], self.testpinyin)

    def test_word_count(self):
        self.assertEqual(len(self.db.mapping), 13053)

    def test_find_word(self):
        pinyin = self.db.findAWord(self.testword)
        self.assertEqual(pinyin, self.testpinyin[0])

        pinyin = self.db.findAWord(self.testword, multi_pinyin=True)
        self.assertEqual(pinyin, self.testpinyin)

if __name__ == '__main__':
    unittest.main()
