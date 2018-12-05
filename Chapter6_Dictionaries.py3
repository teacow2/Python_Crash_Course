# Exercise 6-1

myFriend = {'first_name': 'Jed', 'last_name': 'Whatevers', 'age': '23', 'city':'Cleveland'}

print('My friend ' + myFriend['first_name'] + ' ' + myFriend['last_name'] + ' is ' + myFriend['age'] + ' and lives in ' + myFriend['city'] + '.')

# Exercise 6-2 + 6-10

favNum = {'Amy': ['23','41'], 'Bill': ['13','3','813'], "Cassie": '7', "Donald": ['75', '12'], "Erica": ['30', '0','66']}
for key, value in favNum.items():
	print(key + "'s favorite numbers:", end=' ')
	for numero in value:
		print(numero, end=' ')
	print('\n')

# Exercise 6-3 and 6-4
spanishWords= {'entonces': 'then', 'a veces': 'sometimes', 'cada ves': 'every time', 'siempre': 'always', 'nunca': 'never'}
for key, value in spanishWords.items():
	print(key + ' means ' + value + '.')

# Exercise 6-5
riverCountries = {'nile': 'egypt', 'mississippi': 'america', 'ganges': 'india'}
for river, country in riverCountries.items():
	print('The ' + river.title() + ' is in ' + country.title())

for river in riverCountries.keys():
	print(river.title())

for country in riverCountries.values():
	print(country.title())

# Exercise 6-6
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'javascript', 'phil': 'processing'}
need_poll = ['adam', 'edward', 'fran', 'jen', 'sarah']

for name in need_poll:
	if name not in favorite_languages.keys():
		print(name.title() + ', please take the language poll.')
	else:
		print(name.title() + ', thanks for taking the language poll.')

# Exercise 6-7 
myFriend2 = {'first_name': 'Kelly', 'last_name': 'Youknow', 'age': '32', 'city':'Boise'}
myFriend3 = {'first_name': 'Lenora', 'last_name': 'Zilch', 'age': '43', 'city':'Fresno'}
people = [myFriend, myFriend2, myFriend3]

for person in people:
	print('My friend ' + person['first_name'] + " " + person['last_name'] + ' is ' + person['age'] + ' and lives in ' + person['city'] + '.')

# Exericse 6-8
bellaboo = {'name': 'bellaboo', 'type': 'cat', 'owner': 'margaret'}
jackson = {'name': 'jackson','type': 'dog', 'owner': 'melanie'}
rufus = {'name': 'rufus','type': 'rat', 'owner': 'jimmy'}
diablo = {'name': 'diablo','type': 'parrot', 'owner': 'elise'}

pets = [bellaboo, jackson, rufus, diablo]

for pet in pets:
	print(pet['name'].title() + ' is a ' + pet['type'] + ' owned by ' + pet['owner'].title() + '.')


# Exercise 6-9
people_places = {'ema': ['paris', 'lagos'], 'frank': ['seoul', 'mendoza'], 'greta': ['toronto', 'sydney', 'memphis']}
for key, value in people_places.items():
	print(key.title() + "'s favorite places are:", end=' ')
	for city in value:
		print(city.title(), end=' ')
	print('\n')

# Exercise 6-11 + 6-12
cities = {'new york': {'country': 'america', 'population': '8 million', 'currency': 'dollars'}, 'berlin': {'country': 'germany', 'population': '5 million', 'currency': 'euro'}, 'tokyo': {'country': 'japan', 'population': '6 million', 'currency': 'yen'}}
for key,value in cities.items():
	print(key.title() + ' is in ' + value['country'].title()+ ' with a population of ' + value['population'] + ' and a currency in ' + value['currency'] + '.')
