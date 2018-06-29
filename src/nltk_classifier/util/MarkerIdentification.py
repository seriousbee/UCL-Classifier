__all__ = ["MarkerIdentification"]


class MarkerIdentification:

    def __init__(self, clusters):
        self.vocab_tables = []
        self.clusters = clusters
        self.markers = []

    def identify_markers(self):
        for cluster in self.clusters:
            table = cluster.generate_vocab_table_no_stopwords()
            self.vocab_tables.append(table)
        lists = []
        for table in self.vocab_tables:
            list_n = table.items()
            lists.append(sorted(list_n, key=lambda tup: -tup[1]))
        for list_n in lists:
            for i in range(30):
                if self.is_good_marker(list_n[i][0], list_n[i][1]):
                    self.markers.append(list_n[i][0])
        return self.markers


    def is_good_marker(self, key, value):
        for table in self.vocab_tables:
            if key not in table or table[key] * 2 < value:
                return True
        return False