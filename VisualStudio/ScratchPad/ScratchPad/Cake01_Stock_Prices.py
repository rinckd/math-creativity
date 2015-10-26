
def get_max_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    i = 0
    for outer_time in range(len(stock_prices_yesterday)):
       for inner_time in range(len(stock_prices_yesterday)):
           if outer_time == inner_time:
               continue

           earlier_time = min(outer_time, inner_time)
           later_time = max(outer_time, inner_time)
           earlier_price = stock_prices_yesterday[earlier_time]
           later_price = stock_prices_yesterday[later_time]
           potential_profit = later_price - earlier_price
           max_profit = max(max_profit, potential_profit)
    return max_profit

def get_max_profit2(stock_prices_yesterday):

    min_price = stock_prices_yesterday[0]
    max_profit = 0

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit

print(get_max_profit(test))
print(get_max_profit2(test))