import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        if amount >= coin:
            change[coin] = amount // coin
            amount %= coin
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    change = {}
    remaining = amount
    for coin in sorted(coins, reverse=True):
        num_coins = remaining // coin
        if num_coins > 0:
            change[coin] = num_coins
            remaining -= num_coins * coin
    return change

amount = 1000

start_time = time.time()
find_coins_greedy(amount)
end_time = time.time()
greedy_time = end_time - start_time

start_time = time.time()
find_min_coins(amount)
end_time = time.time()
dynamic_programming_time = end_time - start_time

print("Greedy Algorithm Time:", greedy_time)
print("Dynamic Programming Algorithm Time:", dynamic_programming_time)

if greedy_time < dynamic_programming_time:
    print("Greedy Algorithm is faster.")
else:
    print("Dynamic Programming Algorithm is faster.")

