result = []
def generate_fibonacci_sequence(n):
	def generate(n, b1, b2):
		if n  == 0:
			return b1
		else:
			if b1 > 0:
				result.append(b1)
			return generate(n - 1, b2, (b1+b2))
		
	return generate(n, 0, 1)

generate_fibonacci_sequence(8)
print(result)