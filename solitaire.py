from card import Card
from cardpile import DeckPile
from cardpile import DiscardPile
from cardpile import SuitPile
from cardpile import TablePile

from tkinter import *
from collections import deque

# This version works with multi-card move.

# Keep track of wins and losses
# undo move


class GameConfig:
    FRAME_WIDTH = 450
    FRAME_HEIGHT = 600
    DECK_PILE_X = 335
    DECK_PILE_Y = 30
    DISCARD_PILE_X = 268
    DISCARD_PILE_Y = 30
    SUIT_PILE_Y = 30
    TABLE_PILE_Y = Card.height + 35


class Solitaire(Frame):
    deckPile = deque()
    discardPile = deque()
    tableau = deque()
    suitPile = deque()
    cardPile = deque()  # CardPile

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Python Solitaire!!")
        self.master.geometry(f"{GameConfig.FRAME_WIDTH}x{GameConfig.FRAME_HEIGHT}")

        # Restart
        self.restart_button = Button(self, text="Restart", command=self.restart)
        self.restart_button.pack(side=BOTTOM)

        self.myCanvas = Canvas(self, width=GameConfig.FRAME_WIDTH,
                               height=GameConfig.FRAME_HEIGHT, background="green")
        self.myCanvas.pack(side="bottom", fill="both", expand=True)

        self.myCanvas.bind("<Button-1>", self.mouse_pressed)

        self.allPiles = deque()

        self.init()

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
        self.myCanvas.update()  # Force canvas update
        self.myCanvas.delete('all')

        self.deckPile = DeckPile(GameConfig.DECK_PILE_X, GameConfig.DECK_PILE_Y, self, self.myCanvas)
        self.allPiles.append(self.deckPile)
        self.discardPile = DiscardPile(GameConfig.DISCARD_PILE_X, GameConfig.DISCARD_PILE_Y, self, self.myCanvas)
        self.allPiles.append(self.discardPile)

        for i in range(4):
            self.suitPile.append(SuitPile(15 + (Card.width + 10) * i, GameConfig.SUIT_PILE_Y, self.myCanvas))
            self.allPiles.append(Solitaire.suitPile[i])

        for i in range(7):
            self.tableau.append(TablePile(15 + (Card.width + 5) * i, GameConfig.TABLE_PILE_Y, i + 1, self, self.myCanvas))
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
