class Base:
	__nb_objects = 0


	#class constructor
	def __init__(self, id=None):
		if id is not None:
			self.id = id
