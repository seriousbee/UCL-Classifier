from nltk_classifier.models.Clusters import Clusters
from nltk_classifier.ml_techniques.NltkTraining import *


def main():
    clusters = Clusters("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-new-clusters.json")
    training_set = clusters.get_labeled_dataset()
    training = NltkTraining(training_set)
    training.train(0.9)
    i = clusters.identify_features_for_unknown("I don't like working out.")
    print(training.classifier.classify(i))

__all__ = ["util", "models", "ml_techniques"]

if __name__ == "__main__":
    main()
