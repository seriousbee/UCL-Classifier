from Feature import *

class FeatureFactory:
    def __init__(self, sentence):
        self.__sentence = sentence

    def produce_features(self):
        features = []
        features.append(self.feature_length())

    def feature_length(self):
        f = Feature()
        f.name = "Length of string"
        f.value = len(self.__sentence)
        return f