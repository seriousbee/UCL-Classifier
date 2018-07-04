from nltk_classifier.models.Feature import *
from nltk_classifier.util.WordSplitter import identify_words
__all__ = ["FeatureCreator"]


class FeatureCreator:

    def __init__(self, clusters, expression, marker_identification):
        self.clusters = clusters
        self.expression = expression
        self.features = {}
        self.marker_identification = marker_identification

    def produce_features(self):
        #self.feature_length()
        #self.vocabulary_similarity_optimised()
        #self.vocabulary_similarity_no_stopwords()
        self.markers_present()
        #self.objective_word_present()
        self.expression.features = self.features
        return self.expression

    def feature_length(self):
        f = Feature()
        f.name = "Length of string"
        f.value = len(self.expression.text)
        self.features[f.name] = f

    def vocabulary_similarity_optimised(self):
        for cluster in self.clusters:
            f1 = Feature()
            f1.name = "Single word similarity score for cluster" + cluster.name
            f1.value = 0
            f2 = Feature()
            f2.name = "Weighted single word similarity score for cluster" + cluster.name
            f2.value = 0
            table = cluster.generate_vocab_table()
            for word in identify_words(self.expression.text):
                if word in table:
                    f1.value += table[word]
                    f2.value += table[word]*len(word)
            self.features[f2.name] = f2
            self.features[f1.name] = f1

    def vocabulary_similarity_no_stopwords(self):
        for cluster in self.clusters:
            f = Feature()
            f.name = "No stopwords single word similarity score for cluster" + cluster.name
            f.value = 0
            table = cluster.generate_vocab_table_no_stopwords()
            for word in identify_words(self.expression.text):
                if word in table:
                    f.value += table[word]*len(word)
            self.features[f.name] = f

    def objective_word_present(self):
        f = Feature()
        f.name = "Key word score objective"
        f.value = 0
        with open("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/objective.txt", 'r') as input:
            data = input.read()
        total = 0.0
        length = 0.0
        for word in identify_words(self.expression.text):
            length += 1
            if word in data:
                total += 1
        return total / length

    def markers_present(self):
        words = identify_words(self.expression.text)
        fs = self.marker_identification.feature_generation_for(words)
        for f in fs:
            self.features[f.name] = f

    # TODO: create a hashtable for individual words without stop words (all + without given one)
    # TODO: create a hashtable for expressions (all + without given one)
    # TODO: create a hashtable for expressions without stop expressions (all + without given one)
