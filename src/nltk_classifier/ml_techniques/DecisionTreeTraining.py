import random
from sklearn import tree
import json

__all__ = ["DecisionTreeTraining"]


class DecisionTreeTraining:
    def __init__(self, labeled_tuples):
        self.labeled_tuples = labeled_tuples
        self.classifier = None

    def train(self):
        random.shuffle(self.labeled_tuples)
        print(json.dumps(self.labeled_tuples))
        X = []
        Y = []
        for case in self.labeled_tuples:
            data1 = []
            for key in case[0]:
                data1.append(case[0][key])
            X.append(data1)
            Y.append(case[1])
        self.classifier = tree.DecisionTreeClassifier()
        self.classifier.fit(X, Y)
        print("Trained Model, accuracy:")
        print(self.classifier.score(X, Y))
