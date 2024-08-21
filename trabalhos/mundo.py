import os
from random import randint
from time import sleep

def gera_mundo(n):
	mundo = [0]*n
	for i in range(n):
		mundo[i] = (2 if randint(0, 6) == 0 else 0)
	mundo[randint(0, n-1)] = 1
	return mundo	

def printm(pos, m, pos_perdido):
	os.system('cls' if os.name == 'nt' else 'clear')
	n = len(m)
	s = ''
	for i in range(n):
		if i != pos and i != pos_perdido:
			s += ' '
		elif i == pos:
			s += '@'
		elif pos_perdido >= 0:
			s += 'i'
	print(s + '\n', end='\033[91m')
	for i in range(n):
		print(('M' if m[i] == 2 else 'Q'), end='')
	print(end='\033[0m\n')
	sleep(0.25)
