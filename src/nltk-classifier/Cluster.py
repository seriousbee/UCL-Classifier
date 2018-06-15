from Expression import *


class Cluster:
    def __init__(self, name, sentences):
        self.name = name
        self.expressions = []
        self.sentences = sentences

    def setences_to_expressions(self, sentences):
        for sentence in sentences:
            self.expressions.append(Expression(sentence))

    def calculate_relative_features(self):
        for i in range(len(self.expressions)):
            self.whatever(self.expressions[i], self.expressions[:i] + self.expressions[i+1:])

    def whatever(self, expression, others):
        expression.update_relative_features(others)