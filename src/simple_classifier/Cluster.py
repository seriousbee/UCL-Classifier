import random
__all__ = ["Cluster"]


# represents a cluster - a tuple of a name and a list of example sentences
class Cluster:

    def __init__(self, name, sentences):
        self.name = name
        self.__sentences = sentences
        self.values = {}

    # calculating the percentage number of  occurrences of each word
    def compute_values(self):
        total = 0.0
        for sentence in self.__sentences:
            for word in sentence.lower().split(' '):
                if word in self.values:
                    self.values[word] += 1
                else:
                    self.values[word] = 1
                total += 1
        for i in self.values:
            self.values[i] /= total

    def rate_new_sentence(self, sentence):
        total = 0.0
        for word in sentence.lower().split(' '):
            if word in self.values:
                total += self.values[word]
        return total

    def pop_random_sentence(self):
        return self.__sentences.pop(random.randrange(len(self.__sentences)))

    def size(self):
        return len(self.__sentences)