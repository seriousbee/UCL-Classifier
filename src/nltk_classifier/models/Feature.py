__all__ = ["Feature"]


class Feature:
    def __init__(self):
        self.name = ""
        self.value = 0.0

    def __str__(self):
        return "<" + self.name + ", " + str(self.value) + ">"
