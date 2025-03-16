import itertools

def count_all_subsets(n):
	result = [()]
	def find_permutations(number, numCombinations):
		if numCombinations == 0:
			return result
		
		numArray = list(range(1, number+1))

		for p in itertools.combinations(numArray, numCombinations):
			result.append(p)

		find_permutations(n, numCombinations - 1)

	test = n
	find_permutations(n, test)

	return len(result)

print(count_all_subsets(4))