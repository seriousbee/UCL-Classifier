from nltk_classifier.DataImporter import *
from nltk_classifier.FeatureFactory import *
from nltk_classifier.Expression import *
from nltk_classifier.FeatureCreator import *
__all__ = ["Clusters"]


#stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)
        self.labeled_expressions = []
        self.identify_features()


    #imports raw data into raw clusters
    def import_raw_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters

    def get_labeled_dataset(self):
        labeled_tuples = []
        for expression in self.labeled_expressions:
            # labeled_tuples.append(expression.export_as_tuple())
            labeled_tuples.append(expression.export_as_dict())
        return labeled_tuples

    def identify_features(self):
        ff = FeatureFactory(self.clusters)
        self.labeled_expressions = ff.labeled_exprs

    def identify_features_for_unknown(self, sentence):
        expr = Expression(sentence, "Unknown")
        fc = FeatureCreator(self.clusters, expr)
        return fc.produce_features().export_as_dict()[0]
