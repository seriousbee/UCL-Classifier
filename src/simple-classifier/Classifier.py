# represents a classifier system - it has a list of clusters, is able to create the clusters, and allocate an unknown
# sentence to one of the clusters


class Classifier:

    def __init__(self, clusters):
        self.__clusters = clusters

    def classify(self, sentence):
        max_value = 0
        max_cluster = ""
        for cluster in self.__clusters:
            value = cluster.rate_new_sentence(sentence)
            if value > max_value:
                max_value = value
                max_cluster = cluster.name
        return max_cluster

    # test data is a list of tuples - sentence and the correct outcome
    def test(self, test_data):
        total = 0.0
        correct = 0
        for test_case in test_data:
            total += 1
            result = self.classify(test_case[0])
            if result == test_case[1]:
                print("Passed: " + test_case[0] + " correctly identified as " + test_case[1])
                correct += 1
            else:
                print("Failed: " + test_case[0] + " identified as " + result + ", instead of " + test_case[1])
        print("Success rate: " + str(correct/total))