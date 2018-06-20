class FeatureCreator:

    def __init__(self, clusters, expression):
        self.clusters = clusters
        self.expression = expression
        self.features = []

    def produce_features(self):
        self.features.append(self.feature_length())
        self.features.append(self.vocabulary_similarity())

    def feature_length(self):
        f = Feature()
        f.name = "Length of string"
        f.value = len(self.__sentence)
        return f

    def vocabulary_similarity(clusters):
        f = Feature()
        f.name == "Single word similarity score"
        #calculate the value
        f.value = 0
        return f