from chatbot.ChatEngine import *

__all__ = [""]

def main():
    print("Hello. I'm really interested in your exercise habits.")
    print("Do you exercise on a regular basis?")
    i = input()
    print("I see... Could you tell me why?")
    while True:
        engine.input_and_classify()
        engine.give_counterargument()
        print("Are you now convinced it's worth to exercise?")
        i = input()
        if i[0] == 'y':
            break
        else:
            print("Why?")
    print("Thank you for taking the time time to speak to me :)")
    print("Good bye!")

if __name__ == "__main__":
    print("Program initialisation:")
    engine = ChatEngine()
    print("Progress: 10%")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180718-094337.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-motivation.json",
        name="motivation")
    print("Progress: 40%")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180718-094629.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-work.json",
        name="work")
    print("Progress: 60%")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180718-094633.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-time.json",
        name="time")
    print("Progress: 80%")
    engine.add_classifier_layer(
        labeled_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/features20180718-094647.json",
        raw_path="/Users/tomaszczernuszenko/PycharmProjects/UCL-Classifier/data/excercise-is-family.json",
        name="family")
    print("Progress: 100%")
    print("Program initialised correctly.")
    print("----")
    print()


    engine.add_counterarguments(markers = ["motivation"], arguments= ["You could use a personal coach"])
    engine.add_counterarguments(markers =["work"], arguments= ["You could join a gym close to your office"])
    engine.add_counterarguments(markers =["time"], arguments= ["If you waste less time on social media, you'll surely find time to excercise"])
    engine.add_counterarguments(markers =["family"], arguments=["You can can ask a member of your family to care of the household while you excercise"])
    engine.add_counterarguments(markers =["motivation", "work"], arguments= ["You can work out with other people from your office"])
    engine.add_counterarguments(markers =["motivation", "time"], arguments= ["Try watching some motivation speakers about time management"])
    engine.add_counterarguments(markers =["motivation", "family"], arguments= ["You could use a personal coach"])
    engine.add_counterarguments(markers =["work", "time"], arguments= ["Try lunchtime workouts!"])
    engine.add_counterarguments(markers =["work", "family"], arguments= ["Invite your other collegues from work and you can all with your families"])
    engine.add_counterarguments(markers =["time", "family"], arguments= ["Maybe you get someone to take care of the house while you're away?"])

    engine.add_counterarguments(["motivation", "work"], ["You could use a personal coach"])
    #handling more labels than counterarguments DONE
    #lemmatisation DONE
    #other messages DONE
    #courtasies DONE
    #fix classifiers DONE
    #store classifiers, markers
    #plan for the rest of the research
    #TODO: don't repeat countteratguments
    #TODO: new features - main word in a subsentence and y/n
    #TODO: pythonise code
    #TODO: thorough documentation

    main()

