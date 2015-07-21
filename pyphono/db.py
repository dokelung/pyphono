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

    def pinAWord(self, word, multi_pinyin=False):
        if word not in self.mapping:
            return False
        if multi_pinyin:
            return self.mapping[word]
        else:
            return self.mapping[word][0]

    def pinASentence(self, sentence, multi_pinin=False):
        results = []
        for word in sentence:
            pinin = self.pinAWord(word, multi_pinin)
            if pinin:
                results.append(pinin)
            else:
                results.append(word)
        return results
            

