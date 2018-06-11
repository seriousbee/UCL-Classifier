from Classifier import *
from DataManipulator import *


def main():
    dm = DataManipulator("meat-clusters.json", 0.33)
    classifier = Classifier(dm.get_clusters())
    classifier.test(dm.get_test_data())

if __name__ == "__main__":
    main()

