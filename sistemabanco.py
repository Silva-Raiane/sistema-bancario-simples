menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f'Depositado de R$ {valor:.2f}\n'

        else: 
            print("Operação falhou! valor inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor a ser sacado:"))

        excedeu_saldo = valor > saldo

        excedeu_limite  = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE   

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Limite atingido")

        elif excedeu_saque:
            print("Número máximo de saques realizados")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}, restam R${saldo:.2f}\n"
            numero_saque += 1

        else: 
            print('Operacao Falha! Valor invalido')
    
    elif opcao == 'e':
        print(f'\n--- Extrato ---\n{extrato:.2f}')
    
    elif opcao == 'q':
        break

    else:
        print(f'Opção Inválida!\nTente novamente.')
