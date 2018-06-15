from Feature import *

class FeatureFactory:

    def __init__(self, sentence, features):
        self.__sentence = sentence
        self.features = features

    @classmethod
    def new_expression(self, sentence):
        self(sentence, [])

    @classmethod
    def updating_features(self, expression):
        self.__sentence = expression.text
        self.features = expression.features

    def produce_features(self):
        self.features.append(self.feature_length())

    def feature_length(self):
        f = Feature()
        f.name = "Length of string"
        f.value = len(self.__sentence)
        return f

    def vocabulary_similarity():


    #clusters is an array of clusters
    def calculate_relative(self, clusters):
        #remove relative ones if exist
        #calculate relative
        pass