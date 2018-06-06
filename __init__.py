from Classifier import *
from DataManipulator import *


def main():
    dm = DataManipulator("clusters.json", 0.3)
    classifier = Classifier(dm.get_clusters())
    classifier.test(dm.get_test_data())

if __name__ == "__main__":
    main()

