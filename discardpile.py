#
# Created by Robert on 5/13/2014.
#

from cardpile import CardPile


class DiscardPile(CardPile):

    def __init__(self, x, y, main, canvas):
        super().__init__(x, y, canvas)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.main = main

    def add_card(self, a_card):
        if not a_card.face_up:  # use method instead??
            a_card.flip()
        self.thePile.append(a_card)  # self.add_card???

    def select(self):
        if self.is_empty():
            return

        top_card = self.pop()

        for sp in self.main.suitPile:
            if sp.can_take(top_card):
                sp.add_card(top_card)
                return

        for tp in self.main.tableau:
            if tp.can_take(top_card):
                tp.add_card(top_card)
                return

        # nobody can use it, put it back on our list
        assert top_card is not None
        self.add_card(top_card)

