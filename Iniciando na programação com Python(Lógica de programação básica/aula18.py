# Atribui o valor False à variável condicao1
condicao1 = False

# Atribui o valor False à variável condicao2
condicao2 = False

# Atribui o valor True à variável condicao3
condicao3 = True

# Atribui o valor True à variável condicao4
condicao4 = True

# Verifica se condicao1 é True
if condicao1:
    # Este código só será executado se condicao1 for True (não será, pois condicao1 é False)
    print('Código para condição 1')
    print('Código para condição 1')

# Verifica se condicao2 é True, caso condicao1 seja False
elif condicao2:
    # Este código só será executado se condicao2 for True (não será, pois condicao2 é False)
    print('Código para condição 2')

# Verifica se condicao3 é True, caso as condições anteriores sejam False
elif condicao3:
    # Este código será executado porque condicao3 é True
    print('Código para condição 3')

# Verifica se condicao4 é True, caso as condições anteriores sejam False
elif condicao4:
    # Este código não será executado porque condicao3 já foi satisfeita
    print('Código para condição 4')

# Caso todas as condições anteriores sejam False, executa o código dentro do else
else:
    # Este código só será executado se nenhuma das condições anteriores for True
    print('Nenhuma condição foi satisfeita.')

# Verifica se 10 é igual a 10 (sempre True)
if 10 == 10:
    # Como a condição é True, este código será executado
    print('Outro if')

# Este código é executado independentemente de qualquer condição anterior
print('Foras dos if')
