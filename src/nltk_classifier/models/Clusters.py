from nltk_classifier.util.DataImporter import *
from nltk_classifier.util.FeatureFactory import *
from nltk_classifier.util.MarkerIdentification import *
__all__ = ["Clusters"]

# stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)
        self.labeled_expressions = []
        self.markers = []
        self.labeled_tuples = []
        marker_identifier = MarkerIdentification(self.clusters)
        self.markers = marker_identifier.identify_markers()

        self.identify_features()

    # imports raw data into raw clusters
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

    def __len__(self):
        total = 0
        for cluster in self.clusters:
            total += len(cluster)
        return total