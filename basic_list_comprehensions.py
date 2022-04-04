# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

nums_to_million = [x for x in range(1,1_000_001)]
for number in nums_to_million:
    print(number)
