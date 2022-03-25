# Created by: Shahiel Maassen
# Created Date: 22-3-2022
# Version: 1.0
from Bio.Blast import NCBIWWW

class BLAST:

    def blasten(ORF_list):
        """Iedere sequentie in de lijst wordt geblast door middel van
        qblast. De gebruikte blast is Blastn. De gebruikte database is
        non-redundant database. De gebruikte filters zijn een e_value filter
        en hoeveelheid hits. Alle hits zijn hierna toegevoegd aan een XML
        bestand.
        :param tsvbestand: file
        :param l_seq: list
        :return: Alle data van de sequenties in een XML bestand
        """
        try:
            index = 0
            # Loopt door iedere sequentie in de sequentie lijst heen
            for sequence in ORF_list:
                print("Start", index)
                print("Start BLAST...")
                # Blasten van iedere sequentie tegen de non-redunant
                # database
                result_handle = NCBIWWW.qblast("blastn", "nr", sequence,
                                               expect=0.01, hitlist_size=10)
                print("BLAST resultaat in variabele")
                xmlbestand = "Resultaten.xml"
                # Append de data in een XML bestand
                with open(xmlbestand, "a") as out_handle:
                    out_handle.write(result_handle.read())
                print("eind", index)
                index += 1


        except MemoryError:
            print("De operator is out of memory in de functie blasten")
        except NameError:
            print("Functienaam of variabelenaam bestaat niet in de functie"
                  "blasten")
        except TypeError:
            print("Een of meer variabelen in de functie blasten "
                  "heeft/hebben niet de correcte variabele type(n).")
        except SyntaxError:
            print("Er is een invalide syntax gevonden in de functie "
                  "blasten")

