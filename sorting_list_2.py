#############################################################
# Alkaline earth metals
#############################################################
### List
earth_metals_list = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals_list.sort()
print("reverse=False", earth_metals_list)
earth_metals_list.sort(reverse=True)
print("reverse=True", earth_metals_list)
# Tuple
earth_metals_tuple = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
#earth_metals_tuple.sort() --> tuple does not provide sort() hence throw error
earth_metals_tuple_sorted = sorted(earth_metals_tuple)
print("original: ", earth_metals_tuple)
print("sorted: ", earth_metals_tuple_sorted)

#help(list.sort)
"""sort(...)
   L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*"""

planets = [
	("Mercury", 2440, 5.43, 0.395),
	("Venus", 6052, 5.24, 0.723),
	("Earth", 6378, 5.52, 1.000),
	("Mars", 3396, 3.93, 1.530),
	("Jupiter", 71492, 1.33, 5.210),
	("Saturn", 60268, 0.69, 9.551),
	("Uranus", 25559, 1.27, 19.213),
	("Neptune", 24764, 1.64, 30.070)
]

# x = lambda planet: planet[0] # print 1st parameter in list
x = lambda planet: planet[1]
planets.sort(key=x, reverse=True)
print(planets)