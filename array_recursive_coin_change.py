
#############################################
# iteration + dynamic 
#############################################

coins = [1,2,5]
def change(total, coins):
    return change_helper(total, coins)

def change_helper(total, coins):
    combinations = [0 for i in range(total+1)]
    combinations[0]=1
    for coin in coins:
        for amount in range(1, len(combinations)):
            if amount >= coin:
                combinations[amount] += combinations[amount-coin]
    return combinations[total]

print("number of combos : ", change(12, coins))

#############################################################
# recursion with memonization
#############################################################

def combo(coins, amount):
    memo = {}
    return combo_helper(coins, amount, 0, memo)
def combo_helper(coins, amount, index, memo):
    if amount == 0:
        return 1
    if index >= len(coins):
        return 0
    key = str(amount) + "-" + str(index)
    if key in memo:
        return memo[key]
    amountwithcoin = 0
    ways = 0
    while amountwithcoin <= amount:
        remaining = amount - amountwithcoin
        ways += combo_helper(coins, remaining, index+1, memo)
        amountwithcoin += coins[index]
    memo.update({key: ways})
    return ways

print("number of combos : ", combo(coins,12))

#############################################################
# recursion 
#############################################################
coins = [1,2,5]
temp = []
def combo3(amount, current_coin, temp):
    if amount == 0:
        print("change is 0 ", temp)
        return 1
    if amount < 0:
        return 0
    nCombos = 0
    for i in range(current_coin, len(coins)):
        temp.append(coins[i])
        nCombos += combo3(amount-coins[i], i, temp)
        temp.pop()
    return nCombos

print("number of combos : ", combo3(12, 0, temp))