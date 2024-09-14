# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')  # Solicita ao usuário que digite "entrar" ou "sair" e armazena a resposta na variável 'entrada'.

if entrada == 'entrar':  # Verifica se o valor digitado é igual a 'entrar'.
    print('Você entrou no sistema')  # Se a condição for verdadeira, exibe a mensagem de que o usuário entrou no sistema.
    print(12341234)  # Exibe o número 12341234 na tela.

elif entrada == 'sair':  # Se a primeira condição não for satisfeita, verifica se o valor digitado é igual a 'sair'.
    print('Você saiu do sistema')  # Se a condição for verdadeira, exibe a mensagem de que o usuário saiu do sistema.

else:  # Se nenhuma das condições anteriores for satisfeita (ou seja, o valor não foi 'entrar' nem 'sair'), executa o bloco abaixo.
    print('Você não digitou nem entrar e nem sair.')  # Exibe a mensagem informando que o usuário não digitou um valor válido.

print('FORA DOS BLOCOS')  # Esta linha será sempre executada, independentemente das condições anteriores, pois está fora do bloco condicional.