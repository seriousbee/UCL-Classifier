from nltk_classifier.util.DataImporter import *
from nltk_classifier.util.FeatureFactory import *
from nltk_classifier.models.Expression import *
from nltk_classifier.util.FeatureCreator import *
import json
__all__ = ["Clusters"]


#stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)
        self.labeled_expressions = []
        self.vocab_tables = []
        self.markers = []
        self.labeled_tuples = []
        self.identify_markers()
        self.identify_features()

    #imports raw data into raw clusters
    def import_raw_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters

    def get_labeled_dataset(self):
        for expression in self.labeled_expressions:
            self.labeled_tuples.append(expression.export_as_dict())
        return self.labeled_tuples

    def identify_features(self):
        ff = FeatureFactory(self.clusters, self.markers)
        self.labeled_expressions = ff.labeled_exprs

    def identify_features_for_unknown(self, sentence):
        expr = Expression(sentence, "Unknown")
        fc = FeatureCreator(self.clusters, expr, self.markers)
        return fc.produce_features().export_as_dict()[0]

    def identify_markers(self):
        for cluster in self.clusters:
            table = cluster.generate_vocab_table_no_stopwords()
            self.vocab_tables.append(table)
        lists = []
        for table in self.vocab_tables:
            list_n = table.items()
            lists.append(sorted(list_n, key=lambda tup: -tup[1]))
        for list_n in lists:
            for i in range(30):
                if self. is_good_marker(list_n[i][0], list_n[i][1]):
                    self.markers.append(list_n[i][0])

    def is_good_marker(self, key, value):
        for table in self.vocab_tables:
            if key not in table or table[key]*2 < value:
                return True
        return False

    def __len__(self):
        total = 0
        for cluster in self.clusters:
            total += len(cluster)
        return total