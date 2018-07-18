from ml_classifier.ml_techniques.Training import *
__all__ = ["util", "models", "ml_techniques"]


def main():
    training = Training(raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-family.json", train_only=False)
    print("SVM: ")
    training.support_vector_machine_train(.8)

    print("Naive Bayes: ")
    training.naive_bayes_train(.8)

    print("Decision Tree: ")
    training.decision_tree_train(.8)


if __name__ == "__main__":
    main()
