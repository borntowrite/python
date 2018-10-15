class Robot():
    a, b = 11, 22
    population = 0
    def __init__(self, name):
        self.name = name
        Robot.population += 1
    @classmethod
    def how_many(cls):
        print(cls.population)


robo1 = Robot('Transformer')
print(robo1.a)
print(robo1.name)
robo1.how_many()
robo2 = Robot('Monster')
print(robo2.a)
print(robo2.name)
robo2.how_many()