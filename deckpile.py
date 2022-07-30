#
# Created by Robert on 5/13/2014.
#

import random
from card import Card
from cardpile import CardPile


class DeckPile(CardPile):

    def __init__(self, x, y, main, canvas):
        # first initialize parent
        super().__init__(x, y, canvas)
        self.canvas = canvas
        self.main = main
        # then create new deck

        #########################
        for i in range(4):
            for j in range(13):
                # use add_card??
                self.add_card(Card(i, j))  # Card needs canvas as third parm

        # shuffle the list
        # load the deque from the shuffled list
        # shuffle the cards
        random.shuffle(self.thePile)

    def select(self):

        if self.is_empty():  # self.empty
            print("\nIn deckpile, select - self is empty: ", self.is_empty())
            # take discard pile, flip it over and make it the new deckpile
            while not self.main.discardPile.is_empty():
                temp = self.main.discardPile.pop()
                if temp.faceUp():
                    temp.flip()
                self.add_card(temp)
            return

        temp = self.thePile.pop()
        self.main.discardPile.add_card(temp)
