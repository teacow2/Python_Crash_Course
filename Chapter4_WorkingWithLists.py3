#chapter 4-1 
pizzas = ['olive','mushroom','pepperoni','spinach']
for pizza in pizzas:
	print('I like ' + pizza + ' pizza!')

print('I guess I like lots of pizza!\n')

#chapter 4-2
pets = ['cats', 'dogs', 'birds', 'fish']
for pet in pets:
	print(pet + " make great pets!")

print('There are lots of great pets!\n')

#chapter 4-3 
for value in range(1,21):
	print(value)

#chapter 4-4 and 4-5
# for value in range(1, 1000001):
#	print value 
# not running because it will take a stupid long time

milliones = list(range(1,1000001))
print(min(milliones))
print(max(milliones))
print(sum(milliones))

#chapter 4-6 
oddnums = list(range(1,20,2))
for value in oddnums:
	print(value)

#chapter 4-7
threenums = list(range(3,30,3))
for value in threenums:
	print(value)

#chapter 4-8 
cubes = []
for value in range(1,11):
	cubes.append(value**3)

print(cubes)

#chapter 4-9
cubes2 = [value**3 for value in range(1,11)]
print(cubes2)


#chapter 4-10
veggies = ['squash','carrot','lettuce','spinach','pepper','zucchini','mushroom','onion','potato']
print('\nThe first three veggies are: ' + str(veggies[:3]))
print('The middle three veggies are: ' + str(veggies[3:6]))
print('The last three veggies are: ' + str(veggies[-3:]))

#chapter 4-11
friendpizzas = pizzas[:]
pizzas.append('anchovy')
friendpizzas.append('onion')

print('\nMy pizzas are: ' + str(pizzas))
print("My friend's pizzas are: " + str(friendpizzas))

#chapter 4-12 

myfoods = ['pizza', 'falafel', 'carrot cake']
friend_foods = myfoods[:]

myfoods.append('cannoli')
friend_foods.append('ice cream')

print('\nFoods that I like include: ')
for food in myfoods:
	print(food)

print('\nFoods that my friend likes include: ')
for food in friend_foods:
	print(food)

#chapter 4-13
buffet = ('pasta', 'salad', 'bread', 'pizza', 'chicken')
print('\nWe serve: ')
for item in buffet: 
	print(item)

print('\nOops, new buffet! \n')
buffet = ('pasta', 'salad', 'bread', 'lasagna', 'turkey')
print('Now we serve: ')
for item in buffet: 
	print(item)


