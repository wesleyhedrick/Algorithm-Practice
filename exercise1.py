# 1. Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
nums = [1,2,7,8,4,0,4,7,0,3,7,0,45,3,2,5,6,7,8,9,9,0,9,8,77,0,7,7,0,8,9,0,8,9,98,9]

def sortzeroes(list_of_numbers):
    z_list = []
    for num in list_of_numbers:
        if num == 0:
            z_list.append(num)
            list_of_numbers.remove(num)
    list_of_numbers.extend(z_list)
    return list_of_numbers

print(sortzeroes(nums))

# 2. Write a function that counts the number of times the number 7 occurs in a given integer
# # without converting it to a string.


# # For example the number 7,704,793 would output 3
# 3. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

my_list = [1,2,3,4]
target = 7




# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.
# # Examples and clarification here: https://leetcode.com/problems/two-sum/
# # Example 1:
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Because nums[0] + nums[1] == 9, we return [0, 1].
# JEREMY'S CHALLENGE:
# 4. You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# # For
# # a = [[1, 2, 3],
# #      [4, 5, 6],
# #      [7, 8, 9]]
# # the output should be
# # rotateImage(a) =
# #     [[7, 4, 1],
# #      [8, 5, 2],
# #      [9, 6, 3]]
