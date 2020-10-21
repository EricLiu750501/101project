"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""



def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number you want to get
	:return:
	"""
	# absolute
	if n < 0:
		n = -n

	biggest = 0
	return find_largest_digit_helper(n, biggest)


def find_largest_digit_helper(n, biggest):
	# Base case
	if n < 10:
		if n > biggest:
			biggest = n
		return biggest
	else:
		# Recursion
		num = n % 10
		new_num = (n - num) // 10
		if num > biggest:
			biggest = num
		return find_largest_digit_helper(new_num, biggest)


if __name__ == '__main__':
	main()
