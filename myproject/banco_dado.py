db = {}

print('Bem-vindo aos seu banco')

while True:
	print('O que você quer fazer?')
	print('Digite [P] para Adiciona, [G] para Obter, [L] para Listar ou [Q] para Sair')

	action = input().upper()
	if action == 'P':
		k = input('Digite uma chave: ')
		d = input('Digite os dados: ')
		db[k] = d

	elif action == 'G':
		k = input('Digite a chave: ')
		if not k in db:
			print('chave não existe!')
		else:
			print('seus dados; %s' %db[k])
	elif action == 'L':
		print(f'DB contents: {db}')
	elif action == 'Q':
		print('ate logo!')
		break
	else:
		print('Alternativa incorreta!')