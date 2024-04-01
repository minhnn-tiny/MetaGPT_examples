import set

class PermutNumber:
    def __init__(self, number):
        self.number = number
        self.digits = set(str(number))

    def is_permut(self):
        return len(self.digits) == len(str(self.number * 2))
