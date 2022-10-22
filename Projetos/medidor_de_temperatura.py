tempo = input('Digite sua temperatura atual: ');
if tempo < '0':
	print('Congelando...')
elif '0' <= tempo <= '20':
	print('Frio')
elif '21' <= tempo <= '25':
	print('Normal')
elif '26' <= tempo <= '35':
	print('Quente')
else:
	print('Muito Quente!')