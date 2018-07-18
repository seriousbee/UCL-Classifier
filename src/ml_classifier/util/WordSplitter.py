import nltk
from nltk.stem import WordNetLemmatizer

__all__ = ["identify_words"]

class WordSplitter:
    def __init__(self):
        self.wordnet_lemmatizer = WordNetLemmatizer()


def identify_words(sentence):
    words = nltk.word_tokenize(sentence)
    result = []
    wordnet_lemmatizer = WordNetLemmatizer()
    for word in words:
        if word[0].isalpha():
            result.append(wordnet_lemmatizer.lemmatize(word.lower(), pos="v"))
    return result
