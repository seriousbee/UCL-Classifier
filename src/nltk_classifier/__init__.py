from nltk_classifier.Clusters import Clusters
from nltk_classifier.NltkTraining import *


def main():
    clusters = Clusters("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-new-clusters.json")
    training = NltkTraining(clusters.get_labeled_dataset())
    training.train(0.8)
    i = clusters.identify_features_for_unknown("I don't like working out.")
    print(training.classifier.classify(i))

__all__ = ["Cluster", "Clusters", "DataImporter", "Expression", "Feature", "FeatureFactory", "FeatureCreator"]
if __name__ == "__main__":
    main()


