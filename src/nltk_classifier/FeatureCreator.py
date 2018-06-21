from nltk_classifier.Feature import *
__all__ = ["FeatureCreator"]


class FeatureCreator:

    def __init__(self, clusters, expression):
        self.clusters = clusters
        self.expression = expression
        self.features = {}

    def produce_features(self):
        self.feature_length()
        self.vocabulary_similarity()
        self.expression.features = self.features
        return self.expression

    def feature_length(self):
        f = Feature()
        f.name = "Length of string"
        f.value = len(self.expression.text)
        self.features[f.name] = f

    def vocabulary_similarity(self):
        for cluster in self.clusters:
            f = Feature()
            f.name = "Single word similarity score for cluster" + cluster.name
            #calculate the value
            f.value = 0
            self.features[f.name] = f

    # TODO: create a hashtable for individual words without stop words (all + without given one)
    # TODO: create a hashtable for expressions (all + without given one)
    # TODO: create a hashtable for expressions without stop expressions (all + without given one)