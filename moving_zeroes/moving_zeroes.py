'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
	# Your code here
	count = arr.count(0)
	for i in range(0, count):
		arr.remove(0)
		arr.append(0)
	return arr # returns in 0.000s


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# def moving_zeroes(arr):
#     # Your code here
#     for i in arr:
#         if i == 0:
#             arr.append(arr.pop(arr.index(0)))
#     return arr