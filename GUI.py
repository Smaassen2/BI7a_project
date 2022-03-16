import tkinter
from tkinter import messagebox


class GUI:
    def _init_(self):
        # Maak de window aan
        self.main_window = tkinter.Tk()

        # Maak twee frames aan (top en bottom)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak een label aan
        self.label1 = tkinter.Label(self.top_frame,
                                    text="Was het maar vakantie!")
        self.label2 = tkinter.Label(self.top_frame,
                                    text="Hello world")
        # Maak een button aan
        self.knopje = tkinter.Button(self.bottom_frame,  # Waar komt de knop
                                     text="Klik hier!",  # Text in de knop
                                     command=self.do_something) # Wat te doen bij klik
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text= "quit",
                                          command=self.main_window.destroy)
        # PLaats de label in de GUI
        self.label1.pack()
        self.label2.pack()

        # Plaats de frames in de GUI
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Plaats de buttons in de GUI
        self.knopje.pack(side = "left")
        self.quit_button.pack(side="left")

        # Zorg dat de GUI tevoorschijn komt
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response",
                                    "Bedankt voor het klikken")


if __name__ == '__main__':
    myGUI = GUI()