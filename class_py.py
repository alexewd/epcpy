# First class
class Goat():
	name = ' '
	age = 0
	wight = 0.0

	def show(self):
		print(self.name)
		print(self.age)
		print(self.wight)

goat = Goat()

goat.name = 'Julia'
goat.age = 2
goat.wight = 2.0

goat.show()
