from DataImporter import *


#stores all data in the system
class Clusters:

    def __init__(self):
        self.clusters = []
        pass

    #imports raw data into raw clusters
    def import_data(self, path):
        di = DataImporter(path)
        self.clusters = di.clusters


    def