import sys
filename = sys.argv[1]

with open(filename) as f:
    input_primer = f.read()

def compliment(input_primer):
    seq = input_primer.upper()
    newseq = ""

    nucleotides = 'ACGT'
    compliments = 'TGCA'

    for nuc in seq:
        i = nucleotides.find(nuc)

        if i >= 0:
            comp = compliments[i]
        else:
            comp = nuc
        newseq = newseq + comp
    return newseq

def reverseCompliment(input_primer):
    seq = input_primer.upper()
    newseq = ""
    for nuc in seq:
        newseq = compliment(nuc) + newseq
    return newseq

inputp = input_primer.split("\n")

for lines in inputp:
    if lines != "":
        split = lines.split(" ")

        forward = split[0]
        reverse = split[1]

        note = split[2:]
        note = " ".join(note)

        forward_seq = reverseCompliment(forward)
        reverse_seq = reverseCompliment(reverse)

        print(forward_seq, reverse_seq, note)
