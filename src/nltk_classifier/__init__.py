from nltk_classifier.Clusters import Clusters
from nltk_classifier.NltkTraining import *


def main():
    clusters = Clusters("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-new-clusters.json")
    training = NltkTraining(clusters.get_labeled_dataset())
    training.train()
    training.classifier.classify(clusters.identify_features_for_unknown("I don't like working out."))

__all__ = ["Cluster", "Clusters", "DataImporter", "Expression", "Feature", "FeatureFactory", "FeatureCreator"]
if __name__ == "__main__":
    main()

