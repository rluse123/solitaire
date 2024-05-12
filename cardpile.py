# need to handle the display method - Tkinter or PyGame

"""
Stack
is_empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
add_card(card) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop_card() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""

from card import Card
from collections import deque



class CardPile:

    def __init__(self, xl, yl, canvas):
        self.canvas = canvas
        self.x = xl
        self.y = yl
        self.thePile = deque()

    def top(self):
        return self.thePile[-1]  # Card

    def is_empty(self):
        # Checks if stack is empty.
        # return: True if empty, False otherwise.
        if len(self.thePile) == 0:
            return True
        else:
            return False

    def pop(self):
        if len(self.thePile) == 0:
            return None
        else:
            return self.thePile.pop()

    # the following are sometimes overridden
    # includes if for the gui to select the card
    def includes(self, tx, ty):
        return self.x <= tx <= self.x + Card.width and \
            self.y <= ty <= self.y + Card.height

    def select(self):
        pass

    def add_card(self, card):
        self.thePile.append(card)

    def display(self):
        if len(self.thePile) == 0:
            self.canvas.create_rectangle(self.x, self.y, self.x + Card.width, self.y + Card.height, outline="blue")
        else:
            self.top().draw(self.x, self.y, self.canvas)

    def can_take(self):
        # return False
        pass
