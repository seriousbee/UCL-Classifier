from ml_classifier.models.Feature import *

__all__ = ["Expression"]


class Expression:
    def __init__(self, text, label):
        self.text = text
        self.features = {}
        self.label = label

    def export_as_tuple(self):
        if self.text != "Unknown":
            return (self.text,) + (tuple([self.features[i].value for i in self.features])) + (self.label,)
        return (self.text,) + (tuple([self.features[i].value for i in self.features]))

    def export_as_array(self):
        # if "text" not in self.features:
        #     f = Feature()
        #     f.name = "text"
        #     f.value = self.text
        #     self.features["text"] = f
        return [[self.features[i].value for i in sorted(self.features.keys())]]

    def export_as_dict(self):
        feature_dict = {"text": self.text}
        for key in self.features:
            feature_dict[self.features[key].name] = self.features[key].value
        if self.text != "Unknown":
            return (feature_dict, self.label)
        return feature_dict

    def __str__(self):
        if self.features:
            return str(self.features) + "; " + self.label
        else:
            return "<\"" + self.text + "\", \"" + self.label + "\">"
