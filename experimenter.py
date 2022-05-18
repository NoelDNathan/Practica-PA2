from binTree import BinTree
from person import Person
# Add Graphviz
# lst = [3, 1, 4, 0, 0, 2, 0, 0, 5, 0, 0]
# print(preorder2tree(lst).preorder())


class Experiment:
    def __init__(self, n, m, tree, genomes):
        self.__n = n
        self.__m = m
        self.__family_tree = self.__preorder2tree__(tree)
        self.__people = self.__people__(genomes)
        self.__feature = {}  # Crear nuestra propia version de diccionario
    # Getters

    def has_feature(self, feature):
        return feature in self.__feature

    def get_number_people(self):
        return self.__n

    def get_genome_size(self):
        return self.__m

    def get_family_tree(self):
        return self.__family_tree

    def get_person(self, id):
        return self.__people[id + 1]

    def __people__(self, genomes):
        output = []
        for id in range(1, self.__n + 1):
            gens_person = []
            for n in range(len(genomes[id])//self.get_genome_size()):
                gens_person += genomes[id][n:((n+1)+1)]

            output += Person(id, gens_person)
        return output

    # Hacer un buen testing

    def __preorder2tree__(self, lst):
        tree = BinTree(v=lst[0])
        trees = [tree]
        isRight = False
        for element in lst[1:]:
            if element:
                if isRight:
                    isRight = False
                    new_tree = BinTree(v=element)
                    t = trees.pop()
                    t.set_right(new_tree)
                    tree = new_tree

                else:
                    new_tree = BinTree(v=element)
                    tree.set_left(new_tree)
                    trees.append(new_tree)
                    tree = new_tree
            else:
                isRight = True

        return trees.pop()


#   Funciones que piden explicitamente los profes

    def afegir_tret(self, id, feature):
        assert type(feature) == 'string'
        assert 1 <= id <= self.get_number_people()
        self.get_person(id).add_feature(feature)
        self.consulta_tret(feature)

    def consulta_tret(self, feature):
        assert type(feature) == 'string'
        who_has = []
        persones = []
        for id in range(1, self.get_number_people() + 1):
            person = self.get_person(id)
            if person.has_feature(feature):
                who_has += (id + 1)
                persones += [person.get_genome()]
        if who_has == []:
            return print("error")
        output = genomes[0]
        g = len(genomes)
        for genomes in persones[1:]:
            for n in range(g):
                for i in output[n]:
                    if output[n][i] != genomes[n][i]:
                        output[n][i] = "-"

        return output, who_has

    def consulta_individu(self, id):
        assert 1 <= id <= self.get_number_people()
        print(self.get_person(id))

    def distribucio_tret(self, feature):
        assert type(feature) == 'string'
        if not self.has_feature():
            return print("error")

        feature_tree = BinTree()
