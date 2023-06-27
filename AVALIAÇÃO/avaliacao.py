from lista_competencias import lista_competencias

lista_letras = []
soma = 0

while len(lista_competencias) != len(lista_letras):
  for competencias in lista_competencias:
    nota = str(input(f'Qual sua nota para: {competencias}? '  
          '(B - Bom, R - Regular e I - Ruim) ')).upper()
    if all([nota != 'B', nota != 'R', nota != 'I']):
      print(f'Letra inserida incorretamente! Tente novamente.')
      lista_letras.clear()
      break
    else:
      lista_letras.append(nota)

for nota in lista_letras:
  if nota == 'B':
    soma += 3
  elif nota == 'R':
    soma += 2
  elif nota == 'I':
    soma += 1

media = soma/5
print(f'A sua média é: {media}')