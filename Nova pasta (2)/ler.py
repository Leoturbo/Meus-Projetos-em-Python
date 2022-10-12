# com with
with open("musica.txt", "w") as f:
  f.write("Testando escrita com with")

"""
f = open('teste2.txt', 'r')
for line in f:
  print(line)


f.close()"""

# Abra o arquivo (leitura)
arquivo = open('musica.txt', 'r', encoding='utf-8')
conteudo = arquivo.readlines()

# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
conteudo.append('Nova linha')

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
arquivo = open('musica.txt', 'w')
arquivo.writelines(conteudo)
arquivo.close()
