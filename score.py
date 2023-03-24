from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.goto(0, 450)
        self.color('white')
        self.write(f'{self.p1_score} : {self.p2_score}', False, 'center', ('Arial', 40, 'bold'))

    def new_point(self):
        self.clear()
        self.write(f'{self.p1_score} : {self.p2_score}', False, 'center', ('Arial', 40, 'bold'))

    def gameover(self):
        self.goto(0,0)
        if self.p1_score > self.p2_score:
            self.write('The winner is player 1!', False, 'center', ('Arial', 40, 'bold'))
        else:
            self.write('The winner is player 2!', False, 'center', ('Arial', 40, 'bold'))



