class Chiken(Bird):
	way_of_move = 'walk'
	possible_in_KFC = True
	
class Oriole(Bird):
	way_of_move = 'fly'
	possible_in_KFC = False
	
summer = Chiken()
print summer.have_feather
print summer.move(5,8)
