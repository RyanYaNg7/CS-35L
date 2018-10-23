words = ['cat', 'window', 'defenestrate']

for w in words:
	print(w, len(w))

for n in range(2, 10):
	print('n is', n)

#Continue to continue with next iteration
for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)
