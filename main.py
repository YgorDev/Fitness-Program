from Funçoes import calcular_metabolismo, calcular_get
while True:
    try:
        altura = int(input('Digite sua altura em centimetro: '))
        peso = int(input('Digite seu peso em Kg: '))
        idade = int(input('Digite sua idade: '))
        break
    except ValueError:
        print('Digite apenas números!')

while True:
    genero = str(input('Digite seu Genero H(homem) M(mulher): ')).strip().upper()

    if genero not in ['H', 'M']:
        print('Digite um genero valido!')
    else:
        break

taxa_metabolica = calcular_metabolismo(altura, peso, idade, genero)
print(f'{taxa_metabolica}')

atividade = {
    1:1.2,
    2:1.375,
    3:1.55,
    4:1.725,
    5:1.9
}

while True:
    try:
        nivel = int(input('''Qual seu nivel de atividade fisita:
    1 = Sedentario
    2 = Leve
    3 = Moderado
    4 = Intenso
    5 = Muito Intenso
    : '''))
        break
    except ValueError, TypeError:
        print('Digite um valor valido!')

get = calcular_get(taxa_metabolica, atividade, nivel)
print(get)
