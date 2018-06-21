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

    def __str__(self):
        return "<\"" + self.text + "\", \"" + self.label + "\">"
