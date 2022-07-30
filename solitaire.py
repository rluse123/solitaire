from card import Card
from deckpile import DeckPile
from discardpile import DiscardPile
from suitpile import SuitPile
from tablepile import TablePile

from tkinter import *
from collections import deque

# This version works with multicard move.
# make method calls consistent
# remove print statements
# Then enhance - move multiple cards


class Solitaire(Frame):
    deckPile = deque()
    discardPile = deque()
    tableau = deque()
    suitPile = deque()
    cardPile = deque() # CardPile

    deckPileX = 335
    deckPileY = 30
    discardPileX = 268
    discardPileY = 30
    suitPileY = 30
    tablePileY = Card.height + 35

    frameWidth = 450
    frameHeight = 600

    cardPileSize = 13
    suitPileSize = 4
    tableauSize = 7

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Python Solitaire!!")
        self.master.geometry(f"{Solitaire.frameWidth}x{Solitaire.frameHeight}")

        # Restart
        self.restart_button = Button(self, text="Restart", command=self.restart)
        self.restart_button.pack(side=BOTTOM)

        self.myCanvas = Canvas(self, width=Solitaire.frameWidth, height=Solitaire.frameHeight, background="bisque")
        self.myCanvas.pack(side="bottom", fill="both", expand=True)

        self.myCanvas.bind("<Button-1>", self.mouse_pressed)

        self.allPiles = deque()

        self.init()

        # print("DeckPile size is: ", len(self.deckPile.thePile))
        # print("DiscardPile size is: ", len(self.discardPile.thePile))

    def restart(self):
        Solitaire.deckPile.clear()
        Solitaire.discardPile.clear()
        Solitaire.tableau.clear()
        Solitaire.suitPile.clear()
        Solitaire.cardPile.clear()  # CardPile

        self.allPiles.clear()

        self.myCanvas.delete('all')
        self.init()

    def init(self):
        # print("in init")

        self.myCanvas.update()  # Force canvas update
        self.myCanvas.delete('all')

        self.deckPile = DeckPile(Solitaire.deckPileX, Solitaire.deckPileY, self, self.myCanvas)
        self.allPiles.append(self.deckPile)
        self.discardPile = DiscardPile(Solitaire.discardPileX, Solitaire.discardPileY, self, self.myCanvas)
        self.allPiles.append(self.discardPile)

        for i in range(4):
            self.suitPile.append(SuitPile(15 + (Card.width + 10) * i, Solitaire.suitPileY, self.myCanvas))
            self.allPiles.append(Solitaire.suitPile[i])

        for i in range(7):
            self.tableau.append(TablePile(15 + (Card.width + 5) * i, Solitaire.tablePileY, i + 1, self, self.myCanvas))
            self.allPiles.append(self.tableau[i])

        self.paint_screen()

    # @staticmethod
    def mouse_pressed(self, event):
        # print("Mouse Pressed event type: ", type(event))
        # get mouse click position
        x = event.x
        y = event.y
        for i in range(13):
            if self.allPiles[i].includes(x, y):
                self.allPiles[i].select()

                self.paint_screen()

    def paint_screen(self):
        self.myCanvas.delete('all')
        for i in range(13):
            self.allPiles[i].display()


if __name__ == "__main__":
    Solitaire().mainloop()
