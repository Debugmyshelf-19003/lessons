import sys

filename = sys.argv[1]
with open(filename, "r") as f:
    DNA = f.read().upper()

complement = ""

for base in DNA:
    if base == "A":
        complement = complement + "T"
    elif base == "T":
        complement = complement + "A"
    elif base == "C":
        complement = complement + "G"
    elif base == "G":
        complement = complement + "C"

reverse_complement = complement[::-1]
print("original DNA sequence:", DNA)
print("complement:", complement)
print("reverse complement is:",reverse_complement)
