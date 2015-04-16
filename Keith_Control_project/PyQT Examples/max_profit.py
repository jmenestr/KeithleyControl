__author__ = 'Justin M'
import random
import time
stock_prices_yesterday = [random.randint(300,500) for x in range(10000)]


def get_max_profit(stock_prices_yesterday):
    max_profit = 0
    #go through every time
    for earlier_time in range(len(stock_prices_yesterday)):
        #only go through time's later than earlier time
        for later_time in range(earlier_time+1,len(stock_prices_yesterday)):
            #calculate potential profit
            potential_profit = stock_prices_yesterday[later_time] - stock_prices_yesterday[earlier_time]
            #upate max_profit if we did better
            max_profit = max(max_profit,potential_profit)
    return max_profit

def get_max_profit2(stock_prices_yesterday):

    max_profit = 0

    # go through every time
    for outer_time in range(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in range(len(stock_prices_yesterday)):

            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit
startTime = time.time()
print(get_max_profit(stock_prices_yesterday))
endTime = time.time()
print(endTime-startTime)

times = []
for x in range(1000,10000,1000):
    stock_prices_yesterday = [random.randint(300,500) for i in range(x)]
    startTime = time.time()
    get_max_profit2(stock_prices_yesterday)
    endTime = time.time()
    times.append(endTime-startTime)

for num in times:
    print(num)