#Código simples para avaliação com 5 atibutos (pt-br)

lista_competencias = ['Pró-ativo', 'resiliência', 'gostaDesafios', 'comunicativo', 'trabalhoEquipe']
listagem_2 = []
lista_notas_numero = []

for competencias in lista_competencias:
  lista = str(input(f'Qual sua nota a competência {competencias}? (B - Bom, R - Regular e I - Ruim) '))
  if lista in {'b','B','r','R','i','I'}:
    lista = lista.upper()
    listagem = listagem_2.append(lista)
  else:
    break

for nota in listagem_2:
  if nota == 'B':
    lista_notas_numero.append(3)
  elif nota == 'R':
    lista_notas_numero.append(2)
  elif nota == 'I':
    lista_notas_numero.append(1)
  else:
    break

if (lista == 'B') or (lista == 'R') or (lista == 'I'):
  soma_lista = sum(lista_notas_numero)
  media = soma_lista/5
  print(f'A sua média é: {media}')
else:
  print(f'Letra inserida incorretamente.')
