from FeatureFactory import *
class Expression:
    def __init__(self, text):
        self.text = text
        self.features = []

    def identify_features(self):
        ff = FeatureFactory(self.text)
        self.features = ff.produce_features()

    def export_as_tuple(self):
        return (i.value for i in self.features)