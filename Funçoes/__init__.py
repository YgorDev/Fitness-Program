def calcular_metabolismo(altura, peso, idade, genero):
    '''
    Calcular o metabolsimo basal do usuario

    Parametros:
    Peso (int): Peso por Kg
    Altura (int): Altura por Cm
    Idade (int): Idade do usuario
    Genero (str): H para Homem e M para Mulher

    '''
    if genero == 'H':
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif genero == 'M':
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    

def calcular_get(taxa_metabolica, atividade, nivel):
    '''
    Calcular a taxa de gasto energetico total do usuario
    
    Parametros:
    Taxa_metabolica (float): Pega o total do calculo do metabolismo basal
    Atividade (int): Pergunta a intencidade do usuario (sedentario, leve, moderado, intenso, muito intenso)
    Nivel (int): Pega o valor quantificado do nivel de atividade fisica do usuario

    '''
    if nivel not in atividade:
        return None
    else:
        return taxa_metabolica * atividade[nivel]


def calcular_objetivo(get, objetivo , ajuste):
    '''
    Calcula o objetivo que o usuario quer, entre (Perder Peso, Ganhar Massa, Manutenção)

    Parametros:
    Get (float): Gasto energetico total do usuario
    Objetivo (int): É as opçoes de atividade mostradas entre (Perder Peso, Ganhar Massa, Manutenção)
    Ajuste (int): Pega a o número correspondente a escolha do usuario para o calculo

    '''
    if ajuste not in objetivo:
        return None
    else:
        return get + objetivo[ajuste]