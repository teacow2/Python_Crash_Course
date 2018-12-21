#Exercise 8-1

def display_message():
	""" Just a stupid print function """
	print("I'm learning how functions work in Python.")

display_message()

#Exercise 8-2 
def favorite_book(name):
	""" Prints the paramater in the sentence"""
	print('One of my favorite books is ' + name.title() + '.')

favorite_book('Huckleberry Finn')

# Exercise 8-3 + 8-4

def tshirt_make(copy='I love Python', size='L'):
	print('This T-shirt is a size ' + size + ' and says ' + copy.title() + '.')

tshirt_make('Kiss my Grits', 'XL')
tshirt_make(size='M', copy='just do it')
tshirt_make(copy='born to ride')
tshirt_make(size='M')
tshirt_make()

# Exercise 8-5 
def describe_city(city, country='the world'):
	print(city.title() + ' is a city of ' + country.title() + '.')

describe_city('paris', 'france')
describe_city('lagos', 'nigeria')
describe_city('reykjavik')

# Exercise 8-6
def city_country(city, country):
	combination = city + ', ' + country
	return combination

north = city_country('Moscow', 'Russia')
south = city_country('Mendoza', 'Argentina')
middle = city_country('Calcutta', 'India')

print(north)
print(south)
print(middle)	
# Exercise 8-7
def make_album(musician, name, tracks=''):
	if tracks:
		album = {'musician': musician, 'title': name, 'tracks': str(tracks)}
	else:
		album = {'musician': musician, 'title': name}
	return album

albums = []

albums.append(make_album('Pavement', 'Crooked Rain, Crooked Rain', 10))
albums.append(make_album('Parquet Courts', 'Wide Awake'))
albums.append(make_album('Speedy Ortiz', 'Twerk Verse', 12))

for thing in albums:
	print(thing)

#Exercise 8-8 
def make_album_2(musician, name):
	draft_album = {'musician': musician, 'title': name}
	return draft_album

while True: 
	album_title = input('What is the name of the artist? ')
	if album_title == 'quit':
		print('Thank you for listing albums.')
		break
	album_name = input('What is the album name? ')
	if album_name == 'quit':
		print('Thank you for listing albums')
		break
	print(make_album_2(album_title, album_name))

# Exercise 8-9 + 8-10 + 8-11
print('One List!')

def make_great(name):
	name += ' The Great'
	return name

known_magicians = ['Merlin', 'Gandalf', 'Saruman']
for each in range(len(known_magicians)):
	known_magicians[each] = make_great(known_magicians[each])


print(known_magicians)
print('\n')

# Exercise 8-11
def make_great_2(roster):
	temp_list = []
	for each in roster:
		each += ' The Great'
		temp_list.append(each)

	return temp_list

known_magicians = ['Merlin', 'Gandalf', 'Saruman']
great_magicians = make_great_2(known_magicians)
print("Both Lists!")
print(known_magicians)
print(great_magicians)

# Exercise 8-12
def sandwich_parts(*components):
	print('The sandwich contains:')
	for component in components:
		print(component)

sandwich_parts('cheese')
sandwich_parts('pastrami','swiss')
sandwich_parts('lettuce','tomato','ham','cheese','mortadella')

# Exericse 8-13
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

my_profile = build_profile('nick', 'fortugno', location='NYC', hobby='dancing', height='tall')

print(my_profile)

# Exercise 8-14
def car_model(manu, model, **car_info):
	car = {}
	car['manufacturer'] = manu
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car

my_car = car_model('honda', 'elantra', color='white', year='2015')
print(my_car)

# Exercise 8-15 + 8-16 + 8-17
from printing_functions import car_model as pf 

my_car = pf('buick', 'capata', color='green', year='2014')
print(my_car)