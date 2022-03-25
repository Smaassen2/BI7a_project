from ORF import ORF1
from BLASTN import BLAST


if __name__ == '__main__':
    seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTG" \
          "GATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    ORF_list = ORF1.finding_ORF(seq)
    print(ORF_list)
    BLAST.blasten(ORF_list)

