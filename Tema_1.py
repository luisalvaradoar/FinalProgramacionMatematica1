from itertools import combinations

def all_sub_suc(sucesion):
	R = []
	for n in range(2, len(sucesion)):
		sub_suc_n = tuple(combinations(sucesion, n))

		for j in sub_suc_n:
			R.append(j)

	for i in sucesion:
		R.append([i])
	return(R)

def suc_buena(sucesion, m):
	subs = all_sub_suc(sucesion)
	for s in subs:
		if sum(s)%m != 0:
			return(False)

	return(True)

def salida(sucesion, m):
	cont = 0
	subs = all_sub_suc(sucesion)
	for s in subs:
		if suc_buena(s, m):
			cont += 1

	return(cont)


def main():
	res = []
	T = int(input(''))
	for t in range(T):
		NM = input('')
		NM = NM.split(' ')
		m = int(NM[1])

		sucesion_str = input('')
		sucesion_str = sucesion_str.split(' ')
		sucesion = []
		for s in sucesion_str:
			sucesion.append(int(s))


		res.append(salida(sucesion, m))

	print('\n')
	for r in res:
		print(str(r))

main()