import nltk

__all__ = ["identify_words"]

class WordSplitter:
    def __init__(self):
        pass


def identify_words(sentence):
    words = nltk.word_tokenize(sentence)
    result = []
    for word in words:
        if word[0].isalpha():
            result.append(word.lower())
    return result
