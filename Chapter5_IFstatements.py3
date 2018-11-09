#5-1 and 5-2
names = ['Andy', 'Betty', 'Carla', 'Dominic', 'Evelyn']
ages = [21,19, 20, 14, 30]

print("if names[0] == andy, print true")
print(names[0] == 'Andy')

print("if names[1] == andy print true")
print(names[1] == 'Andy')
print("what about if it DOESN'T equal andy")
print(names[1] != 'Andy')

print("does names[0] == andy?")
print(names[0] == 'andy')
print("what about names[0].lower()")
print(names[0].lower() == 'andy')

print("is Carla's age equal to 20?")
if ages[2] == 20:
	print("yes")

print("is Carla's age equal to 30?")
if ages[2] != 30:
	print("no")

nameNum = 0
for age in ages:
	if age >= 21:
		print(names[nameNum] + ' can legally drink.')
	else:
		print(names[nameNum] + ' can not legally drink.')
	if age>=20 and age<30:
		print(names[nameNum] + ' is in their 20s.')
	if age==20 or age==30:
		print(names[nameNum] + ' had a big birthday this year!')
	nameNum+=1

print('is dominic on of us?')
if 'Dominic' in names:
	print('yes')
else:
	print('no')

print('is francis one of us?')
if 'francis' in names:
	print('yes')
else:
	print('no')

print('gladis is not one of us, right?')
if 'gladis' not in names:
	print('No, she is not.')
else:
	print('Yes, she is')

#5-3, 5-4, 5-5

alien_color = 'green'
if alien_color == 'green':
	print("You earned 5 points.")
else:
	print("You earned nothing.")

print("Next round:")
if alien_color == 'green':
	print('You earned 5 points')
else:
	print('You earned 10 points.')

print('Next alien is red')
alien_color = 'red'
if alien_color == 'green':
	print('You earned 5 points')
else:
	print('You earned 10 points.')

alien_colors = ['red', 'green', 'yellow']
for color in alien_colors:
	if color == 'red':
		print(color + " alien earns 15 points.")
	elif color == 'green':
		print(color + ' alien earns 5 points.')
	else:
		print(color + ' alien earns 10 points.')

#5-6
age = 14
if age<2:
	print("You are a baby.")
elif age>=2 and age<=4:
	print("You are a toddler.")
elif age>4 and age<13:
	print("You are a tween.")
elif age>= 13 and age<20:
	print('You are a teenager.')
elif age>=20 and age<65:
	print('You are an adult.')
elif age>=65:
	print('You are a senior citizen.')


#5-7
favorites = ['peaches', 'bananas', 'blueberries']
if 'peaches' in favorites:
	print('Peaches are one of your favorite fruits.')
if 'bananas' in favorites:
	print('Bananas are one of your favorite fruits.')
if 'pears' in favorites:
	print('Pears are one of your favorite fruits.')
if 'apples' in favorites:
	print('Apples are one of your favorite fruits.')
if 'blueberries' in favorites:
	print('Blueberries are one of your favorite fruits.')

#5-9 and 5-10 and 5-11
users = ["Jack", "admin", "Samantha", "Gregor", "Dana"]
for user in users:
	if user == 'admin':
		print("All hail " + user.title())
	else:
		print('Hello ' + user.title())

if users:
	print('')
else:
	print('We need users.')

users = []
if users:
	print('')
else:
	print('We need users.')

users = ["Jack", "admin", "Samantha", "Gregor", "DaNa"]
current_users = ['tim', 'jack', 'dana', 'john', 'lisa']
for user in users:
	if user.lower() in current_users:
		print('Sorry, ' + user + ", you need to pick a new user name")

# 5-12
for value in range(1, 10):
	if value == 2:
		print(str(value) + 'nd')
	elif value == 1:
		print(str(value) + 'st')
	elif value == 3:
		print(str(value) + 'rd')
	else: 
		print(str(value) + 'th')
