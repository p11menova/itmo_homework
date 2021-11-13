class Line:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def words(self):
        return len(self.__data.split())

    def word(self, number):
        if number > len(self.__data):
            raise IndexError('операция получения слова невозможна')
        return self.__data.split()[number]


class Text:
    def __init__(self, data):
        self.__text = list(map(lambda x: Line(data=x), data))

    def text_length(self):
        return len(self.__text)

    def line_by_num(self, num):
        if num > len(self.__text):
            raise IndexError('операция получения строки невозможна')
        return self.__text[num].data

    def words_in_line(self, num):
        return self.__text[num].words

    def one_word_by_num(self, strnum: int, wordnum: int):
        try:
            return self.__text[strnum].word(wordnum)
        except IndexError as e:
            print('операция получения слова про номеру невозможна:', e)


class EditableText(Text):
    def __init__(self, data):
        super().__init__(data)
        self.TEXT = list(map(lambda x: Line(data=x), data))

    def change_str(self, num, another_str):
        if num > len(self.TEXT):
            raise IndexError('операция замены строки невозможна')
        self.TEXT[num] = Line(another_str)

    def change_word(self, strnum, wordnum, another_word):
        try:
            self.TEXT[strnum].data[wordnum] = another_word
        except IndexError as e:
            print('операция замены слова невозможна: ', e)

    def word_position(self, word):
        try:
            return list(map(lambda x: x.data, self.TEXT)).index(word)
        except IndexError as e:
            print('операция получения слова в тексте невозможна: ', e)

    @property
    def text(self):
        return '/n'.join(list(map(lambda x: x.data, self.TEXT)))
