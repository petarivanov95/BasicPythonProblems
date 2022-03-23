
# a simple program to calculate the average of test scores

num_of_students = int(input("How many students do you have? ")) #takes in the number of students that are going to be calculated

num_test_scores = int(input("How many tests has each student taken? ")) #takes in the number of tests each of the students has taken

# the for loop below is used to take the scores that each student has gotten for each test and calculate his or her average
for student in range(num_of_students):
    total = 0
    print("student #", student+1)
    for test_num in range(num_test_scores):
        print ("test number:", test_num+1, end=" ")
        score = float(input(": "))
        total += score

    average = round(total/num_test_scores,2)
    print("Student # {} has an average of: {}".format(student+1,average))


