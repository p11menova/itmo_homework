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
        return self.__data.split()[number]


class Text:
    def __init__(self, data):
        self.__text = list(map(lambda x: Line(data=x), data))

    def text_length(self):
        return len(self.__text)

    def line_by_num(self, num):
        return self.__text[num].data

    def words_in_line(self, num):
        return self.__text[num].words

    def one_word_by_num(self, strnum, wordnum):
        return self.__text[strnum].word(wordnum)


class EditableText(Text):
    def __init__(self, data):
        super().__init__(data)
        self.TEXT = list(map(lambda x: Line(data=x), data))

    def change_str(self, num, another_str):
        self.TEXT[num] = Line(another_str)

    def change_word(self, strnum, wordnum, another_word):
        self.TEXT[strnum].data[wordnum] = another_word

    def word_position(self, word):
        return list(map(lambda x: x.data, self.TEXT)).index(word)
    @property
    def text(self):
        return '/n'.join(list(map(lambda x: x.data, self.TEXT)))
