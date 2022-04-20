# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# nums_to_million = [x for x in range(1,1_000_001)]
# # for number in nums_to_million:
# #     print(number)


# # 4-5. Summing a Million: Make a list of the numbers from one to one million,
# # and then use min() and max() to make sure your list actually starts at one and
# # ends at one million. Also, use the sum() function to see how quickly Python can
# # add a million numbers.

# max_of_nums = max(nums_to_million)
# min_of_nums = min(nums_to_million)
# sum_of_nums = sum(nums_to_million)

# print("The min is: {:,} and the max is {:,}! The sum of the numbers from 1 to 1,000,000 is {:,}".format(min_of_nums,max_of_nums,float(sum_of_nums)))

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

numbs = list(range(3,31))
multiples_of_three = []
for number in numbs:
    if number%3==0:
        multiples_of_three.append(number)
    else:
        pass

print(multiples_of_three)
