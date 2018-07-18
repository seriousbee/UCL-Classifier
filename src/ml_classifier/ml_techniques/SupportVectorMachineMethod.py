from sklearn import svm
from sklearn.metrics import f1_score

__all__ = ["SupportVectorMachineMethod"]


class SupportVectorMachineMethod:
    def __init__(self, X, Y):
        self.classifier = None
        self.X = X
        self.Y = Y

    def train(self, percentage):
        self.classifier = svm.SVC()
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

    #TODO: understand what the output means
    def classify_unknown(self, expression):
        return self.classifier.predict(expression.export_as_array())[0]