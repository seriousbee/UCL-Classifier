from ml_classifier.ml_techniques.Classifier import *

__all__ = []

def main():
    # load labeled data & train
    # write initial message
    # get input
    # classify input
    # if unable to classify - ask to rephrase
    # if classified but shorter than 6 words - please expand
    # if classified to multiple - from what I figure these issues are important, elaborate on one
    write_initial_message()

def write_initial_message():
    print("Hello. I'm really interested in your exercise habits.")
    print("Do you exercise on a regular basis?")
    i = input()
    print("I see... Could you tell me why?")
    while True:
        i = input()
        if simple_classify(i) != "Other":
            if len(i.split(" ")) < 6:
                print("I understand you don't have motivation, could you give me an example for it?")
                continue
            print("So you don't have motivation, right? A personal trainer can help")
            break
        else:
            if len(i.split(" ")) < 6:
                print("Would you mind expanding on it?")
            else:
                print("So motivation is not an issue in your case? That's an important first step!")

def simple_classify(message):
    return classifier.classify_unknown(message)


if __name__ == "__main__":
    classifier = Classifier()
    classifier.add_training(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180710-093846.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-motivation.json",
        name="motivation")
    classifier.add_training(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180711-103931.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-work.json",
        name="work")
    classifier.add_training(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180711-103856.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-time.json",
        name="time")
    classifier.add_training(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180711-103847.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-family.json",
        name="family")
    main()

