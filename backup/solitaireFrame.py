import tkinter as tk
from tkinter import Frame

from pysoly.deckPile import DeckPile
from pysoly.discardPile import DiscardPile
from pysoly.cardPile import CardPile
from pysoly.card import Card
from pysoly.suitPile import SuitPile
from pysoly.tablePile import TablePile


# Where are the cards actually drawn on the tableau"
# Card needs draw fixed
# Card needs to have all its writes converted
# CardPile needs display fixed


class Solitaire:
    def __init__(self):
        print('in Solitaire init')
        self.deckPile = DeckPile(335, 50, self)
        self.discardPile = DiscardPile(268, 50, self)

        self.tableau = []
        self.suitPile = []
        self.allPiles = []

        # allPiles[0] is deckPile
        self.allPiles.append(CardPile)
        self.allPiles[0] = self.deckPile

        # allPiles[1] is discardPile
        self.allPiles.append(CardPile)
        self.allPiles[1] = self.discardPile

        # For (Type iterator: collection of T)
        for i in range(4):
            self.allPiles.append(CardPile)
            self.suitPile.append(SuitPile(15 + (Card.width + 10) * i, 50, self))
            self.allPiles[i + 2] = self.suitPile[i]

        for i in range(7):
            self.allPiles.append(CardPile)
            self.tableau.append(TablePile(15 + (Card.width + 5) * i, Card.height + 55, i + 1, self))
            self.allPiles[i + 6] = self.tableau[i]


class SolitaireFrame(Frame):

    def __init__(self):

        # initialize GUI
        Frame.__init__(self)
        self.pack(expand=tk.constants.YES, fill=tk.constants.BOTH)
        self.master.title("Solitaire!!!")
        self.master.geometry("600x600")

        self.bind("<ButtonRelease-1>", self.mouse_pressed)

        self.restartButton = tk.Button(self, text="New Game", command=self.restart)
        self.restartButton.pack(side=tk.BOTTOM)

        self.solitaire = Solitaire()

        self.redraw()

    def restart(self):
        # self.callback.init()
        print("Button Pressed")
        # clear the screen
        # self.solitaire = Solitaire()

        # Need python equivalents for mousePressed and paint

    def mouse_pressed(self, event):

        # now get the mouse position
        x, y = event.x, event.y

        for i in range(13):
            if self.solitaire.allPiles[i].includes(x, y):
                self.solitaire.allPiles[i].select(x, y)
                # As the last step after clicking the mouse refresh the tables
                self.redraw()

    def redraw(self):

        # clear the screen first
        for i in range(13):
            self.solitaire.allPiles[i].display()


if __name__ == "__main__":
    SolitaireFrame().mainloop()
