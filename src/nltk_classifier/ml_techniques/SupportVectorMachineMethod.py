from sklearn import svm

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
        print("Trained Model, accuracy:")
        print(self.classifier.score(X2, Y2))