from nltk_classifier.DataImporter import *
__all__ = ["Clusters"]


#stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)
        self.identify_features()

    #imports raw data into raw clusters
    def import_raw_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters

    def create_labeled_dataset(self):
        # TODO: given the clusters, prepare the data to be injested into ML
        pass

    def identify_features(self):
        ff = FeatureFactory(self.clusters)

