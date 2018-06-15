from FeatureFactory import *


class Expression:
    def __init__(self, text, label):
        self.text = text
        self.features = []
        self.label = label

    def identify_features(self):
        ff = FeatureFactory.new_expression(self.text)
        self.features = ff.produce_features()

    def export_as_tuple(self):
        #transform the features array into a hashtable
        return (i.value for i in self.features)

    def update_relative_features(self, clusters):
        ff = FeatureFactory.updating_features(self)
        ff.calculate_relative(clusters)