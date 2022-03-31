# Created by: Shahiel Maassen
# Created Date: 22-03-2022
# Version: 9.0
# The found ORFs in the created ORF list will be blast using qblast
from Bio.Blast import NCBIWWW


class BLAST:
    def blasts(list_of_orfs):
        """Every seq in the list will be blast by using qblast. The
        used blast is BLASTN. The used filters are a e_value filter and
        the amount of hits. All hits will be add to a XML file.

        :param
        list_of_orfs - List - List with ORFs

        :return:
        xmlfile - xml file - file with all data of the ORFs.
        """
        try:
            index = 0
            # Loop through all the sequences in the list_of_orfs
            for sequence in list_of_orfs:
                print("Start", index)
                print("Start BLAST...")
                # Blast of all the sequences against the non-redunant
                # database
                result_handle = NCBIWWW.qblast("blastn", "nr", sequence,
                                               expect=0.01,
                                               hitlist_size=10)
                print("BLAST results in variable")
                xmlfile = "Resultats.xml"
                # Append all the data to the XML file
                with open(xmlfile, "a") as out_handle:
                    out_handle.write(result_handle.read())
                # prints that the job is done for that specific seq
                print("The end", index)
                index += 1

        except MemoryError:
            print("The operator has no memory left in the function "
                  "blasts")
        except NameError:
            print("Job name or variable name does not exist in the "
                  "function blasts")
        except TypeError:
            print("One or more variables in the function blasts does "
                  "not have the correct variable type(s).")
        except SyntaxError:
            print("An invalid syntax has been found in the function "
                  "blasts")

