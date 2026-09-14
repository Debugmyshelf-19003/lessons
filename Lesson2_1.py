# 2.1 Test whether a PCR primer is a reverse complement palindrome

# test the program on the following
# Primer 1 = TTGAGTAGACGCGTCTACTCAA
# Primer 2 = TTGAGTAGACGTCGTCTACTCAA
# Primer 3 = ATATATATATATATAT
# Primer 4 = ATCTATATATATGTAT

input_seq = input("Enter a PCR primer: ")

def compliment(nuc):

    nucleotides = 'ACGT' # it will change the nuc at the same position
    compliments = 'TGCA'

    i = nucleotides.find(nuc)

    if i>= 0:
        comp = compliments[i]
    else:
        comp = nuc
    return comp

def reversecompliment(seq):
    seq = seq.upper()
    newseq = ""

    for nuc in seq:
        newseq = compliment(nuc) + newseq

    return newseq

def palindrome(seq):
    seq = seq.upper()
    seq_length = len(seq)

# The function below removes the middle nuc if odd and checks if the first and second part is palindrome.
# The sequence/primer can sometimes make self hybrid structures and this function helps to include the condition.

    if seq_length % 2 != 0:
        middle = seq_length // 2
        seq = seq[:middle] + seq[middle+1:]

    if seq == reversecompliment(seq):
        return True
    else:
        return False

print('The reverse compliment is ', reversecompliment(input_seq))
print('The palindrome is ', palindrome(input_seq))

# Primer 1 = True
# Primer 2 = True (middle nuc removed as a it can self hybridize)
# Primer 3 = True
# Primer 4 = False
