###########################################
# O(n)
###########################################
def get_max_profit(prices):
	min_price = prices[0]
	max_profit = 0
	for price in prices:
		if price-min_price > max_profit:
			max_profit = price-min_price
		if min_price > price:
			min_price = price
	return max_profit

print(get_max_profit([3,7,1,6,4]))
print(get_max_profit([5,4,3,2,1]))

###########################################
# O(n^2)
###########################################
def get_max_profit_2(prices):
	max_profit=0
	for a in range(len(prices)):
		for b in range(a, len(prices)):
			if prices[b]-prices[a] > max_profit:
				max_profit = prices[b]-prices[a]
	return max_profit

print(get_max_profit_2([3,7,1,6,4]))
print(get_max_profit_2([5,4,3,2,1]))