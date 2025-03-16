def calculate_factorials(n):
	if n == 1:
		return n
	
	return n * calculate_factorials(n - 1)

print(calculate_factorials(5))