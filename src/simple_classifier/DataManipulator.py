import json
from simple_classifier.Cluster import *
__all__=["DataManipulator"]

# system responsible for splitting som input clusters' data into training and testing data
class DataManipulator:

    def __init__(self, path, percentage):
        self.__clusters = []
        self.__test_data = []
        with open(path, 'r') as input:
            data = input.read()
        self.decode(data, percentage)

    # format: clusters: {{name: A, sentences: ["sen1", "sen2"]}, {name: B, sentences: ["sen3", "sen4"]}}
    def decode(self, json_string, percentage):
        j_object = json.loads(json_string)

        for i in j_object["clusters"]:
            cluster = Cluster(i["name"], i["sentences"])
            self.__clusters.append(cluster)
        self.extract_testing_data(percentage)

        for cluster in self.__clusters:
            cluster.compute_values()

    # percentage is a float between 0 and 1
    def extract_testing_data(self, percentage):
        for cluster in self.__clusters:
            for i in range(int(cluster.size() * percentage)):
                data_point = cluster.pop_random_sentence()
                self.__test_data.append((data_point, cluster.name))

    def get_clusters(self):
        return self.__clusters

    def get_test_data(self):
        return self.__test_data
