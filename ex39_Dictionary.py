things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things


stuff = {'name': 'Matt', 'age': 20, 'height': 5}

print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "San Franciso"
print stuff['city']

print stuff

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]
print stuff


del stuff['city']
del stuff[1]
del stuff[2]
print stuff

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Franciso',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan abbriv is : ", states['Michigan']
print "Florida abbriv is : ", states['Florida']

print '-' * 10
print "Michigan has : ", cities[states['Michigan']]
print "Florida has : ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has the city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
state = state.get('Texas', None)

if not state:
    print "No Texas"

city = cities.get('TX', 'Does noot Exist')
print "The city for the state 'TX' is %s" % city