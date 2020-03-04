import praw 
import googlefinance
import time
from yahoo_finance import Share

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Harvesting the reddit data
meme_stocks = input("Enter a list of ticker symbols: ")
stocks = meme_stocks.split(",")

times = []
shares = []
index_history = []
total_market_cap = 0

# Initialize pyplot
style.use('fivethirtyeight')
plt.ion()
graph = plt.plot(times, index_history)[0]

print(stocks[0])
share = Share(stocks[0])

# Convert the list of stocks to total_market_cap
# for stock in stocks:
    # share = Share(stock)
    # total_market_cap += share.get_market_cap()
    # shares.append(share)

# Normalize market cap
# index_divisor = total_market_cap/100

# Add value to index_history
# index_history.append(total_market_cap/index_divisor)
# time.append(time())

# while True:
#     new_market_cap = 0
# 
#     for share in shares:
#         share.refresh()
#         new_market_cap += share.get_market_cap()
#    
#     index_history.append(new_market_cap/index_divisor)
#     times.append(time())
# 
#     graph.set_data(time, index_history)
#     plt.draw()
#     plt.pause(0.01)
# 
#     sleep(60)

