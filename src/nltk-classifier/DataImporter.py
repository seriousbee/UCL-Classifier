from Cluster import *
import json


# system responsible for splitting som input clusters' data into training and testing data
class DataImporter:

    def __init__(self, path):
        self.clusters = []
        with open(path, 'r') as input:
            data = input.read()
        self.decode(data)

    # format: clusters: {{name: A, sentences: ["sen1", "sen2"]}, {name: B, sentences: ["sen3", "sen4"]}}
    def decode(self, json_string):
        j_object = json.loads(json_string)

        for i in j_object["clusters"]:
            cluster = Cluster(i["name"], i["sentences"])
            self.clusters.append(cluster)
