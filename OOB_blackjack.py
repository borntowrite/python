from enum import Enum

class Color(Enum):
	red = 1
	blue = 2
	yellow = 3
	black = 4

print(Color.red)
print(repr(Color.red))
for i in Color:
	print(repr(i))
