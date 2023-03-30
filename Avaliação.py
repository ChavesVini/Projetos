#Código simples para avaliação com 5 atibutos (pt-br)

lista_competencias = ['Pró-ativo', 'resiliência', 'gostaDesafios', 'comunicativo', 'trabalhoEquipe']
lista_notas = []
lista_notas_numero = []

for competencias in lista_competencias:
  lista = input(f'Qual sua nota a competência {competencias}? (B - Bom, R - Regular e I - Ruim) ')
  listagem = lista_notas.append(lista)

for nota in lista_notas:
  if nota == 'B':
    lista_notas_numero.append(3)
  elif nota == 'R':
    lista_notas_numero.append(2)
  elif nota == 'I':
    lista_notas_numero.append(1)
  elif not lista_notas:
    print('Letra inserida incorretamente.')
    
soma_lista = sum(lista_notas_numero)
media = soma_lista/3
print(f'A sua média é: {media}')
