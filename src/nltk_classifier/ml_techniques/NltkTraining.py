import nltk
import random

__all__ = ["NltkTraining"]


class NltkTraining:
    def __init__(self, labeled_tuples):
        self.labeled_tuples = labeled_tuples
        self.classifier = None

    def train(self, percentage):
        i = int(len(self.labeled_tuples)*percentage)
        random.shuffle(self.labeled_tuples)
        train_set = self.labeled_tuples[i:]
        test_set = self.labeled_tuples[:i]
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        print("Trained Model, accuracy:")
        print(nltk.classify.accuracy(self.classifier, test_set))
