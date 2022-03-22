from Bio.Blast import NCBIWWW


def lijstfilteren(bestandnaam):
    """Opent een TSV bestand. Vanuit hier wordt iedere regel gestript en
    gesplitst op een tab. De sequentie en headers worden aan aparte
    nieuwe lijsten toegevoegd
    :param bestandnaam: TSV File
    :return: l_seq, l_headers
    """
    try:
        # Opent een bestand
        document = open(bestandnaam, "r")
        l_seq = []
        l_headers = []
        # Kijkt naar iedere regel van het bestand
        for line in document:
            if line != "    ":
                l_seq.append(line.strip().split("	")[1])
                l_headers.append(line.strip().split("	")[0])
                l_seq.append(line.strip().split("	")[4])
                l_headers.append(line.strip().split("	")[3])
        # Sluit een bestand
        document.close()
        return l_seq, l_headers
    except FileNotFoundError:
        print("Het bestand is niet gevonden in de functie "
              "lijstfilteren")
    except IOError:
        print("Het bestand is niet leesbaar in de functie "
              "lijstfilteren")
    except NameError:
        print("Functienaam of variabelenaam bestaat niet in de functie"
              "lijstfilteren")
    except TypeError:
        print("Een of meer variabelen in de functie lijstfilteren "
              "heeft / hebben niet de correcte variabele type(n).")


def blasten(l_seq, xmlbestand):
    """Iedere sequentie in de lijst wordt geblast door middel van
    qblast. De gebruikte blast is Blastn. De gebruikte database is
    non-redundant database. De gebruikte filters zijn een e_value filter
    en hoeveelheid hits. Alle hits zijn hierna toegevoegd aan een XML
    bestand.
    :param xmlbestand: file
    :param l_seq: list
    :return: Alle data van de sequenties in een XML bestand
    """
    try:
        index = 0
        # Loopt door iedere sequentie in de sequentie lijst heen
        for sequence in l_seq:
            print("Start", index)
            print("Start BLAST...")
            # Blasten van iedere sequentie tegen de non-redunant
            # database
            result_handle = NCBIWWW.qblast("blastn", "nr", sequence,
                                           expect=0.01, hitlist_size=10)
            print("BLAST resultaat in variabele")
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

def main():
    l_seq, l_headers = lijstfilteren("B4_seq_app.txt")
    blasten(l_seq, "De_definitieve_blast.xml")

main()
