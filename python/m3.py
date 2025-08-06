    #Lambda Function

square = lambda x: x * x
print(square(5))  # Output: 25


   #map

nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9]


   #filter

nums = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]


   #reduce
   
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # 10
