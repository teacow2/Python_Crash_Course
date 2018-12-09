# Exercise 7-1
carType = input('What kind of car would you like to rent? ')
print('Let me see if I can find that ' + carType.title() + '.')

# Exercise 7-2
reserveNum = input('How many people are in your party? ')
reserveNum = int(reserveNum)
if reserveNum > 8:
	print("You will need to wait for some tables to clear.")
else:
	print('Your table is ready.')


# Exercise 7-3
numOfTen = input('Give me a number to check: ')
numOfTen = int(numOfTen)
if numOfTen%10 == 0:
	print(str(numOfTen) + " is a multiple of 10.")
else:
	print(str(numOfTen) + " is not a multiple of 10.")

# Exercise 7-4 
promptRead = False 
prompt = "Give me a topping for your pizza: "
pizzaTopping = ""
while pizzaTopping != 'quit':
	if promptRead: 
		print(pizzaTopping.title() + ' will be added to your pizza. \n')
	pizzaTopping = input(prompt)
	promptRead = True
	
# Exercise 7-5 + 7-6
moviePrompt = "Thanks for coming to the cinema. How old are you? "
movieActive = True
while movieActive: 
	moviePrice = input(moviePrompt)
	if moviePrice == 'quit':
		break
	moviePrice = int(moviePrice)
	if moviePrice < 3:
		print('Your ticket is free')
	elif moviePrice < 12:
		print('The ticket is $10')
	else:
		print('The ticket is $15')

# Exercise 7-7

# infiniteCheck = 'a'
# while infiniteCheck == 'a':
# 	print('Continuing this stupid loop')


# Exercise 7-8 + 7-9

sandwich_orders = ['reuban', 'pastrami', 'cuban', 'pastrami', 'italian', 'club', 'pastrami']
finished_sandwiches = []
print('Welcome to the deli. Unfortunately, we ran out of pastrami.')

while 'pastrami' in sandwich_orders: 
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	made_sandwich = sandwich_orders.pop()
	print('I made your ' + made_sandwich + ' sandwich.')
	finished_sandwiches.append(made_sandwich)

print('I made the following sandwiches:')
for sandwich in finished_sandwiches:
	print(sandwich)


# Exercise 7-10
response = {}

polling_active = True
next_person = True

while polling_active:
	if next_person: 
		name = input('What is your name? ')
		destination = input('Where would you like to go on a dream vacation? ')

		response[name] = destination

	continue_question = input('Is there another person with a dream vacation? ')
	if continue_question.lower() == 'yes':
		next_person = True
		continue
	elif continue_question.lower() == "no":
		polling_active = False
	else:
		print("Please answer yes or no.")
		next_person = False 

for key, value in response.items():
	print(key.title() + "'s dream vacation is " + value.title() + '.')

