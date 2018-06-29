import random
from sklearn import tree
import json
import graphviz
import time

__all__ = ["DecisionTreeTraining"]


class DecisionTreeTraining:
    def __init__(self, X, Y):
        self.classifier = None
        self.X = X
        self.Y = Y

    def train(self):
        random.shuffle(self.labeled_tuples)
        time_str = time.strftime("%Y%m%d-%H%M%S")
        with open('/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features' + time_str + ".json", 'w') as outfile:
            json.dump(self.labeled_tuples, outfile, indent=4, sort_keys=True)
        self.X = []
        self.Y = []
        for case in self.labeled_tuples:
            data1 = []
            for key in case[0]:
                try:
                    data1.append(float(case[0][key]))
                except ValueError:
                    pass
            self.X.append(data1)
            self.Y.append(case[1])
        self.classifier = tree.DecisionTreeClassifier()
        self.classifier.fit(self.X, self.Y)
        print("Trained Model, accuracy:")
        print(self.classifier.score(self.X, self.Y))

    def setXY(self, X, Y):
        self.X = X
        self.Y = Y

    def train2(self):
        self.classifier = tree.DecisionTreeClassifier()
        i = int(len(self.X) * .8)
        X1 = self.X[:i]
        X2 = self.X[i + 1:]
        Y1 = self.Y[:i]
        Y2 = self.Y[i + 1:]

        self.classifier.fit(X1, Y1)
        print("Trained Model, accuracy:")
        #todo fix test data
        print(self.classifier.score(X2, Y2))

        dot_data = tree.export_graphviz(self.classifier, out_file=None)
        graph = graphviz.Source(dot_data)
        graph.render("output.png")
