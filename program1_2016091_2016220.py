import time

while True:
    option = input("\n\n1. Print.\n2. Sum of numeric field.\n3. Exit.\n\nChoose option: ")
    print()

    if (option == '1'):
        start=time.time()
        datafile = open("GenData.txt", "r")

        for line in datafile:
            words = line.split(',')
            print(words[0] + " " + words[1] + " " + words[2])
            '''for i in words:
                print(" "+i, end='')
            print()'''
        datafile.close()
        print("\n\nTIME:"+str(time.time()-start))
    elif (option == '2'):
        datafile = open("data.txt", "r")

        field = input("Enter field name: ")
        if (field == "Price") | (field == 'price'):
            datafile = open("data.txt", "r")

            sum = 0
            datafile.readline()
            for line in datafile:
                words = line.split(',')
                sum += float(words[2])

            print("\n" + str(sum) + "\n")

        else:
            print("\nError: Field does not exist or has non-numeric values.\n")

    elif (option == '3'):
        break

    else:
        print ("Wrong option!")
        