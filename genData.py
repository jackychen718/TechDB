import os
import random


def genData(n=10000):
	with open('output.txt','a') as f:	
		for i in range(n):
			key = random.randint(0,99)
			val = random.randint(0,500)
			strToWrite = str(key)+' '+str(val)+'\n'
			f.write(strToWrite)




if __name__=='__main__':
	genData(100000)