from Funçoes import calcular_metabolismo
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
