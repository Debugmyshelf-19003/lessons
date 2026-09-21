import sys

filename = sys.argv[1]
sequencef = sys.argv[2]

with open(filename) as f:
    codes = f.readlines()

#program to take a codon table file standard_code and sequence file and outputs the amino acid seq
for line in codes:
    a = codes[1].split( )
    a1 = a[-1]
    b = codes[2].split( )
    b1 = b[-1]
    c = codes[3].split( )
    c1 = c[-1]
    d = codes[4].split( )
    d1 = d[-1]
    e = codes[5].split( )
    e1 = e[-1]

l = [a1, b1, c1, d1, e1]
print(l)

codons = {}
for i in range(len(a1)):
    codon = c1[i] + d1[i] + e1[i]
    codons[codon] = a1[i]

#opening the actual sequence file

with open(sequencef) as f:
    sequence = f.read()
    sequence = "".join(sequence.split())

amino_acids = ""

for i in range(0,len(sequence),3):
    codon = sequence[i:i+3]
    amino_acids = amino_acids + codons[codon]
print("Amino acid sequence:", amino_acids)
print(len(amino_acids))
start_codons = set()

for i in range(len(b1)):
    if b1[i] == "M":
        codon = c1[i] + d1[i] + e1[i]
        start_codons.add(codon)
print("start codon from standard codon table:", start_codons)
