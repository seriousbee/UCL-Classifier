from Cluster import *
from Classifier import *

def main():
    classifier = Classifier()
    with open('clusters.json', 'r') as f:
        data = f.read()
    classifier.decode(data)
    print(classifier.classify("I like meat"))
    print(classifier.classify("Meat is healthy"))
    print(classifier.classify("There's a variety of different meats"))



if __name__ == "__main__":
    main()

