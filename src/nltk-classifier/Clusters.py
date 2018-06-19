from DataImporter import *


#stores all data in the system
class Clusters:

    def __init__(self, path):
        self.clusters = []
        self.import_raw_data(path)

    #imports raw data into raw clusters
    def import_raw_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters

    def create_labeled_dataset(self):
        # TODO: given the clusters, prepare the data to be injested into ML
        pass

