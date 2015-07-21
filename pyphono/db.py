class DataBase:
    """
    Basic database class
    """
    def __init__(self, data_file):
        self.mapping = {}
        self.buildMap(data_file)

    def buildMap(self, data_file):
        with open(data_file, 'r') as reader:
            for line in reader:
                line = line.strip()
                word, num, *pinyin = line.split()
                self.mapping[word] = pinyin

    def findAWord(self, word, multi_pinyin=False):
        if multi_pinyin:
            return self.mapping[word]
        else:
            return self.mapping[word][0]

