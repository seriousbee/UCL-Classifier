from Expression import *


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

    def generate_vocab_table(self, expressions):
        table = {}
        total = 0.0
        for expression in expressions:
            for word in expression.text.lower().replace(".", "").replace(",", "").split(' '):
                if word in table:
                    table[word] += 1
                else:
                    table[word] = 1
                total += 1
        for i in table:
            table[i] /= total
        self.total = total #dangerous if method used not during initialisation
        return table


    #
    # def get_vocab_table_without(self, expression):
    #     table = self.vocabulary
    #     for word in expression.text.lower().split(' '):
    #         if word in table:
    #             table[word] -= 1/self.total
    #         else:
    #             print("Attempting to remove element that should have been there")
    #             print ("Cluster " + self.name)
    #             print ("Expression: " + expression)
    #             exit(0)
    #     return table
    #
    # def get_full_vocab_table(self):
    #     return self.vocabulary

    # TODO: create a hashtable for individual words without stop words (all + without given one)
    # TODO: create a hashtable for expressions (all + without given one)
    # TODO: create a hashtable for expressions without stop expressions (all + without given one)