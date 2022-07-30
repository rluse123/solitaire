

class Card:
    width = 50
    height = 70

    heart = 0
    spade = 1
    diamond = 2
    club = 3

    def __init__(self, sv, rv):

        self.s = sv
        self.r = rv
        self.face_up = False

    def rank(self):
        return self.r

    def suit(self):
        return self.s

    def faceUp(self):
        return self.face_up

    def flip(self):
        self.face_up = not self.face_up

    def color(self):
        if self.faceUp():
            if self.suit() == self.heart or self.suit() == self.diamond:
                return "red"
            else:
                return "black"
        return "yellow"

    def draw(self, x, y, canvas):
        # function to solitaire
        names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # clear rectangle
        canvas.create_rectangle(x, y, x+Card.width, y+Card.height, fill="white")
        # draw border
        canvas.create_rectangle(x, y, x+Card.width, y+Card.height, outline="blue")

        # draw body of card
        # get the color, red or black

        if self.faceUp():
            canvas.create_text(x + 5, y + 15, text=names[self.rank()], fill=self.color())
            if self.suit() == self.heart:
                canvas.create_line(x + 25, y + 30, x + 35, y + 20, fill=self.color())
                canvas.create_line(x + 35, y + 20, x + 45, y + 30, fill=self.color())
                canvas.create_line(x + 45, y + 30, x + 25, y + 60, fill=self.color())
                canvas.create_line(x + 25, y + 60, x + 5, y + 30, fill=self.color())
                canvas.create_line(x + 5, y + 30, x + 15, y + 20, fill=self.color())
                canvas.create_line(x + 15, y + 20, x + 25, y + 30, fill=self.color())
            elif self.suit() == self.spade:
                canvas.create_line(x + 15, y + 45, x + 25, y + 25, fill=self.color())
                canvas.create_line(x + 25, y + 25, x + 35, y + 45, fill=self.color())
                canvas.create_line(x + 15, y + 45, x + 35, y + 45, fill=self.color())
                # Base
                canvas.create_line(x + 23, y + 45, x + 20, y + 55, fill=self.color())
                canvas.create_line(x + 20, y + 55, x + 30, y + 55, fill=self.color())
                canvas.create_line(x + 30, y + 55, x + 27, y + 45, fill=self.color())
            elif self.suit() == self.diamond:
                canvas.create_line(x + 10, y + 35, x + 25, y + 15, fill=self.color())
                canvas.create_line(x + 25, y + 15, x + 40, y + 35, fill=self.color())
                canvas.create_line(x + 40, y + 35, x + 25, y + 55, fill=self.color())
                canvas.create_line(x + 25, y + 55, x + 10, y + 35, fill=self.color())
            elif self.suit() == self.club:
                canvas.create_oval(x + 20, y + 25, x+30, y+35, outline=self.color())
                canvas.create_oval(x + 25, y + 35, x+35, y+45, outline=self.color())
                canvas.create_oval(x + 15, y + 35, x+35, y+45, outline=self.color())
                # Base
                canvas.create_line(x + 23, y + 45, x + 20, y + 55, fill=self.color())
                canvas.create_line(x + 20, y + 55, x + 30, y + 55, fill=self.color())
                canvas.create_line(x + 30, y + 55, x + 27, y + 45, fill=self.color())
        else:  # face down
            canvas.create_line(x + 15, y + 5, x + 15, y + 65, fill=self.color())
            canvas.create_line(x + 35, y + 5, x + 35, y + 65, fill=self.color())
            canvas.create_line(x + 5, y + 20, x + 45, y + 20, fill=self.color())
            canvas.create_line(x + 5, y + 35, x + 45, y + 35, fill=self.color())
            canvas.create_line(x + 5, y + 50, x + 45, y + 50, fill=self.color())
