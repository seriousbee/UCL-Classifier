from nltk.corpus import wordnet


__all__ = ["MarkerIdentificationLevel2"]


class MarkerIdentificationLevel2:

    def __init__(self, clusters):
        self.vocab_tables = []
        self.clusters = clusters
        self.markers = []
        self.more_markers = {}

    def identify_markers(self):
        self.generate_vocab_tables()
        lists = self.sort_dictionaries_and_save_as_tuples()
        for list_n in lists:
            for i in range(30):
                word = list_n[i][0]
                if word not in self.more_markers:
                    self.markers.append(word)
                    self.more_markers[word] = word
                    synonyms = self.find_synonyms_for_word(word)
                    for synonym in synonyms:
                        if synonym not in self.more_markers:
                            self.more_markers[synonym] = word
        return self.more_markers

    def find_synonyms_for_word(self, word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        return synonyms

    def generate_vocab_tables(self):
        for cluster in self.clusters:
            table = cluster.generate_vocab_table_no_stopwords()
            self.vocab_tables.append(table)

    def sort_dictionaries_and_save_as_tuples(self):
        lists = []
        for table in self.vocab_tables:
            list_n = table.items()
            lists.append(sorted(list_n, key=lambda tup: -tup[1]))
        return lists