from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        print(f"You rolled a {randint(1, self.sides)}")


dice_1 = Dice(6)
dice_2 = Dice(10)
dice_3 = Dice(20)

for _ in range(10):
    dice_3.roll_dice()
