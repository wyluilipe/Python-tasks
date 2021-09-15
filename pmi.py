num1 = input()
num2 = input()

def sum(num1, num2):
	if num1[0] == '-':
		num1 = num1[1:]
	if num2[0] == '-':
		num2 = num2[1:]
	num1 = num1[::-1]
	num2 = num2[::-1]
	res = ''
	added = 0
	if len(num1) > len(num2):
		num2 += '0' * (len(num1) - len(num2))
	elif len(num2) > len(num1):
		num1 += '0' * (len(num2) - len(num1))
	for i in range(len(num1)):
		res += str((int(num1[i]) + int(num2[i]) + added) % 10)
		added = (int(num1[i]) + int(num2[i])) // 10
	if added != 0:
		res += str(added)
	return res[::-1]

def multiply(num1, num2):
	sign1 = True # True equal sign '+'
	sign2 = True
	if num1[0] == '-':
		sign1 = False
		num1 = num1[1:]
	if num2[0] == '-':
		sign2 = False
		num2 = num2[1:]
	num1 = num1[::-1]
	num2 = num2[::-1]
	if len(num1) > len(num2):
		num2 += '0' * (len(num1) - len(num2))
	elif len(num2) > len(num1):
		num1 += '0' * (len(num2) - len(num1))
	ares = []
	for i in range(len(num1)):
		added = 0
		ares1 = '0' * i
		for j in range(len(num2)):
			ares1 += str((int(num1[i]) * int(num2[j]) + added) % 10)
			added = (int(num1[i]) * int(num2[j]) + added) // 10
		if (added != 0):
			ares1 += str(added)
		ares.append(ares1)
	for i in range(len(ares)):
		ares[i] = ares[i][::-1]
		j = 0
		while j < len(ares[i]) - 1 and ares[i][j] == '0':
			j+=1
		ares[i] = ares[i][j:]
	res = ares[0]
	for i in range(1, len(ares)):
		res = sum(res, ares[i])
	if sign1 != sign2:
		return '-' + res
	else:
		return res

print(multiply(num1, num2))