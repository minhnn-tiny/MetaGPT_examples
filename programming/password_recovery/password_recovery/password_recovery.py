import random
import string

class PasswordRecovery:
    def __init__(self, password, k):
        self.password = password
        self.k = k

    def generate_combinations(self):
        combinations = []
        for i in range(len(self.password) + 1):
            for j in range(self.k + 1):
                combination = self.password[:i] + ''.join(random.choices(string.ascii_lowercase, k=j)) + self.password[i:]
                combinations.append(combination)
        return combinations

    def find_correct_combination(self):
        combinations = self.generate_combinations()
        for combination in combinations:
            if combination == self.password:
                return combination
        return None

    def count_unsuccessful_attempts(self):
        correct_combination = self.find_correct_combination()
        if correct_combination is None:
            return -1
        return len(combinations) - 1
