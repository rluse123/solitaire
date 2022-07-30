#
# Created by Robert on 5/13/2014.
#

from cardpile import CardPile


class SuitPile(CardPile):

    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.canvas = canvas

    def can_take(self, a_card):
        if self.is_empty():
            return a_card.rank() == 0

        top_card = self.top()
        return a_card.suit() == top_card.suit() and \
            a_card.rank() == 1 + top_card.rank()
