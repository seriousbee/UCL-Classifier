from nltk_classifier.models.Expression import *
__all__ = ["Cluster"]


class Cluster:

    def __init__(self, name, sentences):
        self.name = name
        self.expressions = []
        self.sentences = sentences
        self.expressions = self.sentences_to_expressions(self.sentences)

    def sentences_to_expressions(self, sentences):
        expressions = []
        for sentence in sentences:
            expressions.append(Expression(sentence, self.name))
        return expressions

    def get_cluster_without_expr(self, expr):
        sentence = expr.text
        try:
            i = self.sentences.index(sentence)
            return Cluster(self.name, self.sentences[:i] + self.sentences[i+1:])
        except ValueError:
            return Cluster(self.name, self.sentences)

    def generate_vocab_table(self):
        table = {}
        total = 0.0
        for expression in self.expressions:
            for word in expression.text.lower().replace(".", "").replace(",", "").split(' '):
                if word in table:
                    table[word] += 1
                else:
                    table[word] = 1
                total += 1
        for i in table:
            table[i] /= total
        return table
