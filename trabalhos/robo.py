from mundo import printm

def efetua_passo(pos, mundo, direcao, passo):
	if passo <= 0:
		return -1
	elif direcao == "esquerda" or direcao == "e":
		passo *= -1
	elif direcao == "direita" or direcao == "d":
		pass
	else:
		passo *= -1
	n = len(mundo)
	printm(pos, mundo, -1)
	for _ in range(abs(passo)): #repete 'passo' vezes
		k = (1 if passo > 0 else -1)
		if pos + k < 0 or pos + k == n:
			return -1
		if mundo[pos + k] == 1:
			printm(pos, mundo, pos+k)
			return pos + k
		else:
			pos += k
		printm(pos, mundo, -1)
	return -1
