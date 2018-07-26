from chatbot.ChatEngine import *
import random

__all__ = [""]

def main():
    print("Hello. I'm really interested in your exercise habits.")
    print("Do you exercise on a regular basis?")
    i = input()
    print("I see... Could you tell me why?")
    while True:
        engine.input_and_classify()
        if engine.give_counterargument():
            print("Are you now convinced it's worth to exercise?")
            i = input()
            if len (i) == 0 or i[0] == 'y':
                break
            else:
                print(random.choice(["Alright, why?", "What stops you from doing more exercise then?"]))
    print("Thank you for taking the time time to speak to me :)")
    print("Good bye!")
    #print(engine.messages)

if __name__ == "__main__":
    print("Program initialisation:")
    engine = ChatEngine()
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180723-094404.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-motivation.json",
        name="motivation")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180723-094502.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-work.json",
        name="work")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180723-094505.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-time.json",
        name="time")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180723-092706.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-family.json",
        name="family")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180725-134454.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-money.json",
        name="money")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180725-135039.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-taste.json",
        name="taste")
    print("Program initialised correctly.")
    print("----")
    print()

    engine.add_counterarguments_from_file("/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/counterarguments.json")

    #handling more labels than counterarguments DONE
    #lemmatisation DONE
    #other messages DONE
    #courtasies DONE
    #fix classifiers DONE
    #store classifiers, markers
    #plan for the rest of the research
    #don't repeat countteratguments
    #pythonise code
    #TODO: thorough documentation
    #time
    #stemming of motivation and motivate
    #TODO: fix stemming/lemma + thesaurus
    #no classification?
    #example of a good conversation 5
    #read from a file
    #TODO: 6 classifiers
    #TODO: unclassified counterargument pointer - third try
    #TODO: demo negation + splitting/conjunction
    #TODO: boring data
    #TODO: hour and a half, to and from work
    #TODO: double negation
    #TODO: little as negation?

    main()

