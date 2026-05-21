def calcular_metabolismo(altura, peso, idade, genero):
    if genero == 'H':
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif genero == 'M':
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161