class Roll(object):
    def __init__(self, dice_type, roll_value):
        self.dice_type = dice_type
        self.roll_value = roll_value

    def __str__(self):
        return "Roll{Dice type = %s, Roll value = %s}" % (self.dice_type, self.roll_value)

    def __repr__(self):
        return "Roll{Dice type = %s, Roll value = %s}" % (self.dice_type, self.roll_value)