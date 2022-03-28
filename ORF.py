# Created By: Tosca Frederiks
# Created Date: 21 march 2022
# Version: 1.0
# Searching for ORF's from amino acid till stop codon in the
# given seq

class ORF1:
    def finding_ORF(sequence):
        """Searching for Open Reading Frames (ORF's) from amino acid till
        stop codon in a giffen seq
        :param
        sequence - String - String of DNA nucleotides
        :return:
        orfs - List - List with ORF sequences
        """

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

        # creats a new list to safe the ORF's
        orfs = []
        # puts the seq in capital letters
        seq = sequence.upper()
        stop = False
        try:
            for i in range(0, len(seq), 3):
                codon1 = seq[i:i + 3]
                # checks if the 3 letter codons are in the
                # start_codon list
                if codon1 in start_codon:
                    position1 = i
                    # checks if it found a start codon where the
                    # stop_codon in the same frame is
                    while stop is False:
                        for j in range(position1, len(seq), 3):
                            codon2 = seq[j:j + 3]
                            if codon2 in stop_codon:
                                # if the codon is in the list stop_codon
                                # stop will be set in true
                                stop = True
                                position2 = j
                                orfs.append(seq[position1:
                                                     position2+3])
                elif codon1 in stop_codon:
                    break

        except TypeError:
            print("This seq is not a DNA seq.")
        except SyntaxError:
            print("An invalid syntax has been found in the function "
                  "blasts")
        return orfs
