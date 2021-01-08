

# a number
x = 5
y = -10.6

# strings
hello = "Hi, Python!"

pythonIsHard = False
pythonIsFun = True



#======================================================================================
# Printing

city0 = "Evanston"
city1 = "Chicago"
cities = city0 + " and " + city1
print(cities)

# printing things
print("hello")	# prints "hello"
print(hello)	# prints "Hi, Python!"


print("the best number is " + str(x) + ", but " + str(y) + " is good too")
print(f"the worst number is {x}, but {y} is bad too.")
print(f"....but {y + x + 1000} would be the best number")

# assert city0 == city1, f"cities should be the same! {city0} {city1}"


#======================================================================================
# Comparisons

print(city0 != city1 or x == y)

city0 != city1 or not x == y
(city0 != city1) or not (x == y)

# comparing things
notTheSame = x != y
stillNotTheSame = not x == y
print(f"notTheSame: {notTheSame}")
print(f"stillNotTheSame: {stillNotTheSame}")

citiesNotTheSame = city0 != city1
numbersNotTheSame = not (x == y)
allDifferent = citiesNotTheSame and citiesNotTheSame
print(f"citiesNotTheSame:{citiesNotTheSame}, numbersNotTheSame:{numbersNotTheSame}")
print(f"allDifferent:{allDifferent}")

if x > y:
	print(f"{x} is bigger than {y}")
elif x == y:
	print(f"{x} is the same as {y}")
else:
	print(f"{x} is less than {y}")


if city0 > city1:
	print(f"{city0} is after {city1}")
elif city0 == city1:
	print(f"{city0} is the same as {city1}")
else:
	print(f"{city0} is before {city1}")


#======================================================================================
# Lists


# creating an list... 
# you can do this by declaring one, or using the range function
arr0 = [0,1,2,3,4]
arr1 = range(0,5)

print(f"arr0 is: {arr0}")
print(f"arr0 is: {arr1}")


allExes = "X"*15
squareList = [number*number for number in arr0]

print(f"allExes is: {allExes}")

evenSquareList = [x for x in squareList if (x%2==0)]

print(f"squareList is: {squareList}")
print(f"evenSquareList is: {evenSquareList}")


for i in range(5):
    print (f"The square of {i} is {i*i}")


for number in evenSquareList:
    print (f"{number} is an even square")

elements = ["water", "air", "fire", "earth", "love"]
print(f"The first element is {elements[0]}")
print(f"The final element is {elements[-1]}")

elements[0] = "skittles"
print(f"The first element is {elements[0]}")

laughter = []
while len(laughter) < 4:
	laughter.append("ha")
	print(laughter)


print(f"The middle elements are: {elements[1:3]}")
print(f"All but the first elements: {elements[0:-1]}")

# x = 5
# print(elements[x])

# planets = ("jupiter", "saturn", "uranus", "neptune", "pluto")
# planets[5] = "xena"

#======================================================================================
# Functions

import math
def getDistance(x, y, z): 
	sum = x*x + y*y + z*z
	return math.sqrt(sum)

vx = 5
vy = 10
vz = 15
dist = getDistance(vx, vy, vz)
print(f"The length of a vector {vx} {vy} {vz} is {dist}, about {round(dist)}")

#======================================================================================
# Loops

count = 5
while count > 0:
	count = count - 1
	print(f"countdown: {count}")
print("*boom!*")

# run forever....
# count = 5
# while count > 0:
# 	count = count + 1
# 	print(f"never gonna: {count}")
# print("give you up!")

# Command-C or CTRL-C will break the infinite loop



#======================================================================================
# Dictionaries

translations = {
	"cat": {
		"spanish": "gato",
		"german": "katze", 
		"finnish": "kissa",
		"yoruba": "ologbo"},
	"dog": {
		"afrikaans": "hond",
		"gujarati": "kutto",
		"hawaiian": "ilio"
	}
}


catDictionary = translations["cat"]
# Get all the keys of a dictionary
catLanguages = catDictionary.keys()

for lang in catLanguages:
	print(f"'cat' in {lang} is '{catDictionary[lang]}' ")

canTranslateFish = "fish" in translations
print(f"Can I translate 'fish' with this dictionary? {canTranslateFish}")

if "french" in catLanguages:
	print(f"'A French cat is '{catDictionary['french']}' ")
else:
	print("No cat translation for French")


#======================================================================================
# Classes

class Cat:
	catWord = "meow"

	def __init__(self, name):
		self.fish = 0
		self.mood = "happy"
		self.name = name
	
	def speak(self):
		return f"{self.name} says '{self.catWord}'"
	
	def __str__(self): 
		return f"{self.name}, a {self.mood} cat"

cat0 = Cat("Bustopher")
cat1 = Cat("Grizabella")
cat1.mood = "sad"

print(cat0)
print(cat1)

print(cat0.speak())
print(cat1.speak())

