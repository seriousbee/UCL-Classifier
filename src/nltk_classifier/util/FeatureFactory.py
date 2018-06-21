from nltk_classifier.util.FeatureCreator import *
__all__ = ["FeatureFactory"]


class FeatureFactory:

    def __init__(self, clusters):
        self.clusters = clusters
        self.expressions = []
        self.extract_expressions()
        self.labeled_exprs = []
        self.total = 0
        for i in clusters: self.total += len(i)
        self.generate_features()

    def extract_expressions(self):
        for cluster in self.clusters:
            for expression in cluster.expressions:
                self.expressions.append(expression)

    def generate_features(self):
        i = 1
        for expression in self.expressions:
            print("Working on: " + str(i) + " of " + str(self.total))
            i += 1
            rel_clusters = []
            for cluster in self.clusters:
                rel_clusters.append(cluster.get_cluster_without_expr(expression))
            fc = FeatureCreator(rel_clusters, expression)
            self.labeled_exprs.append(fc.produce_features())
