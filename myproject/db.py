from time import sleep


def inicial():
	print(100*'#')
	print('	                         BEM-VINDO AO CRIADOR DE BANCO DE DADOS')
	print(	100*'#')
	print()

def menu():
	
	print(	100*'¨')
	print('               	Digite [D] para Adiciona, [O] para Obter, [L] para Listar ou [Q] para Sair')
	print(	100*'¨')




def consulta_banco():
	k = input('Digite a chave: ')
	if not k in db:
		sleep(2)
		print('chave não exite!')
	else:
		print(f'seus dados: {db[k]}')

def lista():
	sleep(1.5)
	print(f'DB contents: {db}')


db = {}
inicial()
sleep(2)


while True:

	menu()

	action = input('db%: ').upper()

	if action == 'D':
		k = input('Digite uma chave: ')
		d = input('Digite os dados: ')
		db[k] = d

	elif action == 'O':
		consulta_banco()

	elif action == 'L':
		lista()
		
	elif action == 'Q':
		print('ate logo!')
		break
	else:
		print('Alternativa Incorreta!')

