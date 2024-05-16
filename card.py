from enum import Enum
from tkinter import font


class Suit(Enum):
    HEART = 0
    SPADE = 1
    DIAMOND = 2
    CLUB = 3


class Card:
    width = 50
    height = 70

    def __init__(self, suit, rank, canvas):
        self.suit = suit
        self.rank = rank
        self.face_up_value = False

    def suit(self):
        return self.suit

    def rank(self):
        return self.rank

    def face_up(self):
        return self.face_up_value

    def flip(self):
        self.face_up_value = not self.face_up_value

    def _color(self):
        if self.face_up_value:
            if self.suit == Suit.HEART.value or self.suit == Suit.DIAMOND.value:
                return "red"
            else:
                return "black"
        return "blue"

    def draw_heart(self, x, y, canvas):
        canvas.create_polygon([x+25, y+30, x+35, y+20, x+45, y+30,
                              x+25, y+60, x+5, y+30, x+15, y+20, x+25, y+30],
                              outline="red", fill="red", width=2)
    def draw_spade(self, x, y, canvas):
        canvas.create_polygon([x+15, y+45, x+25, y+25, x+35, y+45, x+35, y+45,
                           x+23, y+45, x+20, y+55, x+30, y+55, x+27, y+45],
                            outline="black", fill="black", width=2)
    def draw_diamond(self, x, y, canvas):
        canvas.create_polygon([x+10, y+35, x+25, y+15, x+40, y+35, x+25, y+55],
                              outline="red", fill="red", width=2)

    def draw_club(self, x, y, canvas):
        canvas.create_oval(x + 20, y + 25, x + 30, y + 35, outline="black", fill="black", width=2)
        canvas.create_oval(x + 25, y + 35, x + 35, y + 45, outline="black", fill="black", width=2)
        canvas.create_oval(x + 15, y + 35, x + 35, y + 45, outline="black", fill="black", width=2)
        # Base
        canvas.create_line(x + 23, y + 45, x + 20, y + 55, fill="black", width=2)
        canvas.create_line(x + 20, y + 55, x + 30, y + 55, fill="black", width=2)
        canvas.create_line(x + 30, y + 55, x + 27, y + 45, fill="black", width=2)

    def draw(self, x, y, canvas):
        # function to solitaire
        names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # clear rectangle
        canvas.create_rectangle(x, y, x + Card.width, y + Card.height, fill="white")
        # draw border
        canvas.create_rectangle(x, y, x + Card.width, y + Card.height, outline="blue")

        # draw body of card
        # get the color, red or black

        if self.face_up_value:
            bold_font = font.Font(family="Helvetica", size=12, weight="bold")
            canvas.create_text(x+5, y+15, text=names[self.rank], font=bold_font, fill=self._color())
            if self.suit == Suit.HEART.value:
                self.draw_heart(x, y, canvas)

            elif self.suit == Suit.SPADE.value:
                self.draw_spade(x, y, canvas)

            elif self.suit == Suit.DIAMOND.value:
                self.draw_diamond(x, y, canvas)

            elif self.suit == Suit.CLUB.value:
                self.draw_club(x, y, canvas)

        else:  # face down
            canvas.create_line(x + 15, y + 5, x + 15, y + 65, fill=self._color())
            canvas.create_line(x + 35, y + 5, x + 35, y + 65, fill=self._color())
            canvas.create_line(x + 5, y + 20, x + 45, y + 20, fill=self._color())
            canvas.create_line(x + 5, y + 35, x + 45, y + 35, fill=self._color())
            canvas.create_line(x + 5, y + 50, x + 45, y + 50, fill=self._color())
