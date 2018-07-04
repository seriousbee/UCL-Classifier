from nltk_classifier.models.Clusters import Clusters
from nltk_classifier.ml_techniques.NaiveBayesMethod import *
from nltk_classifier.ml_techniques.DecisionTreeMethod import *
from nltk_classifier.ml_techniques.SupportVectorMachineMethod import *

import json, time, random
__all__ = ["Training"]


class Training:

    def __init__(self, path, train_only=True):
        self.training = None
        self.training_set = []
        self.X = []
        self.Y = []
        if train_only:
            with open(path, 'r') as input:
                data = input.read()
            j_object = json.loads(data)
            self.generate_XY_arrays(j_object)
            self.json_unpack_to_array_of_tuples(j_object)
        else:
            self.clusters = Clusters(path)
            self.training_set = self.clusters.get_labeled_dataset()
            random.shuffle(self.training_set)
            print(json.dumps(self.training_set))
            self.save_training_set_to_file(self.training_set)
            self.generate_XY_arrays(self.training_set)

    def decision_tree_train(self, percentage):
        self.training = DecisionTreeMethod(self.X, self.Y)
        self.training.train(percentage)
        self.training.draw_decision_tree()

    def support_vector_machine_train(self, percentage):
        self.training = SupportVectorMachineMethod(self.X, self.Y)
        self.training.train(percentage)

    def naive_bayes_train(self, percentage):
        self.training = NaiveBayesMethod(self.training_set)
        self.training.train(percentage)

    #TODO: identify unknown

    def generate_XY_arrays(self, array):
        for i in array:
            self.Y.append(i[1])
            arr = []
            for k in i[0]:
                try:
                    arr.append(float(i[0][k]))
                except ValueError:
                    pass
            self.X.append(arr)

    def json_unpack_to_array_of_tuples(self, json_array):
        for i in json_array:
            element = ({}, i[1])
            for k in i[0]:
                element[0][k]=i[0][k]
            self.training_set.append(element)

    def save_training_set_to_file(self, training_set):
        time_str = time.strftime("%Y%m%d-%H%M%S")
        with open('/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features' + time_str + ".json", 'w') as outfile:
            json.dump(training_set, outfile, indent=4, sort_keys=True)