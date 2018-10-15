
########################################################
# CSV
########################################################
import csv
from datetime import datetime

path = "c:/work/python/google_stock_data.csv"
file = open(path)
# for line in file:
# 	print(line)

#lines = [line for line in open(path)]
# print(lines)
# print(lines[0])
# print(lines[0].strip())
# print(lines[0].strip().split(','))
#lines = [line.strip().split(',') for line in open(path)]
# print(lines)

file2 = open(path, newline='')
reader = csv.reader(file2)
header = next(reader) # the first line is the header
#data = [row for row in reader] # read the remaining data
#print(header)
#help(datetime.strptime)

data = []
for row in reader:
	date = datetime.strptime(row[0], '%m/%d/%Y') # Y must be capital / upper case 
	open_price = float(row[1])
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = int(row[5])
	adj_close = float(row[6])
	data.append([date, open_price, high, low, close, volume, adj_close])

#print(data)

# Compute and store daily stock returns
returns_path = "c:/work/python/google_returns.csv"
file3 = open(returns_path, 'w')
writer = csv.writer(file3)
writer.writerow(["Date", "Return"])
for i in range(len(data)-1):
	todays_row = data[i]
	todays_date = todays_row[0] # date
	todays_price = todays_row[-1] # adj_close
	#print(todays_date, todays_price)
	yesterdays_row = data[i+1]
	yesterdays_price = yesterdays_row[-1]
	daily_return = (todays_price - yesterdays_price) / yesterdays_price
	formatted_date = todays_date.strftime('%m/%d/%Y')
	writer.writerow([formatted_date, daily_return])


