import tkinter as tk
from tkinter import messagebox

#window aanmaken
window = tk.Tk()
#titel window
window.title("ORF finder & BLASTN")
#afmetingen window
window.geometry("500x300")

#labels maken
dna_seq_invoer = tk.Label(text="Voer hier je DNA sequentie in: ")
#label packen
dna_seq_invoer.pack()

#invoerveld maken
entry = tk.Entry()
#invoerveld packen
entry.pack()

#button maken
button = tk.Button(text="Start opdracht")
#button packen
button.pack()



#window weergeven
window.mainloop()
