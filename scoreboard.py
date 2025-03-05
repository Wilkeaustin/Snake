from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(f"Score:  {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:  {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
