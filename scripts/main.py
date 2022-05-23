from pyparsing import WordEnd
from experimenter import Experiment
import sys


def main(input_data):
    experiment = None
    while True:
        line = input_data.readline()
        words = line.split()
        if not words:
            break

        task = words[0]
        print(words)
        if task == "experiment":
            n = int(words[1])
            m = int(words[2])
            tree = input_data.readline().split()
            genomes = []
            for _ in range(n):
                genomes += input_data.readline()

            experiment = Experiment(n, m, tree, genomes)

        if task == "afegir_tret":
            feature, id = words[1], int(words[2])
            experiment.afegir_tret(id, feature)

        if task == "consulta_tret":
            feature = words[1]
            experiment.consulta_tret(feature)

        if task == "consulta_individu":
            id = int(words[1])
            experiment.consulta_individu(id)

        if task == "distribucio_tret":
            feature = words[1]
            experiment.distribucio_tret(feature)


with open("Input_Output/Input.inp") as input_data:
    main(input_data)
