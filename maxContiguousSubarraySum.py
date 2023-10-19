
arr = [1,2,3,5,6,7,8,9]


def contiguosSubArray(arr):
  n = len(arr)

  max_sum = -1000000000

  for left in range(0, n):
    running_max = 0 
    for right in range(left, n):
      running_max += arr[right]

      max_sum = max(running_max, max_sum)

  return max_sum    



## Time complexity The provided algorithm is a nested loop that calculates the maximum sum of subarrays within the input array arr. Let's analyze its time complexity:

# The outer loop iterates over the left index of the subarray from 0 to n-1, where n is the length of the input array arr. This loop runs n times.

# The inner loop iterates over the right index of the subarray, starting from the current left index, and goes up to n-1. In the worst case, it also runs n times.

# Inside the inner loop, there are constant-time operations such as addition and comparison, which do not depend on the size of the input array.

# As a result, the overall time complexity of this algorithm is O(n^2), where 'n' is the length of the input array arr. This is because for each of the 'n' elements in the outer loop, the inner loop potentially iterates 'n' times in the worst case, leading to a quadratic time complexity.








# Where is the use case for this problem?:



# The problem addressed by this algorithm, which calculates the maximum sum of subarrays within an array, is a common one and has various practical use cases across different domains. Here are some examples:

# Financial Data Analysis: Analyzing stock prices, financial time series data, or any data with a temporal aspect often involves finding the maximum gain or loss within a given time period. This algorithm can be used to find the maximum profit that can be made by buying and selling stocks at different points in time.

# Image Processing: In image processing, you might want to find the region within an image that has the highest or lowest intensity. This algorithm can be adapted to calculate the maximum sum of pixel values in subregions of an image.

# Genomics: In bioinformatics, researchers may want to find the maximum sum of values within a sequence of DNA, RNA, or protein data. This could correspond to finding the most significant gene or protein sequence.

# Data Analytics: When dealing with time-series data or any form of sequential data, you may need to identify the subsequence with the highest cumulative value. For example, in web analytics, you might want to find the consecutive days with the highest website traffic.

# Resource Allocation: In resource management scenarios, such as allocating memory or processing power in a computer system, you may need to find the subarray with the maximum sum to make efficient resource allocation decisions.

# Dynamic Programming: This problem is a fundamental example in dynamic programming and serves as a basis for more advanced algorithms and optimizations. Understanding and solving this problem is crucial for learning dynamic programming techniques.

# Algorithm Development: In some cases, finding the maximum sum of subarrays is a component of a larger algorithm or problem-solving process. It can be used as a subroutine in more complex algorithms.

# These are just a few examples, and there are many other scenarios where finding the maximum sum of subarrays is a valuable tool for solving real-world problems efficiently.









# Stock Buy-Sell Problem 



def max_profit(prices):
    if not prices:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)  # Update the minimum price seen so far
        max_profit = max(max_profit, price - min_price)  # Calculate the maximum profit

    return max_profit

# Example usage:
stock_prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(stock_prices)
print("Maximum Profit:", profit)



# In this algorithm:

# We initialize max_profit to 0, which will store the maximum profit we can achieve.
# We initialize min_price to the first stock price, which will store the minimum price encountered while iterating through the prices.
# We iterate through the stock prices, and for each price:
# Update min_price to the minimum of the current min_price and the current price.
# Calculate the potential profit by subtracting min_price from the current price.
# Update max_profit to the maximum of the current max_profit and the potential profit.
# At the end of the iteration, max_profit will contain the maximum profit that can be obtained by buying and selling stocks within the given time period.

# In the example provided, with stock prices [7, 1, 5, 3, 6, 4], the maximum profit is 5, which corresponds to buying the stock at price 1 and selling it at price 6.




























  