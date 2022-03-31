from ORF import ORF1
from BLASTN import BLAST


if __name__ == '__main__':
    # insert the DNA sequence to use
    seq = "ATGGTGATG"
    # call the class ORF
    ORF_list = ORF1.finding_ORF(seq)
    print(ORF_list)
    # call the class BLASTN
    BLAST.blasten(ORF_list)
