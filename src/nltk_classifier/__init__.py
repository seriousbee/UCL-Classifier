from nltk_classifier.models.Clusters import Clusters
from nltk_classifier.ml_techniques.NaiveBayesMethod import *
from nltk_classifier.ml_techniques.DecisionTreeMethod import *
import json
__all__ = ["util", "models", "ml_techniques"]


def main():
    with open("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features.json", 'r') as input:
        data = input.read()
    j_object = json.loads(data)
    X = []
    Y = []
    for i in j_object:
        Y.append(i[1])
        arr = []
        for k in i[0]:
            try:
                arr.append(float(i[0][k]))
            except ValueError:
                pass
        X.append(arr)

    #clusters = Clusters("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-subjective-objective.json")
    #training_set = clusters.get_labeled_dataset()
    training = DecisionTreeTraining(None)
    training.setXY(X, Y)
    training.train2()
    # training = NltkTraining(training_set)
    # training.train(0.9)
    # i = clusters.identify_features_for_unknown("I don't like working out.")
    # print(training.classifier.classify(i))


if __name__ == "__main__":
    main()
