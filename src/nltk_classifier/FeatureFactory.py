from nltk_classifier.FeatureCreator import *
__all__ = ["FeatureFactory"]


class FeatureFactory:

    def __init__(self, clusters):
        self.clusters = clusters
        self.expressions = []
        self.extract_expressions()
        self.labeled_exprs = []
        self.generate_features()

    def extract_expressions(self):
        for cluster in self.clusters:
            for expression in cluster.expressions:
                self.expressions.append(expression)

    def generate_features(self):
        for expression in self.expressions:
            rel_clusters = []
            for cluster in self.clusters:
                rel_clusters.append(cluster.get_cluster_without_expr(expression))
            fc = FeatureCreator(rel_clusters, expression)
            self.labeled_exprs.append(fc.produce_features())
