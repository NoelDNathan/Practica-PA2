from experimenter import Experiment
import sys


def main(input_data):
    experiment = None
    while input_data != None:  # Está mal
        line = input_data.readline()
        words = line.split()
        if words[0] == "experiment":
            n = words[1]
            m = words[2]
            tree = input_data.readline()
            genomes = []
            for _ in range(n):
                genomes += input_data.readline()

            experiment = Experiment(n, m, genomes)


fitxer = sys.argv[1]
with open(fitxer) as input_data:
    main(input_data)
