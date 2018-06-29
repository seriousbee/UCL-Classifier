from sklearn import tree
import graphviz

__all__ = ["DecisionTreeMethod"]


class DecisionTreeMethod:
    def __init__(self, X, Y):
        self.classifier = None
        self.X = X
        self.Y = Y

    def train(self, percentage):
        self.classifier = tree.DecisionTreeClassifier()
        i = int(len(self.X) * percentage)
        X1 = self.X[:i]
        X2 = self.X[i + 1:]
        Y1 = self.Y[:i]
        Y2 = self.Y[i + 1:]
        self.classifier.fit(X1, Y1)
        print("Trained Model, accuracy:")
        print(self.classifier.score(X2, Y2))

    def draw_decision_tree(self):
        dot_data = tree.export_graphviz(self.classifier, out_file=None)
        graph = graphviz.Source(dot_data)
        graph.render("output.png")
