# You must implement the check_sum() function which takes in a list and returns
# True if the sum of two numbers in the list is zero. If no such pair exists, return False
num_list = [10, -14, 26, 5, -3, 13, -5]


def check_sum(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if (num_list[i] + num_list[j] == 0):
                return True
    return False

print(check_sum(num_list))
