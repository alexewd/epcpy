# First class
class Goat():

    def __init__(self, name, age, wight):

        self.name = name
        self.age = age
        self.wight = wight

    def show(self):

        print(self.name)
        print(self.age)
        print(self.wight)


goat = Goat('Irisha',2,3.0)

# goat.name = 'Julia'
# goat.age = 2
# goat.wight = 2.0

goat.show()
