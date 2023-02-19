# import java.awt.*;

#
# Created by Robert on 5/13/2014.
#

from card import Card
from cardpile import CardPile


# There is a bug that sometimes it will not move cards to the right
# Exclude checking its own column

# Enhancement: Let the DeckPile repeat
# Switch lists too Deque

class TablePile(CardPile):

    def __init__(self, x, y, c, main, canvas):
        super().__init__(x, y, canvas)
        self.c = c
        self.canvas = canvas
        self.main = main
        # print("In TablePile, c is: ", c)
        for i in range(c):  # this needs to be c after testing
            self.add_card(self.main.deckPile.pop())  # type needs to be Card

        # flip topmost card face up
        self.top().flip()

    def includes(self, tx, ty):
        # don't test bottom of card
        return self.x <= tx <= (self.x + Card.width) and self.y <= ty

    def can_take(self, a_card):
        # print("In TablePile can take: ", a_card.rank() + 1, a_card.suit())
        if len(self.thePile) == 0:
            return a_card.rank() == 12
        top_card = self.top()
        return (a_card.color() != top_card.color()) and (a_card.rank() == top_card.rank() - 1)

    # break up into smaller funcs
    def get_face_up_cards(self):
        face_up_cards = []
        while not self.is_empty() and self.top().face_up:
            face_up_cards.append(self.pop())

        return face_up_cards

    def select(self):
        if self.is_empty():
            return
        top_card = self.top()
        if not top_card.face_up:
            top_card.flip()
            return

        top_card = self.pop()
        for sp in self.main.suitPile:
            if sp.can_take(top_card):
                sp.add_card(top_card)
                if not self.is_empty():
                    new_top_card = self.top()
                    if not new_top_card.face_up:
                        new_top_card.flip()
                return
        self.add_card(top_card)

        # needs to be refactored
        # Check tableau returns a boolean, not used
        self.check_tableau()

    def check_tableau(self):
        face_up_cards = self.get_face_up_cards()
        for i, tb in enumerate(self.main.tableau):
            if self.c != i + 1:
                if tb.can_take(face_up_cards[-1]):
                    while len(face_up_cards) > 0:
                        tb.add_card(face_up_cards.pop())

                    if not self.is_empty():
                        top_card = self.top()
                        if not top_card.face_up:
                            top_card.flip()
                    return

        # need to put cards back on if no can_take
        while len(face_up_cards) > 0:
            self.add_card(face_up_cards.pop())

    def display(self):
        local_y = self.y
        for aCard in self.thePile:
            aCard.draw(self.x, local_y, self.canvas)
            local_y += 35
