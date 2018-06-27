from nltk_classifier.models.Feature import *
__all__ = ["FeatureCreator"]


class FeatureCreator:

    def __init__(self, clusters, expression):
        self.clusters = clusters
        self.expression = expression
        self.features = {}
        self.tables = []

    def produce_features(self):
        self.feature_length()
        self.vocabulary_similarity_optimised()
        self.vocabulary_similarity_no_stopwords()
        #self.objective_word_present()
        self.identify_markers()
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
            for word in self.expression.text.lower().replace(".", "").replace(",", "").split(' '):
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
            for word in self.expression.text.lower().replace(".", "").replace(",", "").split(' '):
                if word in table:
                    f.value += table[word]*len(word)
            self.features[f.name] = f
            self.tables.append(table)

    def objective_word_present(self):
        f = Feature()
        f.name = "Key word score objective"
        f.value = 0
        with open("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/objective.txt", 'r') as input:
            data = input.read()
        total = 0.0
        length = 0.0
        for word in self.expression.text.lower().replace(".", "").replace(",", "").split(' '):
            length += 1
            if word in data:
                total += 1
        return total / length

    def identify_markers(self):
        lists = []
        markers = []
        for table in self.tables:
            list_n = table.items()
            lists.append(sorted(list_n, key=lambda tup: -tup[1]))
        for list_n in lists:
            for i in range(30):
                if self. is_good_marker(list_n[i][0], list_n[i][1]):
                    markers.append(list_n[i][0])
        print(markers)

    def is_good_marker(self, key, value):
        for table in self.tables:
            if key not in table or table[key]*2 < value:
                return True
        return False
    # TODO: create a hashtable for individual words without stop words (all + without given one)
    # TODO: create a hashtable for expressions (all + without given one)
    # TODO: create a hashtable for expressions without stop expressions (all + without given one)
