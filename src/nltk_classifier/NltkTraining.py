import nltk
import random

__all__ = ["NltkTraining"]


class NltkTraining:
    def __init__(self, labeled_tuples):
        self.labeled_tuples = labeled_tuples
        self.classifier = None

    def train(self):
        i = int(len(self.labeled_tuples)/2)
        random.shuffle(self.labeled_tuples)
        train_set = self.labeled_tuples[i:]
        test_set = self.labeled_tuples[:i]
        print(train_set)
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        print("Done")
        print(nltk.classify.accuracy(classifier, test_set))