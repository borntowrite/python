
#############################################
#
#############################################
def readGivenSize(filepath, size):
	f = open(filepath, 'rb')
	while True:
		read = f.read(size)
		print(read)
		if not read:
			break

readGivenSize('fred.txt', 10)

#############################################
#
#############################################
def countLines(filepath):
	with open(filepath, 'r') as f:
		line = f.readline()
		cnt = 1
		while line:
			print("Line {}: {}".format(cnt, line.strip()))
			cnt += 1
			line = f.readline()

#countLines('fred.txt')

#############################################
# 
#############################################
def readword(filepath):
	with open('fred.txt', 'r') as f:
		for line in f:
			for word in line.split():
				pass#print(word)

readword('fred.txt')