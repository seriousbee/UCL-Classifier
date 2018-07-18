from ml_classifier.ml_techniques.Training import *
from ml_classifier.models.Clusters import Clusters

__all__ = ["Classifier"]


class Classifier:
    def __init__(self):
        self.trainings = []

    def add_training(self, raw_path, labeled_path, name):
        training = Training(labeled_path=labeled_path, raw_path=raw_path)
        training.decision_tree_train(.8)
        training.clusters = Clusters(training.raw_path)
        self.trainings.append((training, name))


    def classify_unknown(self, message):
        result = {}
        for train in self.trainings:
            result[train[1]] = train[0].classify_unknown(message)
            #print(result)
        return result
