import nltk
from nltk.stem import SnowballStemmer
__all__ = ["identify_words", "identify_words_raw"]

class WordSplitter:
    def __init__(self):
        self.snowball_stemmer = SnowballStemmer("english")


def identify_words(sentence):
    words = nltk.word_tokenize(sentence)
    result = []
    snowball_stemmer = SnowballStemmer("english")
    for word in words:
        if word[0].isalpha():
            result.append(snowball_stemmer.stem(word.lower()))
    return result

def identify_words_raw(sentence):
    return nltk.word_tokenize(sentence)

