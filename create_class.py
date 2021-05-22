class Animal:
	def __init__(self, name , weight):
		self.name=name
		self.weight= weight

	def greater_than(self,animal2):
		weight2 = animal2.weight
		print(f'{self.weight > weight2}')


	def __str__(self):
		return(f'name: {self.name}, weight: {self.weight}')

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, name, weight, color):
		super().__init__(name , weight)
		self.color = color
	def __str__(self):
		return(f'name: {self.name}, weight: {self.weight}, color: {self.color}')

dog = Animal('dog', 23)
yellow_cat = Cat('cat', 15, 'yellow')
dog.greater_than(yellow_cat)
print(dog)
print(yellow_cat)
