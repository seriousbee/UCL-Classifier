class Cluster:

    def __init__(self, name, sentences):
        """Initializes the data."""
        self.name = name
        self.__sentences = sentences
        print("(Initializing {})".format(self.__name))
        self.values = {}
        self.compute_values()

    def compute_values(self):
        total = 0.0
        for sentence in self.__sentences:
            for word in sentence.toLowerCase().split(' '):
                if word in self.values:
                    self.values[word] += 1
                else:
                    self.values[word] = 1
                total += 1
        for i in self.values:
            self.values[i] /= total

    def rate_new_sentence(self, sentence):
        total = 0.0
        for word in sentence.toLowerCase().split(' '):
            if word in self.values:
                total += self.values[word]
        return total