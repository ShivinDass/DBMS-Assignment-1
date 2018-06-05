from random import randint, uniform
import random
import string
meta=open("GenMetadata.txt","w")
dataType=["I","F","C"]
N=100000
typing=[]
byte=[]
for i in range(0, N):
	typing.append(dataType[randint(0,2)])
	byte.append(randint(10,21))
	meta.write(str(i)+","+typing[i]+","+str(byte[i])+"\n")

data=open("GenData.txt","w")
for i in range(0, N-1):
	data.write(str(i)+",")
data.write(str(N-1)+"\n")

for i in range(0,10):
	for j in range(0,N):
		if typing[j]=="C":
			data.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)))
		elif typing[j]=="I":
			data.write(str(randint(0,1000)))
		else:
			data.write(str(round(uniform(0,1000),2)))

		if j<N-1:
			data.write(",")
		else:
			data.write("\n")