from ml_classifier.models.Feature import *
from ml_classifier.util.WordSplitter import *
from nltk import pos_tag
from nltk.tokenize import sent_tokenize

__all__ = ["FeatureCreator"]


class FeatureCreator:

    def __init__(self, clusters=None, expression=None, marker_identification=None, is_subsentence=False, subsentence=""):
        if is_subsentence:
            self.marker_identification = marker_identification
            self.subsentence = subsentence
            self.features = {}
            self.expression = None
            self.markers_present()
            self.negate_markers()
        else:
            self.clusters = clusters
            self.expression = expression
            self.features = {}
            self.marker_identification = marker_identification

    def produce_features(self):
        #self.feature_length()
        #self.vocabulary_similarity_optimised()
        #self.vocabulary_similarity_no_stopwords()
        #self.markers_present()
        self.identify_negation_in_subsentences()
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
        if self.expression is None:
            words = identify_words(self.subsentence)
        else:
            words = identify_words(self.expression.text)
        fs = self.marker_identification.feature_generation_for(words)
        for f in fs:
            self.features[f.name] = f

    def negate_markers(self):
        negated_features = {}
        for key in self.features:
            if key == "negation":
                continue
            f = Feature()
            f.name = "not " + key
            f.value = self.features[key].value if self.features["negation"].value == 1 else 0
            negated_features[f.name] = f
        self.features.update(negated_features)


    def identify_subsentences(self):
        sent_tokenize_list = sent_tokenize(self.expression.text)
        sentences = []
        conjunctions = ["and", "but", ",", "because", "-", "so"]
        for sentence in sent_tokenize_list:
            words = identify_words_raw(sentence)
            sens =[""]
            for word in words:
                if word in conjunctions and len(sens[-1])>15:
                    sens.append("")
                else:
                    sens[-1] += " " + word
            sentences += sens
        print(sentences)
        return sentences

    def identify_negation_in_subsentences(self):
        self.markers_present()
        for subsentence in self.identify_subsentences():
            fc = FeatureCreator(marker_identification=self.marker_identification, is_subsentence=True, subsentence=subsentence)
            new_features = {}
            for key in fc.features:
                if key in self.features:
                    if fc.features[key].value == 1:
                        self.features[key].value = 1
                else:
                    new_features[key] = fc.features[key]
            self.features.update(new_features)
        print("No. of features:" + str(len(self.features)))