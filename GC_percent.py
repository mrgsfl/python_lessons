genome = input()
print((genome.upper().count('G') + genome.upper().count('C')) * 100 / len(genome))
