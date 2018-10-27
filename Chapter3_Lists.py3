#Exercise 3-1 + 3-2 
names = ['adam', 'bette', 'claire', 'donald']
for name in names:
	print("I have a friend named " + name + ".")


#Exercise 3-3
transports = ['bicycle', 'skateboard', 'blades']
for transport in transports:
	print('I want to ride my ' + transport + ".")

#Exercise 3-4 + 3-5 + 3-6 + 3-7 +3-9

print("Guests at dinner: " + str(len(names)))
for name in names:
	print("Dear " + name + ", you are invited to my dinner!")

missingGuest = 2
print(names[missingGuest] + " can't make it.")

names[missingGuest] = "bina"

print("Guests at dinner: " + str(len(names)))
for name in names: 
	print("Dear " + name + ", you are invited to my dinner!")

print("There are more seats!")

names.insert(0, "zeina")
names.insert(2, "clifford")
names.append("elena")

for name in names:
	print("Dear " + name + ", you are invited to dinner!")

print("Oh no, there are only two seats!")

for value in range(len(names), 2):
	uninvited = names[value].pop()
	print("Sorry, " + uninvited + ", there's no seat for you.")

print("Guests at dinner: " + str(len(names)))
for name in names:
	print("Don't worry, " + name + ". You're still invited!")


del names[1]
del names[0]

print("Remaining guests: " + str(names))


#Exercise 3-8
locations = ['mendoza', 'santiago', 'valpaiso', 'chicago']
print("Where I've been: \n" + str(locations))

print("Alphabetically: \n" + str(sorted(locations)))

print("Where I've been again: \n" + str(locations))

locations.reverse();
print("Where I've been reversed: \n" + str(locations))

locations.reverse();
print("Where I've been again again: \n" + str(locations))

locations.sort()
print("Where I've been alphabetically: \n" + str(locations))

locations.sort(reverse=True)
print("Where I've been reverse alphabetically:\n" + str(locations))

#Exercise 3-10
bands = ['alvays', 'burial', 'caribou', 'diiv']
print("Bands :" + str(bands))

bands[0] = 'air'
print("Bands: " + str(bands))

bands.insert(2,'cannibal ox')
print('Bands: ' + str(bands))

bands.append('ema')
print('Bands: ' + str(bands))

removedBand = bands.pop()
print("I don't like " + removedBand)

print("Bands: " + str(bands))

bands.reverse()
print('Bands: ' + str(bands))

print('Bands temporarily sorted ' + str(sorted(bands)))

print("Bands: " + str(bands))

bands.sort()
print("Bands: " + str(bands))

bands.sort(reverse=True)
print("Bands: " + str(bands))