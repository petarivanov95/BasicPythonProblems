#Starting out with Python Gaddis pages 352 and 353 problems

#Algo Workbench

#1

# list1 = ['Galileo','Oliver','Ostwald','Descartes']

# for r in range(len(list1)):
#     print(list1[r][0])


#2

# list_list = [1,2,3,4]
# def sum_function(my_list):
#     total = 0
#     for x in my_list:
#         total += x
#     return total

# print(sum_function(list_list))

#3

#PROGRAMMING EXERCISES

#6  --- Larger than n

number_n=6
simple_list = [1,2,5,23,5,6,7,3,32,1,2,33,4,5,64,1,23]

def larger_than_n(a_list, number):
    numbers_larger_than_n = []
    for x in a_list:
        if x > number:
            numbers_larger_than_n.append(x)
        else:
            continue
    return numbers_larger_than_n

print(larger_than_n(simple_list,number_n))

