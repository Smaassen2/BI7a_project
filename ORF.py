# Created By: Tosca Frederiks
# Created Date: 21 march 2022
# Version: 1.0
# Searching for ORF's from amino acid till stop codon in the
# given sequence

def finding_ORF(sequence):
    """Searching for Open Reading Frames (ORF's) from amino acid till
    stop codon in a giffen sequence

    :return:
    orfs - List - List with ORF sequences
    """
    # creats a new list to safe the ORF's
    orfs = []
    # puts the sequence in capital letters
    sequence = sequence.upper()
    stop = False
    try:
        for i in range(0, len(sequence), 3):
            codon1 = sequence[i:i + 3]
            # checks if the 3 letter codons are in the start_codon list
            if codon1 in start_codon:
                position1 = i
                # checks if it found a start codon where the stop_codon
                # in the same frame is
                while stop is False:
                    for j in range(position1, len(sequence), 3):
                        codon2 = sequence[j:j + 3]
                        if codon2 in stop_codon:
                            stop = True
                            position2 = j
                            orfs.append(sequence[position1:position2+3])
            elif codon1 in stop_codon:
                break
    except TypeError:
        print("Deze sequentie is geen DNA sequentie.")

    return orfs


if __name__ == '__main__':
    seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTG" \
          "GATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    stop_codon = ["TTA", "TGA", "TAG"]
    start_codon = ["ATG", "TTT", "TTC", "TTG", "CTT", "CTC", "CTA",
                   "CTG", "ATT", "ATC", "ATA", "GTT", "GTC", "GTA",
                   "GTG", "TCT", "TCC", "TCA", "TCG", "CCT", "CCC",
                   "CCA", "CCG", "ACT", "ACC", "ACA", "ACG", "GCT",
                   "GCC", "GCA", "GCG", "TAT", "TAC", "CAT", "CAC",
                   "CAA", "CAG", "AAT", "AAC", "AAA", "AAG", "GAT",
                   "GAC", "GAA", "GAG", "TGT", "TGC", "TGG", "CGT",
                   "CGC", "CGA", "CGG", "AGT", "AGC", "AGA", "AGG",
                   "GGT", "GGC", "GGA", "GGG"]
    finding_ORF(seq)
