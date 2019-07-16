class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'
	way_of_move = 'fly'


class Chicken(Bird):
	way_of_move = 'walk'


summer = Chicken()
print(summer.have_feather)
print(summer.way_of_move)