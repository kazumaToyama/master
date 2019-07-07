class staff:
    def __init__(self, bonus):
        self.bonus = bonus
    def salary(self):
        salary = 10000 + self.bonus
        return salary

toyama = staff(50000)
toyama.salary()