#
# Version: 1.0
#

def finding_ORF(seq):
    """Searching for Open Reading Frames (ORF's) from amino acid till
    stop codon in a giffen sequence

    :return:
    ORFs - List - List with ORF sequences
    """
    # creats a new list to safe the ORF's
    ORFs = []
    # puts the sequence in capital letters
    seq = seq.upper()
    stop = False
    for i in range(0, len(seq), 3):
        codon1 = seq[i:i+3]
        # checks if the 3 letters together are in the start_codon list
        if codon1 in start_codon:
            position1 = i
            # checks if it found a start codon where the stop_codon in
            # the same frame is
            while stop is False:
                for j in range(position1, len(seq), 3):
                    codon2 = seq[j:j+3]
                    if codon2 in stop_codon:
                        stop = True
                        position2 = j
                        if len(seq[position1:position2+3]) > 30:
                            ORFs.append(seq[position1:position2+3])

        elif codon1 in stop_codon:
            break

    return ORFs


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
