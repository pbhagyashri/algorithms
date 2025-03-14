def segregate_evens_and_odds(numbers):
	l = 0
	r = len(numbers) - 1
	i = 0

	while i <= r:  # Change to <= to include the last element
		if numbers[i] % 2 == 0:  # Check if the number is even
			numbers[l], numbers[i] = numbers[i], numbers[l]  # Swap even number to the left
			l += 1
		i += 1
	
	return numbers

numbers = [4, 9, 5, 2, 9, 5, 7, 10] # [10, 4, 2, 5, 9, 5, 7, 9]
print(segregate_evens_and_odds(numbers))

