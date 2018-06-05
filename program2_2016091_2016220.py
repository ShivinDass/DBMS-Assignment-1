import time

metadata = open("GenMetadata.txt", "r")
meta = {}
filen="GenData.txt"

i = 0;
for line in metadata:
	words = line.split(',')
	meta[i] = words
	i += 1

while True:
	option = input("1. Print.\n2. Add data.\n3. New data.\n4. Sum of numeric field.\n5. Exit.\n\nChoose option: ")
	print()

	if (option == '1'):
		start=time.time()
		for line in metadata:
			words = line.split(',')
			meta[i] = words
			i += 1
		datafile = open(filen, "r")

		for i in range (0, len(meta)):
			print(meta[i][0], end = ' ')
		print("\n")

		datafile.readline()
		for line in datafile:
			words = line.split(',')
			for i in range (0, len(meta)):
				print(words[i], end = ' ')
			print()

		datafile.close()
		print("\n\nTIME:"+str(time.time()-start))
	elif (option == '2'):
		userfile = input("Enter file name: ")

		try:
			ufile = open(userfile, "r")
		except Exception:
			print("\nError: Can't load file.\n")
			continue

		datafile = open(filen, "a")

		ufile.readline()
		for line in ufile:
			datafile.write(line)

	elif (option == '3'):
		userfile = input("Enter file name: ")

		try:
			ufile = open(userfile, "r")
		except Exception:
			print("\nError: Can't load file.\n")
			continue

		datafile = open(filen, "w")

		for line in ufile:
			datafile.write(line)

	elif (option == '4'):
		datafile = open(filen, "r")

		field = input("Enter field name: ")

		isNumericField = False
		type = "x"
		col = -1

		for i in range (0, len(meta)):
			if field == meta[i][0]:
				if (meta[i][1] == "I") | (meta[i][1] == "F") | (meta[i][1] == "D"):
					isNumericField = True
					type = meta[i][1]
					col = i

		if isNumericField:
			datafile = open(filen, "r")

			sum = 0
			datafile.readline()
			for line in datafile:
				words = line.split(',')
				sum = round(sum+float(words[col]),2)

			if type == "I":
				sum = int(sum)

			print("\nSum: " + str(sum) + "\n")

		else:
			 print("\nError: Field does not exist or has non-numeric values.\n")

	elif (option == '5'):
		break

	else:
		print ("Wrong option!")
		