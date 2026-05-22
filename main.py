from Funçoes import calcular_metabolismo, calcular_get, calcular_objetivo
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
print('')
print(f'Seu gasto metabolico basal é de: {taxa_metabolica:.2f}kcal')
print('')

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
        if nivel not in atividade:
            print('Escolha uma opção valida!')
            continue
        break
    except (ValueError, TypeError):
        print('Digite uma opção valido!')

get = calcular_get(taxa_metabolica, atividade, nivel)
print('')
print(f'Seu Gasto energeico total de acordo com sua atividade fisica é de: {get:.2f}kcal')
print('')

objetivo = {
    1:-500,
    2:500,
    3:0
}
while True:
    try:
        ajuste = int(input('''Qual seu objetivo atual:
                           
1 = Perder Peso
2 = Ganhar Massa
3 = Manutenção                          
: '''))
        if ajuste not in objetivo:
             print('Escolha uma opção valida!')
             continue
        
        break
    except (ValueError, TypeError):
        print('Escolha um número valido!')

ajuste_objetivo = calcular_objetivo(get, objetivo, ajuste)
print('')
print(f'Para seu objetivo seu consumo calorido deve ser de {ajuste_objetivo:.2f}')
print('')