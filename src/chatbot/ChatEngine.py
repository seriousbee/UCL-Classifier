from ml_classifier.ml_techniques.Classifier import *
import random, json
__all__ = ["ChatEngine"]

class ChatEngine:
    def __init__(self):
        self.classifier = Classifier()
        self.messages = []
        self.counterarguments = {}
        self.depth_counter = 0
        self.not_understood = ["Please rephrase", "I didn't quite get that...", "Could you expand on this, please?"]

    def add_classifier_layer(self, labeled_path, raw_path, name):
        self.classifier.add_training(raw_path, labeled_path, name)

    def input_and_classify(self):
        i = input()
        while i == "":
            print("Please say something or type 'X' to finish the conversation")
            i = input()
            if i=="X":
                exit()
        self.messages.append([i,{}])
        self.messages[-1][1] = self.classifier.classify_unknown(self.messages[-1][0])
        return self.messages[-1][1]

    def is_short(self):
        return len(self.messages[-1][0].split(" ")) < 6

    def is_key(self, key):
        return self.messages[-1][1][key] != "Other"

    def combined_key(self, markers):
        combined_key = ""
        for marker in markers:
            combined_key += marker
        return combined_key

    #takes an array of counterarguments and an array of markers
    def add_counterarguments(self, arguments, markers):
        self.counterarguments[self.combined_key(sorted(markers))] = arguments

    def add_counterarguments_from_file(self, path):
        with open(path, 'r') as input:
            data = input.read()
        j_object = json.loads(data)
        for i in j_object["counterclasses"]:
            self.add_counterarguments(i["arguments"], i["markers"])

    def give_counterargument(self):
        labels = []
        for key in sorted(self.messages[-1][1].keys()):
            if self.is_key(key):
                labels.append(key)
        for i in self.powerset(labels):
            com_key = self.combined_key(i)
            if com_key in self.counterarguments:
                print(random.choice(self.counterarguments[com_key]))
                #print(self.counterarguments[com_key].pop(0))
                self.depth_counter += 1
                return True

        if self.depth_counter > 0:
            print("Did your argument relate to my previous counterargument or the initial statement? Type 1 or 2 respecively")
            i = input()
            if i == "1":
                #do something with the new argument
                pass
            elif i == "2":
                #do something with the new argument
                pass
            print("Thank you for taking part in the study. Good-bye!")
            exit()

        print(random.choice(self.not_understood))
        return False

    def powerset(self, s):
        result = []
        x = len(s)
        for i in range(1 << x):
            result.append([s[j] for j in range(x) if (i & (1 << j))])
        return list(reversed(sorted(result, key=len)))