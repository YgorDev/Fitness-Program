def calcular_metabolismo(altura, peso, idade, genero):
    if genero == 'H':
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif genero == 'M':
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    

def calcular_get(taxa_metabolica, atividade, nivel):
    if nivel not in atividade:
        return None
    else:
        return taxa_metabolica * atividade[nivel]


def calcular_objetivo(get, objetivo , ajuste):
    if ajuste not in objetivo:
        return None
    else:
        return get + objetivo[ajuste]