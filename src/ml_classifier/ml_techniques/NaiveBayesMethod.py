import nltk


__all__ = ["NaiveBayesMethod"]


class NaiveBayesMethod:
    def __init__(self, labeled_tuples):
        self.labeled_tuples = labeled_tuples
        self.classifier = None

    def train(self, percentage):
        i = int(len(self.labeled_tuples)*percentage)
        train_set = self.labeled_tuples[i:]
        test_set = self.labeled_tuples[:i]
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        #print("Trained Model, precision:")
        #print(nltk.classify.accuracy(self.classifier, test_set))

    def classify_unknown(self, expression):
        #self.classifier.classify(expression.export_as_dict())
        return True