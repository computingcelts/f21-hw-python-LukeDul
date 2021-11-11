# Homework 5

def compute_avg(values):  # finds average of a list of numbers
    if type(values) == list:
        summation = 0
        count = 0

        for n in values:                # loops through elements in list once
            summation = summation + n   # sums all numbers in list
            count += 1                  # count of numbers in list

        print(summation, '/', count, '=')
        return summation / count  # average
    else:
        return 'Invalid Argument: Datatype must be a list'


def compute_greatest(values):  # locates the largest number in a list of numbers
    if type(values) == list:
        biggest = values[0]  # binds the first element in the list to (biggest) as a starting point

        for n in values:  # checks if each element in the given list is larger than the previous
            if n > biggest:
                biggest = n

        return biggest
    else:
        return 'Invalid Argument: Datatype must be a list'


test_A = [10, 20, 5, 4, 9, 30, 8, 7, 17]  # given list

test_B = [9, 6, 15, 41, 90, 31, 82, 47, 0]  # given list

avg_test = [n for n in range(10, 51)]  # creates a list of numbers from 10 to 50

print(compute_avg(avg_test))  # invokes (compute_avg) with the argument (avg_test)

print(compute_greatest(test_A))  # invokes (compute_greatest) with the argument (test_A)

print(compute_greatest(test_B))  # invokes (compute_greatest) with the argument (test_B)


