def raise_money(target: int):

	if target == 100000:
		print(target)
		return target
	
	raise_money(target + 1000)

raise_money(0)