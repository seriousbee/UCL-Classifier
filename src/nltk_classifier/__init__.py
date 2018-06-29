from nltk_classifier.ml_techniques.Training import *
__all__ = ["util", "models", "ml_techniques"]


def main():
    training = Training("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features.json")
    training.naive_bayes_train(.8)

if __name__ == "__main__":
    main()
