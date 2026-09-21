import sys
filename = sys.argv[1]
with open(filename) as f:
    DNA = f.read().upper()

Bases = ["A","T","C","G"]
complements = ["T","A","G","C"]

complement = ""

for i in DNA:
    position = Bases.index(i)
    complement = complement + complements[position]

reverse_complement = complement[::-1]

print("original DNA sequence:", DNA)
print("complement:", complement)
print("reverse_complement:", reverse_complement)
