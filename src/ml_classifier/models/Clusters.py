from ml_classifier.util.DataImporter import *
from ml_classifier.util.FeatureFactory import *
from ml_classifier.util.MarkerIdentificationLevel2 import *
from ml_classifier.util.FeatureCreator import *
from ml_classifier.models.Expression import *


__all__ = ["Clusters"]

# stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)
        self.labeled_expressions = []
        self.labeled_tuples = []
        self.marker_identifier = MarkerIdentificationLevel2(self.clusters)
        self.marker_identifier.identify_markers()

    # imports raw data into raw clusters
    def import_raw_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters

    def get_labeled_dataset(self):
        for expression in self.labeled_expressions:
            self.labeled_tuples.append(expression.export_as_dict())
        return self.labeled_tuples

    def identify_features(self):
        ff = FeatureFactory(self.clusters, self.marker_identifier)
        self.labeled_expressions = ff.labeled_exprs

    def __len__(self):
        total = 0
        for cluster in self.clusters:
            total += len(cluster)
        return total

    def identify_features_for_unknown(self, sentence):
        expression = Expression(sentence, "Unknown")
        fc = FeatureCreator(clusters=self.clusters, expression=expression, marker_identification=self.marker_identifier)
        return fc.produce_features()