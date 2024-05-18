# need to handle the display method - Tkinter or PyGame

"""
Stack
is_empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
add_card(card) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop_card() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""
from typing import List

from card import Card
from collections import deque
import random
from tkinter import Canvas

CARD_WIDTH = Card.width
CARD_HEIGHT = Card.height
OUTLINE_COLOR = "blue"


class CardPile:

    def __init__(self, pos_x: int, pos_y: int, canvas: Canvas):
        self.canvas = canvas
        self.x = pos_x
        self.y = pos_y
        self.thePile = deque()

    def top(self) -> Card:
        return self.thePile[-1]  # Card

    def is_empty(self) -> bool:
        # Checks if stack is empty.
        # return: True if empty, False otherwise.
        return len(self.thePile) == 0

    def pop(self) -> Card | None:
        if self.is_empty():
            return None
        else:
            return self.thePile.pop()

    def is_target_within_card_boundaries(self, target_x: int, target_y: int) -> bool:
        return self.x <= target_x <= self.x + CARD_WIDTH and \
            self.y <= target_y <= self.y + CARD_HEIGHT

    # the following are sometimes overridden
    # includes if for the gui to select the card
    def includes(self, target_x: int, target_y: int) -> bool:
        return self.is_target_within_card_boundaries(target_x, target_y)

    def select(self):
        pass

    def add_card(self, card: Card) -> None:
        self.thePile.append(card)

    def display(self) -> None:
        if self.is_empty():
            self.canvas.create_rectangle(
                self.x, self.y, self.x + CARD_WIDTH,
                self.y + CARD_HEIGHT, outline=OUTLINE_COLOR)
        else:
            self.top().draw(self.x, self.y, self.canvas)

    def card_can_be_taken(self, card) -> bool:
        # return False
        pass


class DeckPile(CardPile):

    def __init__(self, pos_x: int, pos_y: int, main, canvas: Canvas):
        # first initialize parent
        super().__init__(pos_x, pos_y, canvas)
        self.canvas = canvas
        self.main = main
        # then create new deck

        #########################
        for suit in range(4):
            for rank in range(13):
                self.add_card(Card(suit, rank, canvas))  # Card needs canvas as third parm

        # shuffle the list
        # load the deque from the shuffled list
        # shuffle the cards
        random.shuffle(self.thePile)

    def select(self):

        if self.is_empty():  # self.empty
            # print("\nIn deck pile, select - self is empty: ", self.is_empty())
            # take discard pile, flip it over and make it the new deck pile
            while not self.main.discardPile.is_empty():
                temp = self.main.discardPile.pop()
                if temp.face_up():
                    temp.flip()
                self.add_card(temp)
            return

        temp = self.thePile.pop()
        self.main.discardPile.add_card(temp)


class DiscardPile(CardPile):

    def __init__(self, x: int, y: int, main, canvas: Canvas):
        super().__init__(x, y, canvas)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.main = main

    def add_card(self, card: Card) -> None:

        if not card.face_up():  # use method instead??
            card.flip()
        self.thePile.append(card)  # self.add_card???

    def select(self) -> None:

        if self.is_empty():
            return

        top_card = self.pop()

        for sp in self.main.suitPile:
            if sp.card_can_be_taken(top_card):
                sp.add_card(top_card)
                return

        for tp in self.main.tableau:
            if tp.card_can_be_taken(top_card):
                tp.add_card(top_card)
                return

        # nobody can use it, put it back on our list
        assert top_card is not None
        self.add_card(top_card)


class SuitPile(CardPile):

    def __init__(self, pos_x: int, pos_y: int, canvas: Canvas):
        super().__init__(pos_x, pos_y, canvas)
        self.canvas = canvas

    def card_can_be_taken(self, card: Card) -> bool:

        if self.is_empty():
            return card.rank == 0

        top_card = self.top()
        return card.suit == top_card.suit and \
            card.rank == 1 + top_card.rank


# There is a bug that sometimes it will not move cards to the right
# Exclude checking its own column - fixed??

class TablePile(CardPile):

    def __init__(self, x_position: int, y_position: int,
                 column_length: int, main, canvas: Canvas):
        super().__init__(x_position, y_position, canvas)
        self.column_length = column_length
        self.canvas = canvas
        self.main = main
        # print("In TablePile, c is: ", c)
        for i in range(self.column_length):  # this needs to be c after testing
            self.add_card(self.main.deckPile.pop())  # type needs to be Card

        # flip topmost card face up
        self.top().flip()

    def includes(self, tx: int, ty: int) -> bool:
        # don't test bottom of card
        return self.x <= tx <= (self.x + Card.width) and self.y <= ty

    def card_can_be_taken(self, card: Card) -> bool:
        # print("In TablePile can take: ", card.rank() + 1, card.suit())
        if len(self.thePile) == 0:
            return card.rank == 12
        top_card = self.top()
        return (card._color() != top_card._color()) and (card.rank == top_card.rank - 1)

    # break up into smaller funcs
    def get_face_up_cards(self) -> List[Card]:
        face_up_cards = []
        while not self.is_empty() and self.top().face_up():
            face_up_cards.append(self.pop())

        return face_up_cards

    def select(self) -> None:
        if self.is_empty():
            return
        top_card = self.top()
        if not top_card.face_up():
            top_card.flip()
            return

        top_card = self.pop()
        for sp in self.main.suitPile:
            if sp.card_can_be_taken(top_card):
                sp.add_card(top_card)
                if not self.is_empty():
                    new_top_card = self.top()
                    if not new_top_card.face_up():
                        new_top_card.flip()
                return
        self.add_card(top_card)

        # needs to be refactored
        # Check tableau returns a boolean, not used
        self.check_tableau()

    def check_tableau(self) -> None:
        face_up_cards = self.get_face_up_cards()
        for i, tb in enumerate(self.main.tableau):
            if self.column_length != i + 1:
                if tb.card_can_be_taken(face_up_cards[-1]):
                    while len(face_up_cards) > 0:
                        tb.add_card(face_up_cards.pop())

                    if not self.is_empty():
                        top_card = self.top()
                        if not top_card.face_up():
                            top_card.flip()
                    return

        # need to put cards back on if no card_can_be_taken
        while len(face_up_cards) > 0:
            self.add_card(face_up_cards.pop())

    def display(self) -> None:
        local_y = self.y
        for card in self.thePile:
            card.draw(self.x, local_y, self.canvas)
            local_y += 35
