genome = input()
print((genome.upper().count('g'.upper()) + genome.upper().count('c'.upper())) * 100 / len(genome))
