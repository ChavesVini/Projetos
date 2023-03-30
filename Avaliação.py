#Código simples para avaliação com 5 atibutos (pt-br)
lista_competencias = ['Pró-ativo', 'resiliência', 'gostaDesafios', 'comunicativo', 'trabalhoEquipe']
listagem_2 = []
lista_notas_numero = []

for competencias in lista_competencias:
  lista = input(f'Qual sua nota a competência {competencias}? (B - Bom, R - Regular e I - Ruim) ')
  if ((lista == 'b' and 'B') or (lista == 'r' and 'R') or (lista == 'i' and 'I')):
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

if ((listagem_2 == 'b' and 'B') or (listagem_2 == 'r' and 'R') or (listagem_2 == 'i' and 'I')):
  soma_lista = sum(lista_notas_numero)
  media = soma_lista/3
  print(f'A sua média é: {media}')
else:
  print(f'Letra inserida incorretamente.')
