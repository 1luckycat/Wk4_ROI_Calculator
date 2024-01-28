# How many even digits?
# Given an array of integers, return how many of them contain an even number of digits.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits


# def even_digs(array):
#     count = 0
#     even_count = 0
#     for i in array:
#         spl = str(i)
#         for j in spl:
#             count = 0
#             count += 
#             print(count)
#             if count % 2 == 0:
#                 even_count += 1
                
#     return even_count

# print(even_digs([12,345,2,6,7896]))
            



# def how_even_are_we(nums):
    
#     return sum(1 for num in nums if num % 2 == 0)

# print(how_even_are_we([555,901,482,1771]))




# def how_even_are_we(nums):    
#     even_count = 0
#     for num in nums:
#         if num % 2 == 0:
#             even_count += 1
            
#     return even_count

# print(how_even_are_we([12,345,2,6,7896]))




# Alex H's answer:

def how_even_are_we(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)
print(how_even_are_we([555,901,482,1771]))