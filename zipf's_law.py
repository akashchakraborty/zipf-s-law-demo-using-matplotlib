import matplotlib.pyplot as plt 

fname = input('Enter File : ')

hand = open(fname)

di = dict()

for lin in hand :
	lin = lin.rstrip()
	#print(lin) # checking if it is actually stripping
	wds = lin.split()
	#print(wds) # checking if words are being shown
	for w in wds:
		#print(w) # printing the individual words
		if w in di :
			di[w] = di[w] + 1
			#print("**EXISTING BRO!**")
		else :
			di[w] = 1
			#print('**NEW**')
		#print(di[w])
#print(di) # printing dictionary
#print(di.keys())

plt.bar(di.keys(),di.values())
plt.show()