# Created by: Shahiel Maassen
# Created Date: 22-3-2022
# Version: 9.0
# Calling on all the classes at the correct time with the correct
# parameters.
from ORF import ORF1
from BLASTN import BLAST


if __name__ == '__main__':
    # insert the DNA sequence to use
    seq = "ATGGTGAGATAGGAT"
    # call the class ORF
    ORF_list = ORF1.finding_ORF(seq)
    print(ORF_list)
    # call the class BLASTN
    BLAST.blasts(ORF_list)
