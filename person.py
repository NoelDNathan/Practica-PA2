
class Person:
    def __init__(self, id, genome):
        self.__id = id
        self.__genomes = genome
        self.__features = []

    def get_genomes(self):
        return self.__genomes

    def get_id(self):
        return self.__id

    def get_features(self):
        return self.__features

    def __str__(self) -> str:
        output = ""
        for genome in self.get_genomes():
            output += str(genome) + "\n"
        for feature in self.get_features():
            output += str(feature) + "\n"

    def has_feature(self, feature):
        return feature in self.get_features()

    def add_feature(self, feature):
        assert not self.has_feature(
        ), f"person: {self.__id} already has this feature"
        self.__features += feature
