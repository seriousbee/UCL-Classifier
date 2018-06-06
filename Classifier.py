import json
from Cluster import *


class Classifier:

    def __init__(self):
        """Initializes the data."""
        self.__clusters = []

    def classify(self, sentence):
        max_value = 0
        max_cluster = ""
        for cluster in self.__clusters:
            value = cluster.rate_new_sentence(sentence)
            if value > max_value:
                max_value = value
                max_cluster = cluster.name
        return max_cluster

    #format: clusters: {{name: A, sentences: ["sen1", "sen2"]}, {name: B, sentences: ["sen3", "sen4"]}}
    def decode(self, json_string):
        j_object = json.loads(json_string)
        for i in j_object["clusters"]:
            cluster = Cluster(i["name"], i["sentences"])
            self.__clusters.append(cluster)