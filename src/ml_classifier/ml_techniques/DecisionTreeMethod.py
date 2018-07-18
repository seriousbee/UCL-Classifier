from sklearn import tree
from sklearn.metrics import f1_score
import graphviz, time


__all__ = ["DecisionTreeMethod"]


class DecisionTreeMethod:
    def __init__(self, X, Y):
        self.classifier = None
        self.X = X
        self.Y = Y

    def train(self, percentage):
        self.classifier = tree.DecisionTreeClassifier(min_samples_leaf=5)
        i = int(len(self.X) * percentage)
        X1 = self.X[:i]
        X2 = self.X[i + 1:]
        Y1 = self.Y[:i]
        Y2 = self.Y[i + 1:]
        self.classifier.fit(X1, Y1)
        #print("Trained Model, precision:")
        #print(self.classifier.score(X2, Y2))
        y_true = Y2
        y_pred = self.classifier.predict(X2)
        #print("F1: " + str(f1_score(y_true, y_pred, average='macro')))

    def draw_decision_tree(self):
        dot_data = tree.export_graphviz(self.classifier, out_file=None)
        graph = graphviz.Source(dot_data)
        time_str = time.strftime("%Y%m%d-%H%M%S")
        graph.render("graph" + time_str)

    def classify_unknown(self, expression):
        return self.classifier.predict(expression.export_as_array())[0]